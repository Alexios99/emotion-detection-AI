



import sys

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_main import Ui_MainWindow

from ui_dialog import Ui_Dialog

from ui_error import Ui_Error

from ui_function import *

from about import *
import capture_test



class dialogUi(QDialog):
    def __init__(self, parent=None):

        super(dialogUi, self).__init__(parent)
        self.d = Ui_Dialog()
        self.d.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

       
       
       
       
        self.d.bn_min.clicked.connect(lambda: self.showMinimized())

       
        self.d.bn_close.clicked.connect(lambda: self.close())

       
        self.d.bn_east.clicked.connect(lambda: self.close())
        self.d.bn_west.clicked.connect(lambda: self.close())
       

   
       
       
       
        self.dragPos = self.pos()  
        def movedialogWindow(event):
           
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

       
        self.d.frame_top.mouseMoveEvent = movedialogWindow 
       
   
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
   

   
   
   
   
   
    def dialogConstrict(self, heading, message, icon, btn1, btn2):
        self.d.lab_heading.setText(heading)
        self.d.lab_message.setText(message)
        self.d.bn_east.setText(btn2)
        self.d.bn_west.setText(btn1)
        pixmap = QtGui.QPixmap(icon)
        self.d.lab_icon.setPixmap(pixmap)
   



class errorUi(QDialog):
    def __init__(self, parent=None):

        super(errorUi, self).__init__(parent)
        self.e = Ui_Error()
        self.e.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

       
        self.e.bn_ok.clicked.connect(lambda: self.close())

        self.dragPos = self.pos()  
        def moveWindow(event):
           
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

       
        self.e.frame_top.mouseMoveEvent = moveWindow 
       
   
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

   
   
    def errorConstrict(self, heading, icon, btnOk):
        self.e.lab_heading.setText(heading)
        self.e.bn_ok.setText(btnOk)
        pixmap2 = QtGui.QPixmap(icon)
        self.e.lab_icon.setPixmap(pixmap2)




class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


       
        applicationName = "Emotion detection AI"
        self.setWindowTitle(applicationName)
       
       
        UIFunction.labelTitle(self, applicationName)
       
       


       
       
       
       
       
       
        UIFunction.initStackTab(self)
       

        
       
       
        UIFunction.constantFunction(self)
       


       
       
       
       
       
        self.ui.toodle.clicked.connect(lambda: UIFunction.toodleMenu(self, 160, True))
       


       
       
       
       
        self.ui.bn_home.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_home'))
        self.ui.bn_bug.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_bug'))
        #self.ui.bn_android.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_android'))
        #self.ui.bn_cloud.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_cloud'))
       


       
       
       
        UIFunction.stackPage(self)
       


       
       
       
        self.diag = dialogUi()
        self.error = errorUi()
       # self.ui.bn_bug_start.clicked.connect(capture_test.webcam())


        self.dragPos = self.pos()
        def moveWindow(event):
           
            if UIFunction.returStatus() == 1:
                UIFunction.maximize_restore(self)

           
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

       
        self.ui.frame_appname.mouseMoveEvent = moveWindow 
        
   
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
   


   
   
   
   
   
   
    def dialogexec(self, heading, message, icon, btn1, btn2):
        dialogUi.dialogConstrict(self.diag, heading, message, icon, btn1, btn2)
        self.diag.exec_()
   


   
   
    def errorexec(self, heading, icon, btnOk):
        errorUi.errorConstrict(self.error, heading, icon, btnOk)
        self.error.exec_()
   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
