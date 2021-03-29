import time
from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk
from tkinter import filedialog
from array import array

class waysideController:


    def __init__(self,section,line,start,numBlocks):
        self.waysideNumber=section
        self.waysideLine=line   
        self.controllerName=self.waysideLine+"Controller "+str(self.waysideNumber)
        self.startBlock=start
        self.numBlocks=numBlocks

        self.lightStatuses = [0]*numBlocks
        self.blockOccupancies = []
        self.switchPositions = []
        self.blockSugSpeeds = [0]*numBlocks
        self.faultStatuses = []
        self.routedAuth = [0]*numBlocks
        self.underground = []
        self.trainLightSignals = [0]*numBlocks
        self.routedBlocks=[0]*(numBlocks+2)

    def runPLC(self, file_path):
        exec(open(file_path).read())

    def getTrafficLightStatus(self):
        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()
        self.findController()
        self.line_number+=4
        return [int(i) for i in Content[self.line_number].split() if i.isdigit()]

    def getTrainLightSignals(self):
        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()
        self.findController()
        self.line_number+=8
        return [int(i) for i in Content[self.line_number].split() if i.isdigit()]
    
    def getBlockOccupancies(self):
        return self.blockOccupancies
        
    def getSwitchPositions(self):
        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()
        self.findController()
        self.line_number+=3
        return [int(i) for i in Content[self.line_number].split() if i.isdigit()]

    def getBlockAuth(self):
        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()
        self.findController()
        self.line_number+=5
        AuthZero=[int(i) for i in Content[self.line_number].split() if i.isdigit()]
        tempAuths=[]
        for i in range(len(AuthZero)):
            if AuthZero[i]:
                tempAuths.append(0)
            else:
                tempAuths.append(self.routedAuth[i])
        return tempAuths

    def getFaultStatuses(self):
        return self.faultStatuses
        
    def getUnderground(self):
        return self.underground

  
    def setBlockOccupancies(self, blockOcc):
        self.blockOccupancies.clear()
        for i in range(len(blockOcc)):
            self.blockOccupancies.append(blockOcc[i])
        self.findController()
        self.line_number+=1

        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()

        tempstring=""
        for i in range(len(self.blockOccupancies)):
            tempstring=tempstring+str(self.blockOccupancies[i])+","
        tempstring=tempstring[:-1]
        
        Content[self.line_number]="BlockOcc="+tempstring+"\n"

        with open('PLC_IO.txt','w') as file:
            file.writelines(Content)

    def appendBlockOccupancies(self,blockOcc):
        self.blockOccupancies.append(blockOcc)
        self.findController()
        self.line_number+=1
        print(self.line_number)
        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()

        tempstring=""
        for i in range(len(self.blockOccupancies)):
            tempstring=tempstring+str(self.blockOccupancies[i])+","
        tempstring=tempstring[:-1]
        
        Content[self.line_number]="BlockOcc="+tempstring+"\n"

        with open('PLC_IO.txt','w') as file:
            file.writelines(Content)

    def setFaultStatuses(self, faults):
        self.faultStatuses.clear()
        for i in range(len(faults)):
            if(faults[i]!=0):
                self.faultStatuses.append(1)
            else:
                self.faultStatuses.append(0)
        self.findController()
        self.line_number+=2

        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()

        tempstring=""
        for i in range(len(self.faultStatuses)):
            tempstring=tempstring+str(self.faultStatuses[i])+","
        tempstring=tempstring[:-1]
        
        Content[self.line_number]="FaultStatuses="+tempstring+"\n"

        with open('PLC_IO.txt','w') as file:
            file.writelines(Content)

    def appendBlockFaults(self,blockFault):
        if(blockFault!=0):
            self.faultStatuses.append(1)
        else:
            self.faultStatuses.append(0)

        self.findController()
        self.line_number+=2

        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()

        tempstring=""
        for i in range(len(self.faultStatuses)):
            tempstring=tempstring+str(self.faultStatuses[i])+","
        tempstring=tempstring[:-1]
        
        Content[self.line_number]="FaultStatuses="+tempstring+"\n"

        with open('PLC_IO.txt','w') as file:
            file.writelines(Content)

    def setUnderground(self, ug):
        self.underground.clear()
        for i in range(len(ug)):
            self.underground.append(ug[i])
        self.findController()
        self.line_number+=7

        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()

        tempstring=""
        for i in range(len(self.underground)):
            tempstring=tempstring+str(self.underground[i])+","
        tempstring=tempstring[:-1]
        
        Content[self.line_number]="underground="+tempstring+"\n"

        with open('PLC_IO.txt','w') as file:
            file.writelines(Content)

    def setRoutedBlocks(self, routeBlock):
        self.routedBlocks[routeBlock-self.startBlock]=1
        self.findController()
        self.line_number+=6

        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()

        tempstring=""
        for i in range(len(self.routedBlocks)):
            tempstring=tempstring+str(self.routedBlocks[i])+","
        tempstring=tempstring[:-1]
        
        Content[self.line_number]="RoutedBlocks="+tempstring+"\n"

        with open('PLC_IO.txt','w') as file:
            file.writelines(Content)

    def getRoutedBlocks(self):
        return self.routedBlocks

    def clearRoutedBlocks(self):
        self.routedBlocks=[0]*(self.numBlocks+2)

    def setBlockAuthorities(self,routeBlock, blockAuth):
        self.routedAuth[routeBlock-self.startBlock]=blockAuth

    def getRoutedAuth(self):
        return self.routedAuth
       
    def clearBlockAuthorities(self):
        self.routedAuth=[0]*self.numBlocks

    def setRoutedSpeeds(self,routeBlock,routeSugSpeed):
        self.blockSugSpeeds[routeBlock-self.startBlock]=routeSugSpeed

    def getRoutedSpeeds(self):
        return self.blockSugSpeeds
        
    def clearRoutedSpeeds(self):
        self.blockSugSpeeds=[0]*self.numBlocks

    def findController(self):
        self.line_number=0
        with open("PLC_IO.txt",'r') as read_obj:
            for line in read_obj:
                self.line_number+=1
                if self.controllerName in line:
                    return self.line_number