# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passwordUi.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

"""
Todo List:
    Program doesn't like to make more than 8 programs. Goes unresponsive at 9+
        could fix by changing lineEdits to spinBoxes (give fixed options)
            this could also fix issue with incorrect data type being entered and error not showing up.

    Add functionality to menu actions and perhaps more menu items

    Perhaps add an input where passwords could be named (ie what they are for)
        could then be written to a file where they can be stored?


"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet(open("style.qss", "r").read())
        MainWindow.resize(951, 574)
        MainWindow.setWindowIcon(QtGui.QIcon('lock.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
    # Button to run main script
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 440, 271, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStatusTip("Create passwords!")
        self.pushButton.clicked.connect(self.generator) # connected button to main function
    # Text area for output of script
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(120, 320, 711, 71))
        self.textEdit.setObjectName("textEdit") #print area
        self.textEdit.setStatusTip("Passwords displayed here")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setMouseTracking(False)
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(17, 410, 921, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(340, 80, 271, 211))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit") #no of passwords
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2") #no of characters
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setObjectName("lineEdit_5") #need numbers?
        self.gridLayout.addWidget(self.lineEdit_5, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3") #need capital?
        self.gridLayout.addWidget(self.lineEdit_3, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4") #need symbols
        self.gridLayout.addWidget(self.lineEdit_4, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
    # Menubar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 951, 21))
        self.menubar.setObjectName("menubar")
        # File menu
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        # View Menu
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
    # Status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
    # Menu actions
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut('Ctrl+Q') # Added shortcut for exit
        self.actionExit.triggered.connect(QtWidgets.qApp.quit) # Added close action
        self.actionView_Statusbar = QtWidgets.QAction(MainWindow, checkable=True)
        self.actionView_Statusbar.setObjectName("actionView_Statusbar")
        self.actionView_Statusbar.setShortcut('Ctrl+S') # Added shortcut for hiding statusbar
        self.actionView_Statusbar.setChecked(True) # statusbars on state set to true
        self.actionView_Statusbar.triggered.connect(self.toggleMenu)

        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionView_Statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Generator"))
        self.pushButton.setText(_translate("MainWindow", "Generate Password/s"))
        self.label_5.setText(_translate("MainWindow", "Password Generator"))
        self.label.setText(_translate("MainWindow", "How many passwords do you need?"))
        self.label_2.setText(_translate("MainWindow", "How many characters does it need?"))
        self.label_6.setText(_translate("MainWindow", "Does it need any numbers (y or n)?"))
        self.label_3.setText(_translate("MainWindow", "Does it need a capital letter (y or n)?"))
        self.label_4.setText(_translate("MainWindow", "Does it need any symbols (y or n)?"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionView_Statusbar.setText(_translate("MainWindow", "View Statusbar"))

    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def generator(self, MainWindow):
        from random import randint
        import sys

        passwords = []

        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        numbers = '1234567890'

        symbols = '!+-.@ £$^&#*'

        i = 0

        num_of_passwords = int(self.lineEdit.text())

        length = int(self.lineEdit_2.text())

        number = str(self.lineEdit_5.text())
        while number != 'y' and number != 'n':
            self.textEdit.setText("you did not select 'y' or 'n' for number question!") # Need to change this to open a new window with error message. that can reset line edit contents.

        symbol = str(self.lineEdit_4.text())
        while symbol != 'y' and symbol != 'n':
            self.textEdit.setText("you did not select 'y' or 'n' for symbol question!") # Need to change this to open a new window with error message. that can reset line edit contents.

        case = str(self.lineEdit_3.text())
        while case != 'y' and case != 'n':
            self.textEdit.setText("you did not select 'y' or 'n' for capital question!") # Need to change this to open a new window with error message. that can reset line edit contents.

        for i in range(num_of_passwords):
            password = ''
            index = 0
            c_index = 0
            n_index = 0

            for character in range(length):
                password += alphabet[randint(0, 25)]

            new_password = list(password)

            if case == 'y':
                c_index = randint(0, length - 1)
                new_password[c_index] = new_password[c_index].upper()

            if number == 'y':
                n_index = randint(0, length - 1)
                while n_index == c_index:
                    index = randint(0, length - 1)
                del new_password[n_index]
                new_password.insert(n_index, numbers[randint(0, len(numbers) - 1)])

            if symbol == 'y':
                index = randint(0, length - 1)
                while index == c_index or index == n_index:
                    index = randint(0, length - 1)
                del new_password[index]
                new_password.insert(index, symbols[randint(0, len(symbols) - 1)])

            password = ''.join(new_password) #converting back to string

            passwords.append(password) #appending string to list

            i += 1 #loop increment, do not touch!

        new_passwords = "  ,  ".join(passwords)

        self.textEdit.setText(str(new_passwords)) # Output of passwords


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
