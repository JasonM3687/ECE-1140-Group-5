import unittest
from SWTrackController import Ui_MainWindow

class TestSWTrackController(unittest.TestCase):
    #test switch positions for red line controllers
    def tests(self):
        for i in range(20):
            Ui_MainWindow.waysideControllers[0][i].setPLCinputs(Ui_MainWindow.blockOccupancies,Ui_MainWindow.blockAuthorities,Ui_MainWindow.faultStatuses,Ui_MainWindow.underground)
            self.assertEqual(Ui_MainWindow.waysideControllers[0][i].getSwitchPositions(), Ui_MainWindow.outputs, 'incorrect')
        #test switch positions for green line controllers
        Ui_MainWindow.waysideControllers[0][i].setPLCinputs(Ui_MainWindow.blockOccupancies,Ui_MainWindow.blockAuthorities,Ui_MainWindow.faultStatuses,Ui_MainWindow.underground)
        for j in range(26):
            self.assertEqual(Ui_MainWindow.waysideControllers[1][j].getSwitchPositions(),Ui_MainWindow.outputs, 'incorrect')


        #test Traffic light status for red line controllers
        Ui_MainWindow.waysideControllers[0][i].setPLCinputs(Ui_MainWindow.blockOccupancies,Ui_MainWindow.blockAuthorities,Ui_MainWindow.faultStatuses,Ui_MainWindow.underground)
        for i in range(20):
            self.assertEqual(Ui_MainWindow.waysideControllers[0][i].getTrafficLightStatus(),Ui_MainWindow.outputs, 'incorrect')
        #test Traffic light status for green line controllers
        Ui_MainWindow.waysideControllers[0][i].setPLCinputs(Ui_MainWindow.blockOccupancies,Ui_MainWindow.blockAuthorities,Ui_MainWindow.faultStatuses,Ui_MainWindow.underground)
        for j in range(26):
            self.assertEqual(Ui_MainWindow.waysideControllers[1][j].getTrafficLightStatus(),Ui_MainWindow.outputs, 'incorrect')


        #test block authorities for red line controllers
        Ui_MainWindow.waysideControllers[0][i].setPLCinputs(Ui_MainWindow.blockOccupancies,Ui_MainWindow.blockAuthorities,Ui_MainWindow.faultStatuses,Ui_MainWindow.underground)
        for i in range(20):
            self.assertEqual(Ui_MainWindow.waysideControllers[0][i].getBlockAuthorities(),Ui_MainWindow.outputs, 'incorrect')
        #test block authorities for green line controllers
        Ui_MainWindow.waysideControllers[0][i].setPLCinputs(Ui_MainWindow.blockOccupancies,Ui_MainWindow.blockAuthorities,Ui_MainWindow.faultStatuses,Ui_MainWindow.underground)
        for j in range(26):
            self.assertEqual(Ui_MainWindow.waysideControllers[1][j].getBlockAuthorities(), Ui_MainWindow.outputs, 'incorrect')


        '''test block train light signals for red line
        for i in range(20):
            self.assertEqual(Ui_MainWindow.waysideControllers[0][i].getTrainLightSignals(), #plc file calculation array of block train light signals)
        #test block train light signals for green line
        for j in range(26):
            self.assertEqual(Ui_MainWindow.waysideControllers[1][j].getTrainLightSignals(), #plc file calculation array of block train light signals)


        #test block faults for red line
        for i in range(20): 
            self.assertEqual(Ui_MainWindow.waysideControllers[0][i].getFaultStatuses(), #block faults array that the track model sends the wayside controller)
        #test block faults for green line
        for j in range(26):
            self.assertEqual(Ui_MainWindow.waysideControllers[1][j].getFaultStatuses(), #block faults array that the track model sends the wayside controller)


        #test block occupancies for red line
        for i in range(20):
            self.assertEqual(Ui_MainWindow.waysideControllers[0][i].getBlockOccupancies(), #block occupancy array sent from the track model)

        #test block occupancies for green line
        for j in range(26):
            self.assertEqual(Ui_MainWindow.waysideControllers[1][j].getBlockOccupancies(), #block occupancy array sent from the track model)


        #test station occupancies for red line
        for i in range(20):
            self.assertEqual(Ui_MainWindow.waysideControllers[0][i].getStationOccupancies(), #station occupancy array sent from the track model)
        #test station occupancies for green line
        for j in range(26):
            self.assertEqual(Ui_MainWindow.waysideControllers[1][j].getStationOccupancies(), #station occupancy array sent from the track model)'''

    