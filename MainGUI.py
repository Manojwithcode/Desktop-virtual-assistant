


from jarvisUI import Ui_mainUI
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTime, QTimer, QDate
from PyQt5.uic import loadUiType
import mainjarvis
import os
import sys
import webbrowser as web

class MainThread(QThread):


    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        mainjarvis.task_GUI()

startExe = MainThread()

class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()

        self.Gui = Ui_mainUI()
        self.Gui.setupUi(self)

        self.Gui.start_push.clicked.connect(self.startTask)
        self.Gui.close_push.clicked.connect(self.close)
        self.Gui.chrome_push.clicked.connect(self.chrome_app)
        self.Gui.whatsapp_push.clicked.connect(self.whatsapp_app)
        self.Gui.word_push.clicked.connect(self.word_app)
        self.Gui.yt_push.clicked.connect(self.yt_app)
        self.Gui.excel_push.clicked.connect(self.excel_app)
        self.Gui.power_push.clicked.connect(self.power_app)

    def chrome_app(self):
        os.startfile("C:\Program Files\Google\Chrome\Application")

    def yt_app(self):
        web.open("enter uil")

    def whatsapp_app(self):
        web.open("enter uil")

    def note_app(self):
        os.startfile("C:\Windows\system32")

    def power_app(self):
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office")

    def excel_app(self):
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office")

    def word_app(self):
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office")

    def startTask(self):

        self.Gui.label1 =QtGui.QMovie("Iron_Template_1.gif")
        self.Gui.gif_1.setMovie(self.Gui.label1)
        self.Gui.label1.start()

        self.Gui.label2 =QtGui.QMovie("__1.gif")
        self.Gui.gif_2.setMovie(self.Gui.label2)
        self.Gui.label2.start()

       

        startExe.start()

        GuiApp = QApplication(sys)
        jarvis_gui = Gui_Start()
        jarvis_gui.show()
        exit(GuiApp.exec_())
