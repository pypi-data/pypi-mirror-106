import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import pathlib
import queue
import time

import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from guifolder import title_rc
from define import *
##if __name__ == "__main__":
##    import title_rc
##    #import MyToolButton
##else:
##    import guifolder.title_rc
##    #import MyToolButton

currentPath=pathlib.Path(__file__).parent.absolute()

pngName = ['','detecting ','warning - ','positive ','negative - ','invalid - '] #won't use first element, just keep index same as page index

class Ui_Slot():    
    def __init__(self, slot):
        try:
            self.slot=slot
            self.cassetteId=""
            self.timeLeft = TIMER_DURATION
            self.myTimer = QtCore.QTimer()
            self.myTimer.timeout.connect(self.timer_timeout)
        except Exception as error:
            print (error)

    def setStatus(self, status_index, cassette, time=None):
        try:
            self.cassetteId=cassette
            self.slot.setCurrentIndex(status_index)
            page=self.slot.currentWidget()
            tags=page.findChildren(QtWidgets.QPushButton)
    
            if len(tags)!=0:
                tags[0].setText(self.cassetteId) ## 0 for cassette ID
                
                
            if(time!=None):
                if len(tags)>1:
                    tags[1].setText(time) ## 1 for counting down timer
            else:
                self.myTimer.stop()
        except Exception as e:
            print (e)

    def detecting(self, cassette):
        try:
            self.cassetteId=cassette
            self.timeLeft = TIMER_DURATION
            self.myTimer.start(1000)
            self.showDetecting()
        except Exception as e:
            print(e)

    def timer_timeout(self):
        try:
            self.timeLeft -= 1
            self.showDetecting()        
            if self.timeLeft == 0:
                self.detection_timeout()
                self.myTimer.stop()
        except Exception as e:
            print(e)
        
    def showDetecting(self):
        try:
            self.setStatus(SLOT_STATUS_DETECTING, self.cassetteId, time.strftime('%M:%S', time.gmtime(self.timeLeft)))
        except Exception as e:
            print(e)
    def detection_timeout(self):
        try:
            self.setStatus(SLOT_STATUS_WARNING, self.cassetteId)
        except Exception as e:
            print(e)

class EmitThread(QtCore.QThread):
    signal= QtCore.pyqtSignal(object)
    def __init__(self, sharedQue):
        QtCore.QThread.__init__(self)
        self.qForGui=sharedQue
    def run(self):
        print("Start emit thread")
        while True:
            try:
                qItem=self.qForGui.get()
                print('in gui', qItem)
                self.signal.emit(qItem)
                self.qForGui.task_done()
            except Exception as e:
                 print(e)


        
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None, qForGui=None):
        super(MainWindow, self).__init__(parent)

        emitThread = EmitThread(qForGui)
        emitThread.signal.connect(self.emitHook)
        emitThread.start()
        

        self.page=0
        
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        loadUi(os.path.join(currentPath,'spotii.ui'),self)
        self.slots = []
        self.config()
        self.show()
    def config(self):
        try:
            slot_index = 1
            totalSlots = self.findChildren(QtWidgets.QStackedWidget)
            for slot in totalSlots:
                for page in range(1,6):
                    #print (page)
                    slot.setCurrentIndex(page)
                    style = '.QWidget{background-image:url(:/slot_' +str(slot_index)+ '/png/slot/slot_' +str(slot_index)+ '/' +pngName[page]+str(slot_index)+ '.png);border:0px}'
                    #print(style)
                    slot.currentWidget().setStyleSheet(style)
                slot.setCurrentIndex(0)
                slot_index+=1
                self.slots.append(Ui_Slot(slot))

            self.quit.clicked.connect(self.quitHook)
            self.help.clicked.connect(self.helpHook)
        except Exception as error:
            print(error)
            
    def quitHook(self):
        print('will quit')
        #QtWidgets.qApp.quit()
        self.close()


    def helpHook(self):
        print('will help')
        try:
            self.page= (self.page+1) %6
            for index in range(0,5):                
                self.slots[index].setStatus(self.page,'La0000002')
                #item=self.slots[index].currentWidget()
                #print(item.findChildren(QtWidgets.QPushButton))
        except Exception as e:
            print(e)

    def emitHook(self,item):
        try:
            print(time.strftime('%Y%m%d%H%M%S'),"emitHook:",item)
            slotNo  = item[0]
            errCode = item[1]
            qrCode  = item[2]
            
            if slotNo == NON_SLOT_INDEX:
                for i in range(TOTAL_SLOTS):
                    self.slots[i].setStatus(SLOT_STATUS_WARNING, qrCode)
                
            elif errCode == DEVICE_STATE_TAKING_PHOTO:
                self.slots[item[0]].detecting(qrCode)
            elif errCode == Positive_test_result:
                self.slots[item[0]].setStatus(SLOT_STATUS_POSITIVE, qrCode)
            elif errCode == Negative_test_result:
                self.slots[item[0]].setStatus(SLOT_STATUS_NEGATIVE, qrCode)
            elif errCode == Invalid_image_identifier:
                self.slots[item[0]].setStatus(SLOT_STATUS_INVALID, qrCode)
            elif errCode == DEVICE_STATE_CASSETTE_EMPTY:
                self.slots[item[0]].setStatus(SLOT_STATUS_EMPTY, qrCode)
            else:
                self.slots[item[0]].setStatus(SLOT_STATUS_WARNING, qrCode)
        except Exception as e:
            print(e)
        
    def closeEvent(self,event):
        print("Main window is closing")

if __name__ == "__main__":
    import sys
    qForGui=queue.Queue()
    app = QtWidgets.QApplication(sys.argv)
    window=MainWindow(qForGui = qForGui)
    rtn= app.exec_()
    print('main app return', rtn)
    sys.exit(rtn)
