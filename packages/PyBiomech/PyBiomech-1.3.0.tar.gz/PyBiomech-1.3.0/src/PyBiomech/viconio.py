# -*- coding: utf-8 -*-

import numpy as np
from ViconNexus import ViconNexus

class ViconReader:
    
    def __init__(self):
        self.readerType = 'vicon'
        self.fileName = None
        self.vicon = ViconNexus()
        
    def readFromFile(self, fileName):
        pass
    
    def getVectorUnit(self, vecType):
        if vecType == 'marker':
            unit = 'mm'
        elif vecType == 'angle':
            unit = 'deg'
        return unit
    
    def getVectorFrequency(self):
        return self.vicon.GetFrameRate()
    
    def getNVectorFrames(self):
        self.nVectorFrames = self.vicon.GetFrameCount()
        return self.nVectorFrames
    
    def getNVectors(self):
        self.subjects = self.vicon.GetSubjectNames()
        self.subject = self.subjects[0]
        if len(self.subjects) != 1:
            raise Exception('not exactly one subject')
        self.markers = self.vicon.GetMarkerNames(self.subject)
        self.NMarkers = len(self.markers)
        self.modOutputs = self.vicon.GetModelOutputNames(self.subject)
        self.NModOutputs = len(self.modOutputs)
        self.NVectors = self.NMarkers + self.NModOutputs
        return self.NVectors
        
    def getVector(self, i):
        skip = False
        if i < self.NMarkers:
            label = self.markers[i]
            trajX, trajY, trajZ, trajExists = self.vicon.GetTrajectory(self.subject, label)
            data = np.array([trajX, trajY, trajZ]).T
            data[data==0.] = np.nan
            vecType = 'marker'
            if data.shape[0] == 0:
                skip = True
        else:
            label = self.modOutputs[i - self.NMarkers]
            group, components, types = self.vicon.GetModelOutputDetails(self.subject, label)
            [data, exists] = self.vicon.GetModelOutput(self.subject, label)
            print(group)
            if group in ['Modeled Markers','Angles']:
                trajX, trajY, trajZ = data
                data = np.array([trajX, trajY, trajZ]).T
                data[data==0.] = np.nan
                if group == 'Modeled Markers':
                    vecType = 'marker'
                elif group == 'Angles':
                    vecType = 'angle'
            else:
                skip = True
        if skip:
            label = None
            data = None
            vecType = None
        return label, data, vecType
    
    def getNEvents(self):
        self.events = []
        fr1, fr2 = self.vicon.GetTrialRange()
        print([fr1, fr2])
        for context in ['Right', 'Left', 'General']:
            for label in ['Foot Off', 'Foot Strike', 'Event']:
                eventFrames, eventOffsets = self.vicon.GetEvents(self.subject, context, label)
                for i in range(len(eventFrames)):
                    event = {}
                    event['label'] = label
                    event['context'] = context
                    event['frame'] = int(eventFrames[i] - fr1)
                    self.events.append(event)
        return len(self.events)
    
    def getEvent(self, i):
        event = self.events[i]
        label = event['label']
        context = event['context']
        frame = event['frame']
        return label, context, frame
    
    def getData(self):
        return self.readerType
    
    
class ViconWriter:
    
    def __init__(self):
        self.writerType = 'vicon'            
        self.vicon = ViconNexus()
        self.nVectorFrames = None
        
    def initEmpty(self):
        pass
        
    def initSpaceForNVectorFrames(self):
        pass
        
    def setNVectorFrames(self, nVectorFrames):
        self.nVectorFrames = nVectorFrames
        
    def setVectorUnit(self, vecType, unit):
        pass
        
    def setVectorFrequency(self, vecFreq):
        pass
        
    def addVector(self, label, data, vecType):
        self.subjects = self.vicon.GetSubjectNames()
        self.subject = self.subjects[0]
        existingMarkerNames = self.vicon.GetMarkerNames(self.subject)
        existingModelOutputNames = self.vicon.GetModelOutputNames(self.subject)
        if len(self.subjects) != 1:
            raise Exception('not exactly one subject')
        if vecType in ['marker', 'angle', 'translation', 'length']:
            Nf = data.shape[0]
            exists = np.array([True] * Nf)
            data_ = np.zeros((Nf, 3))
            if len(data.shape) < 2:
                data_[:,2] = data
            else:
                data_ = data
            exists[np.isnan(data_[:,2])] = False
            data_[np.isnan(data_)] = 0.
            dataList = data_.T.tolist()
            exists = exists.tolist()
            isOrigMarker = True
            if vecType == 'marker':
                if label not in existingMarkerNames:
                    isOrigMarker = False
                    if label not in existingModelOutputNames:
                        self.vicon.CreateModeledMarker(self.subject, label)
            elif vecType == 'angle':
                isOrigMarker = False
                if label not in existingModelOutputNames:
                    XYZNames = ['X','Y','Z']
                    anglesTypes = ['Angle'] * 3
                    self.vicon.CreateModelOutput(self.subject, label, 'Angles', XYZNames, anglesTypes)
            elif vecType == 'translation':
                isOrigMarker = False
                if label not in existingModelOutputNames:
                    XYZNames = ['X','Y','Z']
                    translationsTypes = ['Length'] * 3
                    self.vicon.CreateModelOutput(self.subject, label, 'Lengths', XYZNames, translationsTypes)
            elif vecType == 'length':
                isOrigMarker = False
                if label not in existingModelOutputNames:
                    XYZNames = ['X','Y','Z']
                    lengthsTypes = ['Length'] * 3
                    self.vicon.CreateModelOutput(self.subject, label, 'Lengths', XYZNames, lengthsTypes)
            if isOrigMarker:
                x, y, z = dataList
                self.vicon.SetTrajectory(self.subject, label, x, y, z, exists)
            else:
                self.vicon.SetModelOutput(self.subject, label, dataList, exists)
        
    def writeToFile(self, fileName):
        pass
        
    def setData(self, data):
        readerType = data[0]
        if readerType != self.writerType:
            raise Exception('reader and writer type must have the same type')
