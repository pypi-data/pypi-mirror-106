# -*- coding: utf-8 -*-

##import sys
##import os
import queue
##import threading
##import time
##
##from datetime import datetime,timezone
##
##from PyQt5 import QtCore
##from PyQt5.QtWidgets import QDialog
##from PyQt5.QtGui import QFont
##
##
##from spotii.define import *
##from spotii.communication.communication import CommunicationThread
##from spotii.on_off.on_off import OnOffThread
##from spotii.test_handler.test_chip_handler import TestChipHandlerThread
##

import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
print('current dir',currentdir)
print('parent dir', parentdir)
sys.path.insert(0, currentdir)

from define import *
from communication.communication import CommunicationThread
from on_off.on_off import OnOffThread
from test_handler.test_chip_handler import TestChipHandlerThread
##
##class NotifyThread(QtCore.QThread):
##    signal_to_Gui  = QtCore.pyqtSignal(object)
##    signal_to_Thread = QtCore.pyqtSignal(object)
##    signal_to_Window = QtCore.pyqtSignal(object)
##
##
##
##def expendingPolicy(widget):
##        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
##        sizePolicy.setHorizontalStretch(0)
##        sizePolicy.setVerticalStretch(0)
##        sizePolicy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())
##        widget.setSizePolicy(sizePolicy)
##
##def minPolicy(widget):
##        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
##        sizePolicy.setHorizontalStretch(0)
##        sizePolicy.setVerticalStretch(0)
##        sizePolicy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())
##        widget.setSizePolicy(sizePolicy)
##def preferPolicy(widget):
##        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
##        sizePolicy.setHorizontalStretch(0)
##        sizePolicy.setVerticalStretch(0)
##        sizePolicy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())
##        widget.setSizePolicy(sizePolicy)
##
##def minExpending(widget):
##        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
##        sizePolicy.setHorizontalStretch(0)
##        sizePolicy.setVerticalStretch(0)
##        sizePolicy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())
##        widget.setSizePolicy(sizePolicy)
##
##class MyToolButton(QtWidgets.QToolButton):
##    def __init__(self, parent, activeIcon, inactiveIcon):
##        super(MyToolButton,self).__init__(parent)
##        self.activeIcon=activeIcon
##        self.inactiveIcon=inactiveIcon
##    def enterEvent(self, event):
####        print("Mouse entered")
####        self.setStyleSheet("QToolButton{background-color: rgba(0,21,59,255);}")
##        icon = QtGui.QIcon()
##        icon.addPixmap(QtGui.QPixmap(self.activeIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
##        self.setIcon(icon)
##        self.repaint()
##        # emit your signal
##    def leaveEvent(self, event):
####        print("Mouse left")
####        self.setStyleSheet("QToolButton{background-color: transparent; border:0; color : white}")
##        if self.isChecked():
##            return
##        icon = QtGui.QIcon()
##        icon.addPixmap(QtGui.QPixmap(self.inactiveIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
##        self.setIcon(icon)
##        self.repaint()
##
##class UnpressedToolButton(QtWidgets.QToolButton):
##    def mousePressEvent(self, event):
##        pass
##
##class MyDialog(QDialog):
##    def __init__(self,parent = None):
##        super(MyDialog, self).__init__(parent)
##        try:
##            print("is modal?",self.isModal())
##            self.setModal(True)
##            print("Set modal", self.isModal())
##        except:
##            print("error in myDialog init")
##        #self.setGeometry(100,100,500,200)
##    def closeEvent(self,event):
##        print("Dialog closed")
####        quit_msg = "Are you sure you want to exit the dialog?"
####        reply = QtGui.QMessageBox.question(self, 'Message', 
####                        quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
####        if reply == QtGui.QMessageBox.Yes:
####            event.accept()
####        else:
####            event.ignore()
##
##    def grabMouse():
##        print("grabMouse")
##    
##    def eventFilter(self, source, event):
##
##        try:
##            
## 
##            if event.type() == QtCore.QEvent.FocusIn: #and source is self.ledit_corteA:
##                print("FocusIn")
##            elif event.type() == QtCore.QEvent.FocusOut:
##                print("FocusOut")
##            elif event.type() == QtCore.QEvent.GrabMouse:
##                print("GrabMouse")
##            elif event.type() == QtCore.QEvent.HoverEnter:
##                print("HoverEnter")
##            elif event.type() == QtCore.QEvent.HoverLeave:
##                print("HoverLeave")
##            elif event.type() == QtCore.QEvent.HoverMove:
##                print("HoverMove")
##            elif event.type() == QtCore.QEvent.MouseButtonRelease:
##                print("MouseButtonRelease")
##            elif event.type() == QtCore.QEvent.MouseTrackingChange:
##                print("MouseTrackingChange")
##            elif event.type() == QtCore.QEvent.MouseButtonPress: #and source is self.ledit_corteB:
##                print("MouseButtonPress")
##            elif event.type() == QtCore.QEvent.MouseMove:
##                print("MouseMove")
##            elif event.type() == QtCore.QEvent.CursorChange:
##                print("CursorChange")
##            elif event.type() == QtCore.QEvent.Enter:
##                print("Enter")
##            elif event.type() == QtCore.QEvent.Leave:
##                print("Leave")
##            elif event.type() == QtCore.QEvent.GraphicsSceneHoverMove:
##                print("GraphicsSceneHoverMove")
##            elif event.type() == QtCore.QEvent.GraphicsSceneMouseMove:
##                print("GraphicsSceneMouseMove")
##            elif event.type() == QtCore.QEvent.GraphicsSceneHoverEnter:
##                print("GraphicsSceneHoverEnter")
##            elif event.type() == QtCore.QEvent.WindowDeactivate:
##                print("WindowDeactivate")
##            elif event.type() == QtCore.QEvent.NonClientAreaMouseButtonPress:
##                print("NonClientAreaMouseButtonPress")
##            elif event.type() == QtCore.QEvent.NonClientAreaMouseMove:
##                print("NonClientAreaMouseMove")
##            else:
##                print("Other")
##        except:
##            print("error in eventFilter")
##        return super(MyDialog, self).eventFilter(source, event)
##        
##
##class MyLabel(QtWidgets.QLabel):
##    def eventFilter(self, source, event):
##
##        try:
##            print("in MyLabel")
##        except:
##            print("error in MyLabel eventFilter")
##        return super(MyLabel, self).eventFilter(source, event)
##        
##
##
##LOCAL_PNG_FOLDER = "guifolder/png/"
##PNG_FOLDER='' ## Will be initialized
##class Ui_Title():
##    def __init__(self, centralwidget, parentLayOut):
##        
##        #print('in ui_title', PNG_FOLDER)
##        self.backGround = MyLabel(centralwidget)
##        
##        self.backGround.setObjectName("BackGround")
##
##        self.backGround.setPixmap(QtGui.QPixmap(PNG_FOLDER+"title/rectangle.png"))
##        self.backGround.setScaledContents(True)
###        minPolicy(self.backGround)
##
##
###        self.backGround.installEventFilter(self.backGround)
##        
##        parentLayOut.addWidget(self.backGround)
##
##        hLayout = QtWidgets.QHBoxLayout(self.backGround)
##        hLayout.setObjectName("titleLayout")
##        hLayout.setSpacing(10)
##        hLayout.setContentsMargins(0, 0, 10, 0)
##        
##        self.iconButton(self.backGround,hLayout, "Logo", 135, 27, PNG_FOLDER+"title/logo.png", PNG_FOLDER+"title/logo.png")
##
##        hLayout.addStretch(1)
##        self.iconButton(self.backGround,hLayout, "Help", 24, 18,
##                        PNG_FOLDER+"title/spot-icons-help-active.png",
##                        PNG_FOLDER+"title/spot-icons-help-inactive.png",
##                        self.clickHook)
##        
##        self.iconButton(self.backGround,hLayout, "Bluetooth", 24, 18,
##                        PNG_FOLDER+"title/spot-icons-bluetooth-active.png",
##                        PNG_FOLDER+"title/spot-icons-bluetooth-inactive.png",
##                        self.clickHook)
##        
##        self.iconButton(self.backGround,hLayout, "Wifi", 24, 18,
##                        PNG_FOLDER+"title/spot-icons-wifi-active.png",
##                        PNG_FOLDER+"title/spot-icons-wifi-inactive.png",
##                        self.clickHook)
##        
##        self.iconButton(self.backGround,hLayout, "Sound", 24, 18,
##                        PNG_FOLDER+"title/spot-icons-sound-active.png",
##                        PNG_FOLDER+"title/spot-icons-sound-inactive.png",
##                        self.clickHook)
##        
##        self.iconButton(self.backGround,hLayout, "Calendar", 24, 18,
##                        PNG_FOLDER+"title/spot-icons-calendar-active.png",
##                        PNG_FOLDER+"title/spot-icons-calendar-inactive.png",
##                        self.clickHook)
##        
##        self.iconButton(self.backGround,hLayout, "Setting", 24, 18,
##                        PNG_FOLDER+"title/spot-icons-settings-inactive.png",
##                        PNG_FOLDER+"title/spot-icons-settings-inactive.png",
##                        self.settingClickHook)
##        
##    def iconButton(self, parent, layout, name, width, height, pixMap ,pixMapInactive, hook=None):
###        toolButton = QtWidgets.QToolButton(parent)
##        if( hook == None):
##            toolButton = UnpressedToolButton(parent)
##        else:
##            toolButton = MyToolButton(parent,pixMap,pixMapInactive)
##            toolButton.clicked.connect(hook)
##            toolButton.setCheckable(True)
##        toolButton.setAutoFillBackground(True)
##        icon = QtGui.QIcon()
##        icon.addPixmap(QtGui.QPixmap(pixMapInactive), QtGui.QIcon.Normal, QtGui.QIcon.Off)
##        toolButton.setIcon(icon)
##        toolButton.setIconSize(QtCore.QSize(width, height))
###        toolButton.repaint()
##        toolButton.setObjectName(name)
##        toolButton.setStyleSheet("QToolButton{background-color: transparent; border:0; color : white}");
##        toolButton.setAutoRaise(True)
##
##        
##        layout.addWidget(toolButton)
##
####    def clickHook(self):
####        print("in clickHook")
##        
##    def clickHook(self):
###        dlg = MyDialog(self.backGround)
##        dlg = MyDialog()
##        dlg.setWindowTitle("HELLO!")
##        dlg.installEventFilter(dlg)
##        dlg.exec_()
##
##    def settingClickHook(self):
##        print('will quit')
##        QtWidgets.qApp.quit()
##
##class Ui_Slot():    
##    def __init__(self, centralwidget, parentLayOut, slot):
##        #print('in ui_slot', PNG_FOLDER)
##        self.stackedLayout_slot = QtWidgets.QStackedLayout()
##        self.stackedLayout_slot.setObjectName("stackedLayout_slot")
##        
##        self.slotItem(centralwidget, self.stackedLayout_slot, "Empty",       PNG_FOLDER+"slot/spot-slot-empty.png")
##        self.slotItem(centralwidget, self.stackedLayout_slot, "Detecting",   PNG_FOLDER+"slot/detecting/detecting "+str(slot)+".png")
##        self.slotItem(centralwidget, self.stackedLayout_slot, "Warning",     PNG_FOLDER+"slot/warning/warning - "+str(slot)+".png")
##        self.slotItem(centralwidget, self.stackedLayout_slot, "Positive",    PNG_FOLDER+"slot/positive/detecting - positive "+str(slot)+".png")
##        self.slotItem(centralwidget, self.stackedLayout_slot, "Negative",    PNG_FOLDER+"slot/negative/negative - "+str(slot)+".png")
##        self.slotItem(centralwidget, self.stackedLayout_slot, "Invalid",     PNG_FOLDER+"slot/invalid/invalid - "+str(slot)+".png")
##                        
##        parentLayOut.addLayout(self.stackedLayout_slot)
###        self.sdfsfsdfs.start(1000)
##        self.cassetteId=""
##        self.timeLeft = TIMER_DURATION
##        self.myTimer = QtCore.QTimer()
##        self.myTimer.timeout.connect(self.timer_timeout)
##        
##    def textButton(self, parent, layout,name, font=None):
##        if font == None:
##            font = QtGui.QFont()
##            font.setPointSize(10)
##            font.setBold(True)
##        button = QtWidgets.QPushButton(parent)
##        button.setFont(font)
##        button.setObjectName(name)
##        button.setStyleSheet("QPushButton{background-color: transparent; border:0; color : white}");
##        button.setFocusPolicy(QtCore.Qt.NoFocus)
##        layout.addWidget(button)
##
##    def slotItem(self, centralwidget, parent, name, pixMap):
##        label = QtWidgets.QLabel(centralwidget)
##        label.setObjectName(name)
###        label.setStyleSheet(".QLabel{border-image:url("+pixMap+");}")
##        label.setPixmap(QtGui.QPixmap(pixMap))
##        label.setScaledContents(True)
###        expendingPolicy(label)
##        
##        vLayout = QtWidgets.QVBoxLayout(label)
##        vLayout.setObjectName("slotLayout")
##        vLayout.setSpacing(51)
##        vLayout.setContentsMargins(0, 133, 0, 0)
##        
##        self.textButton(label,vLayout, "Button Time")
##        self.textButton(label,vLayout, "Button Text")                    
##        parent.addWidget(label)
##       
##    def setStatus(self, status_index, cassette, time=None):
##        
##        self.cassetteId=cassette
##        self.stackedLayout_slot.setCurrentIndex(status_index)
##        item=self.stackedLayout_slot.currentWidget()
##        item.layout().itemAt(1).widget().setText(self.cassetteId) ## 1 for cassette ID
##        if(time!=None):
##            item.layout().itemAt(0).widget().setText(time) ## 0 for counting down timer
##        else:
##            self.myTimer.stop()
##
##    def detecting(self, cassette):
##        
##        self.cassetteId=cassette
##        self.timeLeft = TIMER_DURATION
##        self.myTimer.start(1000)
###         try:
###             self.sdfsfsdfs.start(1000)
###         except:
###             print("error--testing")
##        self.showDetecting()
##
##    def timer_timeout(self):
##        self.timeLeft -= 1
###        print(" in timer_timeout()")
##        self.showDetecting()        
##        if self.timeLeft == 0:
##            self.detection_timeout()
##            self.myTimer.stop()
##        
##    def showDetecting(self):
##        self.setStatus(SLOT_STATUS_DETECTING, self.cassetteId, time.strftime('%M:%S', time.gmtime(self.timeLeft)))
##            
##    def detection_timeout(self):
##        self.setStatus(SLOT_STATUS_WARNING, self.cassetteId)        
## 
##class Ui_MainWindow(object):
##    def setupUi(self, MainWindow):
##        MainWindow.setObjectName("MainWindow")
##        MainWindow.resize(480, 272)
##        self.centralwidget = QtWidgets.QWidget(MainWindow)
##        self.centralwidget.setObjectName("centralwidget")
##        MainWindow.setCentralWidget(self.centralwidget)
##        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
##        self.gridLayout.setObjectName("gridLayout")
##        
##        self.gridLayout.setContentsMargins(0, 0, 0, 0)####        
##
##        self.verticalLayout_main = QtWidgets.QVBoxLayout()
##        self.verticalLayout_main.setObjectName("verticalLayout_main")
##        self.verticalLayout_main.setSpacing(0)
##        self.gridLayout.addLayout(self.verticalLayout_main, 0, 0, 1, 1)
##
##        self.horizontalLayout_title = QtWidgets.QHBoxLayout()
##        self.horizontalLayout_title.setObjectName("horizontalLayout_title")
##        self.horizontalLayout_slots = QtWidgets.QHBoxLayout()
##        self.horizontalLayout_slots.setObjectName("horizontalLayout_slots")
##        self.horizontalLayout_slots.setSpacing(0)
##        self.verticalLayout_main.addLayout(self.horizontalLayout_title)
##        self.verticalLayout_main.addLayout(self.horizontalLayout_slots)
##        
##        self.title=Ui_Title(self.centralwidget, self.horizontalLayout_title)
##        self.slot=[]
##        for i in range(5):
##            self.slot.append(Ui_Slot(self.centralwidget, self.horizontalLayout_slots, i+1))
###         self.slot_1=Ui_Slot(self.centralwidget, self.horizontalLayout_slots, 1)
###         self.slot_2=Ui_Slot(self.centralwidget, self.horizontalLayout_slots, 2)
###         self.slot_3=Ui_Slot(self.centralwidget, self.horizontalLayout_slots, 3)
###         self.slot_4=Ui_Slot(self.centralwidget, self.horizontalLayout_slots, 4)
###         self.slot_5=Ui_Slot(self.centralwidget, self.horizontalLayout_slots, 5)
###        self.showState(1,"hello")
##
##        
##        self.retranslateUi(MainWindow)
##        QtCore.QMetaObject.connectSlotsByName(MainWindow)
##
##        self.detecting=False;
##    def showState(self, status_index,item): # for testing and debugging purpose
##        for i in range(5):
##            self.slot[i].setStatus(status_index,item)
##            
###         self.slot_1.setIndex(index,item)
###         self.slot_2.setIndex(index,item)
###         self.slot_3.setIndex(index,item)
###         self.slot_4.setIndex(index,item)
###         self.slot_5.setIndex(index,item)
##
##    def retranslateUi(self, MainWindow):
##        _translate = QtCore.QCoreApplication.translate
##        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
##
##    def setQue(self,queue):
##        self.queMonitor=EmitThread(queue)
##        self.queMonitor.signal.connect(self.emitHook)
##        self.queMonitor.start()
##        
##
##    def emitHook(self,item):
##        print(time.strftime('%Y%m%d%H%M%S'),"emitHook:",item)
##        slotNo  = item[0]
##        errCode = item[1]
##        qrCode  = item[2]
##        
##        if slotNo == NON_SLOT_INDEX:
##            for i in range(TOTAL_SLOTS):
##                self.slot[i].setStatus(SLOT_STATUS_WARNING, qrCode)
##            
##        elif errCode == DEVICE_STATE_TAKING_PHOTO:
##            self.slot[item[0]].detecting(qrCode)
##        elif errCode == Positive_test_result:
##            self.slot[item[0]].setStatus(SLOT_STATUS_POSITIVE, qrCode)
##        elif errCode == Negative_test_result:
##            self.slot[item[0]].setStatus(SLOT_STATUS_NEGATIVE, qrCode)
##        elif errCode == Invalid_image_identifier:
##            self.slot[item[0]].setStatus(SLOT_STATUS_INVALID, qrCode)
##        elif errCode == DEVICE_STATE_CASSETTE_EMPTY:
##            self.slot[item[0]].setStatus(SLOT_STATUS_EMPTY, qrCode)
##        else:
##            self.slot[item[0]].setStatus(SLOT_STATUS_WARNING, qrCode)
##            
##        
###         self.slot_1.setIndex(1,"La0000107",item) #show index 1 label and cassette ID is "La0000107", with counting down timer on slot 1
###         if not self.detecting:
###             print("set slot 2 detecting")
###             self.slot_2.detecting("La0000100")
###             self.detecting=True
### ##        self.slot_2.setIndex(2,"La0000107")
###         self.slot_3.setIndex(3,"La0000107",item)
###         self.slot_4.setIndex(4,"La0000107")
###         self.slot_5.setIndex(5,"La0000107",item)
##        
##
##TEST_DURATION = 0
##class PeriodQueThread (threading.Thread):
##    def __init__(self, queue, interval):
##        threading.Thread.__init__(self)
##        self.queue=queue
##        self.interval = interval
##    def run (self):
##        duration=0
##        while True:
##            self.queue.put(time.strftime("%H:%M:%S"))
##            time.sleep(self.interval)
##            duration +=1
##            if duration == TEST_DURATION:
##                break;
##
##
##
##class MyMainWindow(QtWidgets.QMainWindow):
##    def __init__(self,notifyThread):
##        super(MyMainWindow, self).__init__()
##        self.notify=notifyThread
##        self.notify.signal_to_Window.connect(self.windowSignalHook)
##
##    def windowSignalHook(self, item):
##        print(item)
##        if item ==CLOSE_NOW:
##            self.close()
##    
##    def closeEvent(self,event):
##        print("main window is closing")
##        self.notify.signal_to_Thread.emit(CLOSE_NOW)
##        #self.emitThread.join()
##        print("everthing done")
##
##def gui(qForGui):
##    notifyThread=NotifyThread()
##    app = QtWidgets.QApplication(sys.argv)
##    MainWindow = MyMainWindow(notifyThread)
##    flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
##    MainWindow.setWindowFlags(flags)
##    ui = Ui_MainWindow()
##    ui.setupUi(MainWindow)
##    ui.setQue(qForGui)
##    MainWindow.show()
##    return app.exec_()
##    
##
###LAUNCHER_FOLDER = '/home/pi/app/spotii/launcher'
##
##def spot_main():
###     print("__file__:",__file__)
###     
##    
##    preStart()
##    qForGui=queue.Queue()
##    qForCom=queue.Queue()
##    qForResult=queue.Queue()
##    Comm       =CommunicationThread(2,"Comm",qForCom, qForResult)
##    TestMonitor=TestChipHandlerThread(3,"TCH",qForCom, qForGui, qForResult)
##    OnOff      =OnOffThread(4,"OnOff")
##
##    Comm.start()
##    OnOff.start()
##    TestMonitor.start()
##    guiRtn=gui(qForGui)
##    
##    print("App end.")
##    qForResult.put(CLOSE_NOW)
##    qForCom.put(CLOSE_NOW)
##    TestMonitor.join()
##    sys.exit(guiRtn)
###     GUI.join()
###     Comm.join()
###     OnOff.join()
###     TestMonitor.join()
##
##if __name__ == "__main__":
##    spot_main()

