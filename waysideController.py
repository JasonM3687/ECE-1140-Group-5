import time
from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk
from tkinter import filedialog
from array import array
import re

class waysideController:


    def __init__(self,line,startBlocks,numBlocks):
        self.controllerName=line
        self.numBlocks=numBlocks
        self.lightStatuses = [0]*numBlocks
        self.blockOccupancies = []
        self.switchPositions = []
        self.blockSugSpeeds = [0]*numBlocks
        self.faultStatuses = [0]*numBlocks
        self.routedAuth = [0]*numBlocks
        self.underground = []
        self.trainLightSignals = [0]*numBlocks
        self.routedBlocks=[0]*numBlocks
        self.startBlocks=startBlocks
        
    def runPLC(self, file_path):
        exec(open(file_path).read())

    def getTrafficLightStatus(self):
        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()

        file.close()

        line_number=0
        line_number=self.findController(self.controllerName)
        line_number+=1
        return [int(s) for s in re.findall(r'\b\d+\b', Content[line_number])]

    def getCrossingStatus(self):
        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()

        file.close()

        line_number=0
        line_number=self.findController(self.controllerName)
        line_number+=5
        return Content[line_number].strip()[-1]

    def getTrainLightSignals(self):
        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()

        file.close()

        line_number=0
        line_number=self.findController(self.controllerName)
        line_number+=2
        return [int(s) for s in re.findall(r'\b\d+\b', Content[line_number])]
    
    def getBlockOccupancies(self):
        return self.blockOccupancies
        
    def getSwitchPositions(self):
        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()
        
        file.close()

        line_number=0
        line_number=self.findController(self.controllerName)
        return [int(s) for s in re.findall(r'\b\d+\b', Content[line_number])]

    def getBlockAuth(self):
        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()

        file.close()

        line_number=0
        line_number=self.findController(self.controllerName)
        line_number+=3
        AuthZero=[int(s) for s in re.findall(r'\b\d+\b', Content[line_number])]
        tempAuths=[]
        for i in range(len(AuthZero)):
            if AuthZero[i] == 1:
                tempAuths.append("0")
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
        line_number=0
        line_number=self.findController(self.controllerName[:-1]+"In")

        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()

        file.close()

        tempstring=""
        for i in range(len(self.blockOccupancies)):
            tempstring=tempstring+str(self.blockOccupancies[i])+","
        tempstring=tempstring[:-1]
        
        Content[line_number]="BlockOcc="+tempstring+"\n"

        with open('PLC_IO.txt','w') as file:
            file.writelines(Content)

        file.close()

    def setFaultStatuses(self, faults):
        self.faultStatuses.clear()
        for i in range(len(faults)):
            if(faults[i]!=0):
                self.faultStatuses.append(1)
            else:
                self.faultStatuses.append(0)

        line_number=0
        line_number=self.findController(self.controllerName[:-1]+"In")
        line_number+=1

        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()

        file.close()

        tempstring=""
        for i in range(len(self.faultStatuses)):
            tempstring=tempstring+str(self.faultStatuses[i])+","
        tempstring=tempstring[:-1]
        
        Content[line_number]="FaultStatuses="+tempstring+"\n"

        with open('PLC_IO.txt','w') as file:
            file.writelines(Content)
    
        file.close()

    def setUnderground(self, ug):
        self.underground.clear()
        for i in range(len(ug)):
            self.underground.append(ug[i])
        line_number=0
        line_number=self.findController(self.controllerName[:-1]+"In")
        line_number+=3

        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()

        file.close()

        tempstring=""
        for i in range(len(self.underground)):
            tempstring=tempstring+str(self.underground[i])+","
        tempstring=tempstring[:-1]
        
        Content[line_number]="underground="+tempstring+"\n"

        with open('PLC_IO.txt','w') as file:
            file.writelines(Content)

        file.close()

    def setRoutedBlocks(self, routeBlock):
        self.routedBlocks[routeBlock-1]=1
        line_number=0
        line_number=self.findController(self.controllerName[:-1]+"In")
        line_number+=2

        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()

        file.close()

        tempstring=""
        for i in range(len(self.routedBlocks)):
            tempstring=tempstring+str(self.routedBlocks[i])+","
        tempstring=tempstring[:-1]
        
        Content[line_number]="RoutedBlocks="+tempstring+"\n"

        with open('PLC_IO.txt','w') as file:
            file.writelines(Content)
        
        file.close()

    def getRoutedBlocks(self):
        return self.routedBlocks

    def clearRoutedBlocks(self, prevBlocks):
        self.routedBlocks[prevBlocks-1]=0
        line_number=0
        line_number=self.findController(self.controllerName[:-1]+"In")
        line_number+=2

        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()

        file.close()

        tempstring=""
        for i in range(len(self.routedBlocks)):
            tempstring=tempstring+str(self.routedBlocks[i])+","
        tempstring=tempstring[:-1]
        
        Content[line_number]="RoutedBlocks="+tempstring+"\n"

        with open('PLC_IO.txt','w') as file:
            file.writelines(Content)

        file.close()

    def setBlockAuthorities(self,routeBlock, blockAuth):
        self.routedAuth[routeBlock-1]=blockAuth
        line_number=0
        line_number=self.findController(self.controllerName)
        line_number+=4

        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()

        file.close()

        tempstring=""
        for i in range(len(self.routedAuth)):
            tempstring=tempstring+str(bin(self.routedAuth[i]))[2:]+","
        tempstring=tempstring[:-1]
        
        Content[line_number]="BlockAuth="+tempstring+"\n"

        with open('PLC_IO.txt','w') as file:
            file.writelines(Content)

        file.close()

    def getRoutedAuth(self):
        return self.routedAuth

    def setRoutedSpeeds(self,routeBlock,routeSugSpeed):
        self.blockSugSpeeds[routeBlock-1]=routeSugSpeed

    def getRoutedSpeeds(self):
        return self.blockSugSpeeds

    def findController(self,toFind):
        line_number=0
        with open("PLC_IO.txt",'r') as read_obj:
            for line in read_obj:
                line_number+=1
                if toFind in line:
                    return line_number
        read_obj.close()
