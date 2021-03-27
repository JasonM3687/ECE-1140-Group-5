import time
from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk
from tkinter import filedialog
from switch import switch
from trafficlight import trafficLight
from station import station
from block import block


class waysideController(object):
    def __init__(self, numLights, numSwitches, numStations, numBlock, lightNames, switchNames, stationNames, blockNames):
        self.lights = [trafficLight]*numLights
        self.switches = [switch]*numSwitches
        self.stations = [station]*numStations
        self.blocks = [block]*numBlock
        self.lightStatuses = []
        self.blockOccupancies = []
        self.switchPositions = []
        self.blockAuthorities = []
        self.blockSugSpeeds = []
        self.faultStatuses = []
        self.stationSales = []
        self.routedBlocks = []
        self.routedAuth = []

        for i in range(numLights):
            self.lights[i].changeLightName(lightNames[i])

        for i in range(numSwitches):
            self.switches[i].changeSwitchName(switchNames[i])

        for i in range(numStations):
            self.stations[i].changeStationName(stationNames[i])

        for i in range(numBlock):
            self.blocks[i].changeBlockName(blockNames[i])

        
    def setPLCinputs(self, Auth, Route):
        self.routedAuth = Auth
        for i in Route:
            self.routedBlocks[i]=Route[i]
        

    def runPLC(self, file_path):
        return 1

    def getTrafficLightStatus(self):
        lightStatuses=[]
        for i in self.lights:
            lightStatuses[i]=self.lights[i].getLightStatus()
        
        return lightStatuses

    def getTrainLightSignals(self):
        for i in self.blocks:
            self.trainLightSigs[i]=self.blocks[i].getTrainLightSignal()
    
    def getBlockOccupancies(self):
        for i in self.blocks:
            self.blockOccupancies[i]=self.blocks[i].getBlockOcc()

        return self.blockOccupancies

    def getSwitchPositions(self):
        for i in self.switches:
            self.switchPositions[i]=self.switches[i].getSwitchPosition()

        return self.switchPositions

    def getStationOccupancies(self):
        stationOccupancies=[]
        for i in self.stations:
            stationOccupancies[i]=self.stations[i].getStationOcc()

        return stationOccupancies

    def getBlockAuth(self):
        for i in self.blocks:
            self.blockAuthorities[i]=self.blocks[i].getBlockAuth()

        return self.blockAuthorities

    def getBlockSugSpeeds(self):
        for i in self.blocks:
            self.blockSugSpeeds[i]=self.blocks[i].getBlockSugSpeed()

        return self.blockSugSpeeds

    def getFaultStatuses(self):
        for i in self.blocks:
            self.faultStatuses[i]=self.blocks[i].getFaultStatus()

        return self.faultStatuses

    def getStationSales(self):
        for i in self.blocks:
            self.stationSales[i]=self.stations[i].getTicketSales()

    
    def setBlockOccupancies(self, blockOcc):
        for i in blockOcc:
            self.blocks[i].changeBlockOcc(blockOcc[i])

    def setStationOccupancies(self, stationOccupancies):
        for i in stationOccupancies:
           self.stations[i].changeStationOcc(stationOccupancies[i])

    def setTicketSales(self, sales):
        for i in sales:
            self.stations[i].changeTicketSales(sales[i])   

    def setBlockSugSpeeds(self, speed):
        for i in speed:
            self.blocks[i].changeBlockSugSpeed(speed)

    def setFaultStatuses(self, faults):
        for i in faults:
            self.blocks[i].changeFaultStatus(faults[i]) 

    def setUnderground(self, ug):
        for i in ug:
            self.blocks[i].changeUnderground(ug[i])

