# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ultronUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ultronUI(object):
    def setupUi(self, ultronUI):
        ultronUI.setObjectName("ultronUI")
        ultronUI.resize(801, 512)
        self.centralwidget = QtWidgets.QWidget(ultronUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 0, 811, 511))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../adarsh/7LP8.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 420, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 420, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 351, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../adarsh/T8bahf.gif"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(370, 10, 181, 31))
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border-radius:none;color:white;font-size:15;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(580, 10, 171, 31))
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"border-radius:none;color:white;font-size:15;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        ultronUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(ultronUI)
        QtCore.QMetaObject.connectSlotsByName(ultronUI)

    def retranslateUi(self, ultronUI):
        _translate = QtCore.QCoreApplication.translate
        ultronUI.setWindowTitle(_translate("ultronUI", "MainWindow"))
        self.pushButton.setText(_translate("ultronUI", "RUN"))
        self.pushButton_2.setText(_translate("ultronUI", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ultronUI = QtWidgets.QMainWindow()
    ui = Ui_ultronUI()
    ui.setupUi(ultronUI)
    ultronUI.show()
    sys.exit(app.exec_())