LOCAL_LAUCHER_FOLDER = '/home/pi/app/spotii/launcher'
LOCAL_LAUCHER_CHK_FILE = LOCAL_LAUCHER_FOLDER+'/chk_sum.md5'
DESK_TOP = '/home/pi/Desktop'
def preStart():
    try:
        import shutil
        #global PNG_FOLDER
        
        os.makedirs(LOCAL_LAUCHER_FOLDER, exist_ok =True)
        os.makedirs(IMG_PATH, exist_ok =True)
        
        lib_path = os.path.dirname(__file__)
        
        
        print('main directory:', lib_path)
        if lib_path == '':
            
            #PNG_FOLDER = os.getcwd()+'/'+LOCAL_PNG_FOLDER
            pass
        else:
            #PNG_FOLDER = lib_path+'/'+LOCAL_PNG_FOLDER
            upgrade_launcher = False
            if os.path.exists(LOCAL_LAUCHER_CHK_FILE):
                with open(lib_path+'/launcher/'+'chk_sum.md5',"rb") as lib_file:
                    lib_check_sum=lib_file.read()
                    print('lib check sum ',lib_check_sum)
                with open(LOCAL_LAUCHER_CHK_FILE,"rb") as local_file:
                    local_check_sum=local_file.read()
                    print('local check sum ',local_check_sum)
                if lib_check_sum != local_check_sum:
                    upgrade_launcher = True
            else:
                upgrade_launcher = True
                
            if upgrade_launcher:
                print('upgrading launcher..')
                src=os.path.join(lib_path,'launcher')
                for item in os.listdir(src):
                    #print(item)
                    if item.endswith('.sh'):
                        print('Copying to deskTop', item)
                        shutil.copy(os.path.join(src, item), os.path.join(DESK_TOP, item))
                    elif item.endswith('.py') or item.endswith('.md5'):
                        print('Copying to local laucher folder',item)
                        shutil.copy(os.path.join(src, item), os.path.join(LOCAL_LAUCHER_FOLDER, item))
    except Exception as e:
        print(e)

    
    #print('png folder: ',PNG_FOLDER)


import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from guifolder.gui import MainWindow
    
def spot_main():
    preStart()
    qForGui=queue.Queue()
    qForCom=queue.Queue()
    qForResult=queue.Queue()
    
    Comm       =CommunicationThread(2,"Comm",qForCom, qForResult)
    TestMonitor=TestChipHandlerThread(3,"TCH",qForCom, qForGui, qForResult)
    OnOff      =OnOffThread(4,"OnOff")

    Comm.start()
    OnOff.start()
    TestMonitor.start()

    app = QtWidgets.QApplication(sys.argv)
    window=MainWindow(qForGui = qForGui)
    
    rtn= app.exec_()
    print('main app return', rtn)
    print("App end.")
    qForResult.put(CLOSE_NOW)
    qForCom.put(CLOSE_NOW)
    TestMonitor.join()
#     GUI.join()
#     Comm.join()
#     OnOff.join()
#     TestMonitor.join()
    sys.exit(rtn)
    
if __name__ == "__main__":
    
    spot_main()
