# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choice_place_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog3(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 480, 360))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_7.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_3")
        self.horizontalLayout_8.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button.setObjectName("button")
        self.verticalLayout.addWidget(self.button)

        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.btn_2_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_2_2.setObjectName("btn_2_2")
        self.verticalLayout.addWidget(self.btn_2_2)
        self.btn_2_1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_2_1.setObjectName("btn_2_1")
        self.verticalLayout.addWidget(self.btn_2_1)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("btn")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn.setObjectName("btn")
        self.verticalLayout.addWidget(self.btn)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "???????????????? ??????????????????"))
        self.label_8.setText(_translate("Dialog", "?????????? ???? ????????"))
        self.label_9.setText(_translate("Dialog", "?????????? ???? ??????????????"))
        self.btn_2_2.setText(_translate("Dialog", "????????????????????"))
        self.btn_2_1.setText(_translate("Dialog", "?????????????? ?????????? ??????????"))
        self.btn.setText(_translate("Dialog", "??????????"))
        self.pushButton_3.setText(_translate("Dialog", "????????????????"))
        self.button.setText(_translate("Dialog", "??????????"))
