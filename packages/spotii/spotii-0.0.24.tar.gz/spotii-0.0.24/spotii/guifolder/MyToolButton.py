from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QFont

class MyToolButton(QtWidgets.QToolButton):
    def __init__(self, parent=None):
        super(MyToolButton,self).__init__(parent)
        self.activeIcon=None
        self.inactiveIcon=None
        self.setStyleSheet("QToolButton{background-color: transparent; border:0; color : white}")
        self.setAutoRaise(True)
        self.setAutoFillBackground(True)
    def setup(self,activeIcon,inactiveIcon):
        print('setting up...')
        self.activeIcon=activeIcon
        self.inactiveIcon=inactiveIcon
##        icon = QtGui.QIcon()
##        icon.addPixmap(self.inactiveIcon, QtGui.QIcon.Normal, QtGui.QIcon.Off)
##        self.setIcon(icon)
##        self.repaint()
##    def enterEvent(self, event):
##        print("Mouse entered")
##        self.setStyleSheet("QToolButton{background-color: rgba(0,21,59,255);}")
##        icon = QtGui.QIcon()
##        icon.addPixmap(self.activeIcon, QtGui.QIcon.Normal, QtGui.QIcon.Off)
##        self.setIcon(icon)
##        self.repaint()
##        # emit your signal
##    def leaveEvent(self, event):
##        print("Mouse left")
##        self.setStyleSheet("QToolButton{background-color: transparent; border:0; color : white}")
##        if self.isChecked():
##            return
##        icon = QtGui.QIcon()
##        icon.addPixmap(self.inactiveIcon, QtGui.QIcon.Normal, QtGui.QIcon.Off)
##        self.setIcon(icon)
##        self.repaint()
