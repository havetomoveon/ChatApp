from PySide6.QtCore import *
import PySide6.QtCore
import PySide6.QtGui
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PIL import Image
class TextArea(QTextEdit):
    def __init__(self,parent):
        super().__init__(parent)
        self.setMinimumSize(parent.width() /70  *100,parent.height() *1.5)
        self.setMaximumHeight(parent.height()*1.5)
        self.setStyleSheet("background-color:rgb(9,9,9);border:0px;border-radius:10px;color:white;padding-top:10px;padding-left:10px")

class SendButton(QLabel):
    def __init__(self,parent):
        super().__init__(parent)
        self.setScaledContents(True)
        self.setPixmap(QPixmap("telqt/s.png"))
        self.setMaximumSize(40,40)
        self.setMinimumSize(40,40)
class FileButton(QLabel):
    def __init__(self,parent):
        super().__init__(parent)
        self.setScaledContents(True)
        self.setPixmap(QPixmap("telqt/f.png"))
        self.setMaximumSize(40,40)
        self.setMinimumSize(40,40)
class messagearea(QHBoxLayout):
    def __init__(self,parent,flip = False):
        super().__init__()
        pho = QLabel(parent)
        pho.setMaximumSize(300,100)
        pho.setScaledContents(True)
        ph = QPixmap("telqt/messagearea.png")
        #pho.setStyleSheet("background-color:none;border:0px")
        if not flip:
            trans = QTransform()
            trans.scale(-1,1)
            ph = ph.transformed(trans)
        pho.setPixmap(ph)
        self.addWidget(pho)
        self.setContentsMargins(25,0,25,0)
class frame(QLabel):
    def __init__(self,parent:QFrame | QWidget):
        super().__init__(parent)
        self.setStyleSheet("background-color:none;border-bottom:0px solid rgb(35, 35, 35)")
        ph = QPixmap("telqt/profile.png")
        self.setScaledContents(True)
        self.setPixmap(ph)  
        self.setMaximumSize( 50, 50)
        self.setMinimumSize( 50,50)
class leftSideWidget(QFrame):
    def __init__(self,parent):
        super().__init__(parent)
        
        self.resize(200,parent.height())
        self.setMinimumSize(200,800)
        self.setMaximumWidth(300)
        #leftSide.setMaximumSize(400,1080)

class TextFrameLayout(QHBoxLayout):
    def __init__(self,parent):
        super().__init__()
        textarea = TextArea(parent)
        fileButton = FileButton(parent)
        sendButton = SendButton(parent)
        self.addWidget(textarea)
        self.addWidget(sendButton)
        self.addWidget(fileButton)
        self.setStretch(0,9)
        self.setStretch(1,1)
        self.setStretch(2,1)
class TopSideWidgetProfileContact(QFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.resize(10,10)
        self.setStyleSheet("background-color:rgb(9,9,9);border-radius:15px;")
        self.setFrameShape(QFrame.StyledPanel)
        self.setMinimumHeight(55)
        self.setMaximumHeight(55)
class RightSideWidgetLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()
class ui(QMainWindow):
    def __init__(self):
        super().__init__()
        central = QWidget(self)
        mainlayout = QHBoxLayout()
        rightsidewidget = QWidget(central)
        rightsidewidget.setStyleSheet("background-color:rgb(35, 35, 35);border-radius:20px")
        textFrame = QFrame(rightsidewidget)
        textFrame.setStyleSheet("background-color:rgb(35, 35, 35)")
        rightSideLayout = RightSideWidgetLayout()

        self.resize(1000,700)
        self.setStyleSheet("background-color:rgba(46, 0, 182, 0.4)")
        leftSide = leftSideWidget(central)
        #
        #leftSide.setStyleSheet("background-color:rgb(0, 4, 82)")
        grid = QGridLayout()
        grid.setVerticalSpacing(4)
        leftSide.setLayout(grid)
        grid.setContentsMargins(4,0,0,0)
        for i in range(10):
            contant = QFrame(leftSide)
            #contant.resize(200,100)
            ak = QGridLayout()
            yi = QTextBrowser(contant)
            ak.setColumnStretch
            yi.setStyleSheet("background-color: rgb(117, 19, 255)")
            yi.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            ak.addWidget(yi,0,1)
            rt = QTextBrowser(contant)
            rt.setStyleSheet("background-color: rgb(117, 19, 255)")
            rt.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            ak.addWidget(rt,1,1)
            contant.setStyleSheet("background-color:rgb(47, 0, 148);border-bottom:0px solid rgb(0, 31, 131);border-radius:10px")
            self.photo = frame(contant)
            contant.setMaximumHeight(100)
            #self.photo.setGeometry(10,contant.height() / 2,contant.width() * 50 / 100,contant.width() * 50 / 100)
            ak.addWidget(self.photo,0,0)
            contant.setLayout(ak)

            grid.addWidget(contant,i,1)
        #rightsidewidget.setGeometry(200,0,self.width()-200,self.height())
        #rightsidewidget.setMaximumSize(1920,1080)
        
        #textFrame.setGeometry(0,rightsidewidget.height() - 50,rightsidewidget.width(),50)
        lay = TextFrameLayout(textFrame)
        #lay.setSpacing(4)
        #lay.setContentsMargins(5,5,5,5)
        
        
        #lay.addLayout(we,Qt.AlignmentFlag.AlignLeft)
        textFrame.setLayout(lay)
        #########################
        messagesFrame = QFrame(rightsidewidget)
        messagesFrame.resize(rightsidewidget.width(),rightsidewidget.height() - 80)
        messagesFrame.setStyleSheet("background-color:rgb(35, 35, 35)")
        messagesList = QGridLayout()
        messagesList.setContentsMargins(0,0,0,0)
        messagesFrame.setLayout(messagesList)
        for i in range(0,8,4):
            messagesList.addWidget(frame(messagesFrame),i,0,Qt.AlignmentFlag.AlignLeft)
            messagesList.addLayout(messagearea(messagesFrame,True),i+1,0,Qt.AlignmentFlag.AlignLeft)
            messagesList.addWidget(frame(messagesFrame),i+2,1,Qt.AlignmentFlag.AlignRight)
            messagesList.addLayout(messagearea(messagesFrame),i+3,1,Qt.AlignmentFlag.AlignRight)
        mainlayout.addWidget(leftSide)
        mainlayout.addWidget(rightsidewidget)
        #central.setLayout(mainlayout)
        
        topSideWidgetProfileContact = QFrame(rightsidewidget)
        
        profiletopSideLayout = QHBoxLayout()
        la = QLabel(topSideWidgetProfileContact)
        la.setMaximumSize(40,40)
        la.setMinimumSize(40,40)
        la.setScaledContents(True)
        la.setPixmap(QPixmap("telqt/profile.png"))
        profiletopSideLayout.addWidget(la)
        topSideWidgetProfileContact.setLayout(profiletopSideLayout)
        rightSideLayout.addWidget(topSideWidgetProfileContact)
        rightSideLayout.addWidget(messagesFrame)
        rightSideLayout.addWidget(textFrame)
        rightSideLayout.setStretch(0,1)
        rightSideLayout.setStretch(1,9)
        rightSideLayout.setStretch(2,1)
        rightsidewidget.setLayout(rightSideLayout)
        leftSide.setMinimumWidth(400)
        central.setLayout(mainlayout)
        self.setCentralWidget(central)




        
        

    
if __name__ == "__main__":
    a = QApplication()
    m = ui()
    #m.resize(1500,300)
    m.show()
    a.exec()
