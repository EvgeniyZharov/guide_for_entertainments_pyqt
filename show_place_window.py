# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show_place_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WindowThree(object):
    def setupUi(self, WindowThree):
        WindowThree.setObjectName("WindowThree")
        WindowThree.resize(500, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(WindowThree)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 235, 280))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)

        # self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        # self.label_2.setObjectName("label_2")
        # self.verticalLayout.addWidget(self.label_2)
        self.btn_3_1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_3_1.setObjectName("btn_3_1")
        self.verticalLayout.addWidget(self.btn_3_1)
        self.btn_3_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_3_2.setObjectName("btn_3_2")
        self.verticalLayout.addWidget(self.btn_3_2)
        self.btn_3_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_3_3.setObjectName("btn_3_3")
        self.verticalLayout.addWidget(self.btn_3_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(WindowThree)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(255, 10, 235, 200))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(WindowThree)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.retranslateUi(WindowThree)
        QtCore.QMetaObject.connectSlotsByName(WindowThree)

    def retranslateUi(self, WindowThree):
        _translate = QtCore.QCoreApplication.translate
        WindowThree.setWindowTitle(_translate("WindowThree", "Dialog"))
        self.label.setText(_translate("WindowThree", "Название заведения"))
        # self.label_2.setText(_translate("WindowThree", "Описание"))
        self.btn_3_1.setText(_translate("WindowThree", "Меню"))
        self.btn_3_2.setText(_translate("WindowThree", "События"))
        self.btn_3_3.setText(_translate("WindowThree", "Акции"))
        self.label_3.setText(_translate("WindowThree", "Отзывов: 0"))
        self.pushButton.setText(_translate("WindowThree", "Посмотреть отзывы"))
        self.pushButton_2.setText(_translate("WindowThree", "Назад"))
