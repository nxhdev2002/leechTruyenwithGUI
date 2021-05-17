from PyQt5.QtGui import QMouseEvent, QCursor, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QPlainTextEdit, QLabel, QLineEdit
from PyQt5.QtCore import Qt, QRect, QMetaObject, QCoreApplication
from res import resource_rc, func

class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.background = QLabel(self)
        self.background.setGeometry(QRect(-10, 0, 791, 461))
        self.background.setStyleSheet("border-image: url(:/newPrefix/maxresdefault.jpg) 0 0 0 0 stretch stretch;")
        

        # input link 

        self.plainTextEdit = QPlainTextEdit(self)
        self.plainTextEdit.setGeometry(QRect(20, 70, 421, 301))
        self.plainTextEdit.setStyleSheet("border-radius: 5px; background-color: rgba(255, 99, 71, 0.6); font-size:16px")
        
        # thread number

        self.threadnum = QLineEdit(self)
        self.threadnum.setGeometry(QRect(480, 70, 221, 30))
        self.threadnum.setPlaceholderText("Số Thread")

        # Push Button Check Login Google
        self.loginGoogleButton = QPushButton(self)
        self.loginGoogleButton.setGeometry(QRect(480, 140, 221, 61))

        font = QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)

        self.loginGoogleButton.setFont(font)
        self.loginGoogleButton.setStyleSheet("QPushButton {border-radius: 10px;background-color: rgba(255, 99, 71, 0.9)} QPushButton::pressed {border-radius: 10px;background-color: rgba(255, 99, 71, 0.6)}")
        self.loginGoogleButton.setText("Login Google")
        self.loginGoogleButton.clicked.connect(lambda: self.loginGoogleButton_clicked())

        # Show info user

        self.labelInfoUser = QPushButton(self)
        self.labelInfoUser.setGeometry(QRect(480, 140, 221, 61))

        font = QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)

        self.labelInfoUser.setFont(font)
        self.labelInfoUser.setStyleSheet("QPushButton {border-radius: 10px;background-color: rgba(255, 99, 71, 0.9)}")
        self.labelInfoUser.setText("Test")
        self.labelInfoUser.setHidden(1)

        # Push Button Check Process
        font = QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.process_label = QPushButton(self)
        self.process_label.setGeometry(QRect(480, 220, 221, 51))
        self.process_label.setText("Click to view process")
        
        # Close
        self.xButton = QPushButton(self)
        self.xButton.setGeometry(QRect(720, 10, 21, 21))
        self.xButton.setStyleSheet("border-image: url(:/newPrefix/pngkey.com-red-x-png-3367399.png)")
        self.xButton.clicked.connect(lambda: QApplication.quit())


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos() - self.pos() #Get the position of the mouse relative to the window
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  #Change mouse icon
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#Change window position
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def loginGoogleButton_clicked(self):
        answer = func.validate(self, self.threadnum.text())
        # print(answer)
        if (answer is not False):
            self.labelInfoUser.setHidden(0)
            self.loginGoogleButton.setHidden(1)
            