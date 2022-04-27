import sys
import pyttsx3
from gtts import gTTS, gTTSError
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class window(QWidget):
    def __init__(self, parent = None):
        super(window, self).__init__(parent)
        self.setGeometry(250, 250, 750, 550)
        self.setFixedSize(self.size())
        self.setWindowTitle("RECORD FILE")
        self.setStyleSheet(
            'background: lightgray;\n'
        )

        self.textField = QTextEdit(self)
        self.textField.setGeometry(15, 80, 650, 440)
        self.textField.setStyleSheet(
            'border-radius: 10px;\n'
            'background: white;\n'
            'font-size: 15px;\n'
            'font-weight: bold;\n'
        )

        self.namefile = QTextEdit(self)
        self.namefile.setGeometry(20, 35, 370, 30)
        self.namefile.setStyleSheet(
            'background: white;\n'
            'border-radius: 10px;\n'
            'font-size: 15px;\n'
            'font-weight: bold;\n'
        )

        self.back = QPushButton(self)
        self.back.setIcon(QIcon(QPixmap('backspace.png')))
        self.back.setGeometry(395, 34, 35, 35)
        self.back.setStyleSheet(
            'border-radius: 10px;\n'
            'background: lightgray;\n'
        )
        self.back.clicked.connect(self.clearNameField)

        self.infoLab = QLabel(self)
        self.infoLab.setGeometry(480, 20, 250, 50)
        self.infoLab.setStyleSheet(
            'background: gray;\n'
            'border-radius: 10px;\n'
            'font-size: 20px;\n'
            'font-weight: bold;\n'
        )
        self.infoLab.setText('      RECORDER FILE')

        self.labelBut = QLabel(self)
        self.labelBut.setGeometry(678, 80, 50, 440)
        self.labelBut.setStyleSheet(
            'background: #C0C0C0;\n'
            'border-radius: 10px;\n'
        )

        self.rec = QPushButton(self.labelBut)
        self.rec.setIcon(QIcon(QPixmap('rec.png')))
        self.rec.setGeometry(7, 107, 35, 35)
        self.rec.setStyleSheet(
            'border-radius: 10px;\n'
            'background: gray;\n'
        )
        self.rec.clicked.connect(self.recoreder)

        self.clear = QPushButton(self.labelBut)
        self.clear.setIcon(QIcon(QPixmap('archeology.png')))
        self.clear.setGeometry(7, 157, 35, 35)
        self.clear.setStyleSheet(
            'border-radius: 10px;\n'
            'background: gray;\n'
        )
        self.clear.clicked.connect(self.clearField)

        self.speakMP = QPushButton(self.labelBut)
        self.speakMP.setIcon(QIcon(QPixmap('speaker.png')))
        self.speakMP.setGeometry(7, 207, 35, 35)
        self.speakMP.setStyleSheet(
            'border-radius: 10px;\n'
            'background: gray;\n'
        )
        self.speakMP.clicked.connect(self.speak)
    # Clear field text input
    def clearField(self):
        self.textField.clear()
        self.infoLab.clear()
        self.infoLab.setText('\tCLEAR')
    # Clear name field
    def clearNameField(self):
        self.namefile.clear()
    # Func speaker
    def speak(self):
        self.infoLab.clear()
        self.infoLab.setText('\tSPEAK')
        text = self.textField.toPlainText()
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    # Recorder in mp3
    def recoreder(self):
        name = self.namefile.toPlainText()
        text = self.textField.toPlainText()
        if len(name) < 1 and text == ' ':
            self.infoLab.clear()
            self.infoLab.setText('NO NAME FILE')
        else:
            text = self.textField.toPlainText()
            record = gTTS(text=text, lang='ru')
            record.save(name + '.mp3')
            self.namefile.clear()
            self.infoLab.clear()
            self.infoLab.setText('       FILE WRITTEN')


def main():
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()