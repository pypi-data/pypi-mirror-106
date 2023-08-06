import numpy as np
import pathlib as pl
import msgpack
import struct
import os.path

from .types import *

def getEEGfromBinary(dataBytes, numChannels):
    unpackFormat = "=d{0}".format("f" * numChannels)
    eegReadData = list(struct.iter_unpack(unpackFormat, dataBytes)) 
    eegPreped = [i[1:(numChannels+1)] for i in eegReadData] # skip timestamp and pack
    eegNumpy = np.asarray(eegPreped).T
    eegTimestamps = np.asarray([i[0] for i in eegReadData])

    return eegNumpy, eegTimestamps

def getResFromBinary(dataBytes, numChannels):
    unpackFormat = "={0}".format("f" * numChannels)
    unpackedData = list(struct.iter_unpack(unpackFormat, dataBytes)) 
    data = np.asarray(unpackedData).T

    return data

def getStimuliFromBinary(dataBytes):
    unpackFormat = "=iid"
    stimuliData = list(struct.iter_unpack(unpackFormat, dataBytes)) 

    return [P300StimulusData(i[0], i[1], i[2]) for i in stimuliData]

class RecordReaderVisitor:
    def OnBegin(self):
        pass
    def OnEnd(self):
        pass
    def OnRawEEG(self, eegData:np.ndarray, eegTimestamps:np.array):
        pass
    def OnRawResistance(self, resData:np.ndarray):
        pass
    def OnP300ProcessingUnit(self, p300unit:P300ProcessingUnit):
        pass
    def OnInterfaceData(self, interfaceData):
        pass

UNDEFINED_STIMULUS = -1
TARGET_STIMULUS = 1
NONTARGET_STIMULUS = 0

class BasicReaderVisitor(RecordReaderVisitor):
    def __init__(self) -> None:
        super().__init__()

        self.eegData = []
        self.eegTimestamps = []
        self.stimuliTimestamps = []
        self.stimuliLabels = []
        self.stimuliIds = []

    def OnBegin(self):
        pass
        
    # Convert to numpy arrays
    def OnEnd(self):
        self.eegData            = np.hstack(self.eegData)           if self.eegData             else None
        self.eegTimestamps      = np.hstack(self.eegTimestamps)     if self.eegTimestamps       else None
        self.stimuliTimestamps  = np.hstack(self.stimuliTimestamps) if self.stimuliTimestamps   else None
        self.stimuliLabels      = np.hstack(self.stimuliLabels)     if self.stimuliLabels       else None
        self.stimuliIds         = np.hstack(self.stimuliIds)        if self.stimuliIds          else None

    def OnRawEEG(self, eegData:np.ndarray, eegTimestamps:np.array):
        self.eegData.append(eegData)
        self.eegTimestamps.append(eegTimestamps)
        
    def OnP300ProcessingUnit(self, p300unit:P300ProcessingUnit):
        targetStimulus = p300unit.targetStimulus

        for stimulusData in p300unit.stimuliData:
            self.stimuliTimestamps.append(stimulusData.timestamp)
            self.stimuliLabels.append(int(stimulusData.stimulusId == targetStimulus) if targetStimulus != UNDEFINED_STIMULUS else UNDEFINED_STIMULUS)
            self.stimuliIds.append(stimulusData.stimulusId)

