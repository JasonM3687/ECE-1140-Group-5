import unittest
from trainModel1 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest

class TestMethods(unittest.TestCase):

    def test_temperature(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        ui.setTemp1(72)
        self.assertEqual(72,ui.getTemp())
    
    def test_ebrake(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        ui.eBrakeToggled()
        self.assertEqual(-2.73,ui.getAcceleration())

    def test_sbrake(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        ui.setServiceBrake()
        self.assertEqual(-1.2,ui.getAcceleration())

    def test_Velocity(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        ui.calculateVelocity(300)
        self.assertEqual(ui.getVelocity(),ui.velocity)

    def test_Beacon(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        ui.setBeacon("hello")
        self.assertEqual("hello",ui.getBeacon())

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QtTest.QTest.qWait(1000)

    unittest.main()
