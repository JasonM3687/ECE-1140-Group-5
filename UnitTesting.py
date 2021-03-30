import unittest
import time
from MainDisplay import Ui_LoginWindow
from EngineerControl import Ui_EngineerWindow
from TrainDisplay import Ui_DisplayWindow
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest

class TestEngineer(unittest.TestCase):
	import sys
	app = QtWidgets.QApplication(sys.argv)
	EngineerWindow = QtWidgets.QMainWindow()
	
	engineerUI = Ui_EngineerWindow()
	engineerUI.setupUi(EngineerWindow)

	#Set up function
	def setUp(self):
		self.EngineerWindow.show()

	#Test setting Kp
	def testKpSet(self):
		#Inputs 2.0 for kp on UI then verify value is updated
		QtTest.QTest.qWait(3000)
		self.assertEqual(2.0, self.engineerUI.kpInput.value())

	def testKiSet(self):
		#Input 3 
		QtTest.QTest.qWait(3000)
		self.assertEqual(3.0, self.engineerUI.kiInput.value())

	def testTrainNumSet(self):
		QtTest.QTest.qWait(3000)
		self.assertEqual("1", self.engineerUI.trainNumOutput.text())

class TestDriver(unittest.TestCase):
	DriveWindow = QtWidgets.QMainWindow()
	driver = Ui_DisplayWindow()
	driver.setupUi(DriveWindow)

	def setUp(self):
		self.DriveWindow.show()

	def testSetSpeed(self):
		QtTest.QTest.qWait(3000)
		self.assertEqual(4.0, self.driver.speedInput.value())







if __name__ == "__main__":

	unittest.main()
	sys.exit(app.exec_())
