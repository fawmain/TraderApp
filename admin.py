# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_admin(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 600)
        self.title_label = QtWidgets.QLabel(Form)
        self.title_label.setGeometry(QtCore.QRect(200, 10, 451, 81))
        font = QtGui.QFont()
        font.setFamily("Gill Sans Ultra Bold Condensed")
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(70, 160, 291, 291))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(Form)
        self.listWidget_2.setGeometry(QtCore.QRect(530, 160, 291, 291))
        self.listWidget_2.setObjectName("listWidget_2")
        self.tip_label = QtWidgets.QLabel(Form)
        self.tip_label.setGeometry(QtCore.QRect(250, 460, 361, 16))
        self.tip_label.setObjectName("tip_label")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 120, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Gill Sans Ultra Bold Condensed")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(550, 120, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Gill Sans Ultra Bold Condensed")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title_label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">ADMIN PANEL</span></p></body></html>"))
        self.tip_label.setText(_translate("Form", "(Onayladığınız Urun/Kullanıcı hareketleri için tıklamanız yeterli)"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">BEKLEYEN SATMALAR </span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">BEKLEYEN SATIN ALMALAR </span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_admin()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
