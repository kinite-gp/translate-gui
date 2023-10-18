# Form implementation generated from reading ui file 'pyqt6.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from threading import Thread
from googletrans import Translator,constants
from time import sleep
from webbrowser import open
import requests

langs = constants.LANGUAGES
font_size = 25

def status():
    try:
        if requests.get('https://translate.google.com').ok:
            return True
    except:
        return False
    
def github():
    open('https://github.com/kinite-gp/translate-gui')

class Ui_mainWindow(object):
    def translator(self, mainWindow):
            try:
                if status():
                    self.label_3.setText("Connect!")
                elif not status():
                    self.label_3.setText("Disconnect!")
                else:
                    self.label_3.setText("Checking......")
                    
                translate_lang = self.comboBox_2.currentText()
                code_lang = list(langs.keys())[list(langs.values()).index(translate_lang)]
                
                text = self.textEdit.toPlainText()
                
                engine = Translator()
                translate_text_obj = engine.translate(text,dest=code_lang)
                translate_text = str(translate_text_obj.text)
                
                self.textEdit_2.setPlainText(translate_text)
            except Exception as e:
                print(e)
                self.label_3.setText("Erorr!")
                
                
                
    
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        mainWindow.setMinimumSize(QtCore.QSize(800, 600))
        mainWindow.setMaximumSize(QtCore.QSize(800, 600))
        mainWindow.setAutoFillBackground(False)
        mainWindow.setAnimated(False)
        mainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.centralwidget = QtWidgets.QWidget(parent=mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(400, 130, 391, 401))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("")
        self.textEdit.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.textEdit.setDocumentTitle("")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet(
        f"""
font-size: {font_size}px;
        """
        )
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 130, 391, 401))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setStyleSheet(
        f"""
font-size: {font_size}px;
        """
        )
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 781, 61))
        font = QtGui.QFont()
        font.setPointSize(29)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 550, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 550, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(46, 164, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.clicked.connect(github)
        self.pushButton.setGeometry(QtCore.QRect(620, 550, 171, 31))
        self.pushButton.setIconSize(QtCore.QSize(15, 13))
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(50, 90, 311, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.clicked.connect(self.translator)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 550, 171, 31))
        self.pushButton_2.setIconSize(QtCore.QSize(15, 13))
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Google Translate"))
        
        self.label.setText("translate google")
        self.label_2.setText("status: ")
        self.label_3.setText("Checking......")
        self.pushButton.setText("Github")
        self.pushButton_2.setText("translate!")
           
        for language in langs:
            self.comboBox_2.addItem(constants.LANGUAGES[language])
            
        self.comboBox_2.setCurrentText("english")
           


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())
        

