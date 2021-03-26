import trackModel
from trackModel import *

import unittest
class TestStringMethods(unittest.TestCase):
    def test_autoTrackHeat(self):
        ui.lineEdit.setText("Track Layout & Vehicle Data vF2.xlsx")
        ui.importTrack()
        block=ui.tracks[0]
        block.setTemp(31)
        self.assertEqual(block.heat,True)

    def test_trackCircuitDetection(self):
        ui.lineEdit.setText("Track Layout & Vehicle Data vF2.xlsx")
        ui.importTrack()
        ui.trains[0].posBlock=1
        ui.trains[0].posLine="Red"
        ui.refresh()
        self.assertEqual(ui.tracks[0].occ,1)
        
    def test_stationSalesShown(self):
        ui.lineEdit.setText("Track Layout & Vehicle Data vF2.xlsx")
        ui.importTrack()
        ui.stations[0].addSales(200)
        ui.stationUpdate()
        self.assertEqual(ui.sales1.text(),"200")
        
    def test_trackFailureModes(self):
        ui.lineEdit.setText("Track Layout & Vehicle Data vF2.xlsx")
        ui.importTrack()
        ui.tracks[0].fail=0
        ui.refresh()
        self.assertEqual(ui.stat_label.text(),"Clear")
        ui.tracks[0].fail=1
        ui.refresh()
        self.assertEqual(ui.stat_label.text(),"Broken Rail")
        ui.tracks[0].fail=2
        ui.refresh()
        self.assertEqual(ui.stat_label.text(),"Circuit Failure")
        ui.tracks[0].fail=3
        ui.refresh()
        self.assertEqual(ui.stat_label.text(),"Power Failure")
        
if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    unittest.main()