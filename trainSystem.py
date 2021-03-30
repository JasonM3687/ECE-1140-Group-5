import trainModel
import SWTrackControllerNew
import trackModel
import t1_1
import MainDisplay
from PyQt5 import QtWidgets

if __name__=='__main__':
    import sys
    
    trackApp=QtWidgets.QApplication(sys.argv)
    trackWindow=QtWidgets.QMainWindow()
    track=trackModel.trackModel()
    track.setupUi(trackWindow)
    track.importTrack()
    
    trainCApp=QtWidgets.QApplication(sys.argv)
    trainCWindow=QtWidgets.QMainWindow()
    trainC=MainDisplay.Ui_LoginWindow()
    
    trainApp=QtWidgets.QApplication(sys.argv)
    trainWindow=QtWidgets.QMainWindow()
    train=trainModel.Ui_MainWindow()
    train.trackModelInstance(track)
    train.trainControllerInstance(trainC)
    train.setupUi(trainWindow)
    
    trainC.setupUi1(trainCWindow)
    trainC.importTrain(train)
    
    trackWindow.show()
    trainWindow.show()
    trainCWindow.show()
    sys.exit(trackApp.exec_())