class RecordReader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = open(filepath,'rb')
        success = RecordReader.__ReadMagic(self.file)
        assert success
        

    @staticmethod
    def __ReadMagic(file) -> bool:
        magic = file.read(5)
        return magic == b"CSRv1"

    @staticmethod
    def UnpackMetadata(filepath):
        datFilepath = pl.Path(filepath).with_suffix(".dat")   

        if not os.path.isfile(datFilepath):
            raise Exception("Session metadata .dat file was not found, unable to unpack metadata!") 

        with open(datFilepath,'rb') as file:
            data = msgpack.unpackb(file.read())
            return data

        return None


    @staticmethod
    def UnpackResistances(filepath):
        datFilepath = pl.Path(filepath).with_suffix(".res")   

        if not os.path.isfile(datFilepath):
            raise Exception("Session resistance .res file was not found, unable to unpack resistances!") 

        with open(datFilepath,'rb') as file:
            data = msgpack.unpackb(file.read())
            
            if not data:
                return None

        metadata = RecordReader.UnpackMetadata(filepath)
        #print(metadata)
        channelNames = metadata["deviceInfo"]["channelNames"]

        def RetrieveResistances(resSamples):
            numSamples = len(resSamples) // len(channelNames)
            resSamples = np.transpose(np.reshape(resSamples, (numSamples, -1)))

            resistancesDict = dict(zip(channelNames, resSamples))
            return resistancesDict

        return { "resBeforeSession": RetrieveResistances(data["resBeforeSession"]), 
                 "resAfterSession": RetrieveResistances(data["resAfterSession"]) }

    @staticmethod
    def Unpack(filepath, visitor:RecordReaderVisitor):
        datFilepath = pl.Path(filepath).with_suffix(".dat")
        recFilepath = pl.Path(filepath).with_suffix(".rec")

        if not os.path.isfile(recFilepath):
            raise Exception("Session record .rec file was not found, unable to unpack data!")

        numChannels = 0

        sessionMetadata = RecordReader.UnpackMetadata(datFilepath)
        numChannels = sessionMetadata["deviceInfo"]["numChannels"]

        with open(recFilepath,'rb') as file:
            if not RecordReader.__ReadMagic(file):
                raise Exception("Failed to read record, format signature not found.")

            visitor.OnBegin()

            while True:
                inBytes = file.read(16)

                if not inBytes: # EOF
                    break

                if len(inBytes) != 16:
                    raise Exception("Data is corrupted, unable to read packet header!")
                   
                unpackedPacketHeader = struct.unpack("=IqI", inBytes)
                packetType = CSRPacketType(unpackedPacketHeader[0])
                packetTimestamp = unpackedPacketHeader[1]
                packetSize = unpackedPacketHeader[2]

                if packetType == CSRPacketType.P300ProcessingUnit:
                    punit = msgpack.unpackb(file.read(packetSize))

                    unitId = punit[0]
                    actId = punit[1]
                    targetStimulus = punit[2]
                    stimuliCount = punit[3]
                    shouldEndLearn = punit[6]
                    eegBinaryData = punit[10]
                    stimuliBinaryData = punit[12]

                    eegNumpy, eegTimestamps = getEEGfromBinary(eegBinaryData, numChannels)
                    stimuliData = getStimuliFromBinary(stimuliBinaryData)

                    visitor.OnP300ProcessingUnit(P300ProcessingUnit(unitId, actId, targetStimulus, stimuliCount, eegNumpy, eegTimestamps, stimuliData, shouldEndLearn))
                elif packetType == CSRPacketType.RawEEG:
                    numSamples = struct.unpack("I", file.read(4))[0]
                    eegBinaryData = file.read(packetSize - 4)
                    
                    eegNumpy, eegTimestamps = getEEGfromBinary(eegBinaryData, numChannels)
                    assert eegNumpy.shape[1] == numSamples

                    visitor.OnRawEEG(eegNumpy, eegTimestamps)
                elif packetType == CSRPacketType.RawResistance:
                    numSamples = struct.unpack("I", file.read(4))[0]
                    resBinaryData = file.read(packetSize - 4)

                    resNumpy = getResFromBinary(resBinaryData, numChannels)
                    assert resNumpy.shape[1] == numSamples

                    visitor.OnRawResistance(resNumpy)
                elif packetType == CSRPacketType.InterfaceData:
                    visitor.OnInterfaceData(file.read(packetSize))
                else:
                    file.read(packetSize) # skip unknown packets

            visitor.OnEnd()