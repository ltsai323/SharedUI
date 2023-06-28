# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1097, 705)
        self.pbSearch = QtWidgets.QPushButton(Form)
        self.pbSearch.setGeometry(QtCore.QRect(110, 300, 81, 41))
        self.pbSearch.setObjectName("pbSearch")
        self.pbClearParams = QtWidgets.QPushButton(Form)
        self.pbClearParams.setGeometry(QtCore.QRect(220, 310, 111, 21))
        self.pbClearParams.setObjectName("pbClearParams")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(40, 120, 381, 161))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ckUseDate = QtWidgets.QCheckBox(self.frame)
        self.ckUseDate.setEnabled(False)
        self.ckUseDate.setGeometry(QtCore.QRect(300, 120, 71, 21))
        self.ckUseDate.setObjectName("ckUseDate")
        self.cbChannelDensity = QtWidgets.QComboBox(self.frame)
        self.cbChannelDensity.setGeometry(QtCore.QRect(220, 80, 161, 21))
        self.cbChannelDensity.setObjectName("cbChannelDensity")
        self.cbChannelDensity.addItem("")
        self.cbChannelDensity.setItemText(0, "")
        self.cbChannelDensity.addItem("")
        self.cbChannelDensity.addItem("")
        self.cbInstitution = QtWidgets.QComboBox(self.frame)
        self.cbInstitution.setGeometry(QtCore.QRect(220, 0, 161, 21))
        self.cbInstitution.setObjectName("cbInstitution")
        self.cbInstitution.addItem("")
        self.cbInstitution.setItemText(0, "")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.dCreated = QtWidgets.QDateEdit(self.frame)
        self.dCreated.setEnabled(False)
        self.dCreated.setGeometry(QtCore.QRect(220, 120, 81, 21))
        self.dCreated.setCalendarPopup(True)
        self.dCreated.setDate(QtCore.QDate(2021, 1, 1))
        self.dCreated.setObjectName("dCreated")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_17.setGeometry(QtCore.QRect(0, 80, 221, 20))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_13.setGeometry(QtCore.QRect(0, 0, 221, 20))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_15.setGeometry(QtCore.QRect(0, 40, 221, 20))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_16.setGeometry(QtCore.QRect(0, 60, 221, 20))
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.cbAssmCol = QtWidgets.QComboBox(self.frame)
        self.cbAssmCol.setEnabled(False)
        self.cbAssmCol.setGeometry(QtCore.QRect(330, 140, 51, 21))
        self.cbAssmCol.setCurrentText("")
        self.cbAssmCol.setObjectName("cbAssmCol")
        self.cbAssmCol.addItem("")
        self.cbAssmCol.setItemText(0, "")
        self.cbAssmCol.addItem("")
        self.cbAssmCol.addItem("")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_18.setGeometry(QtCore.QRect(0, 120, 221, 20))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.cbPCBType = QtWidgets.QComboBox(self.frame)
        self.cbPCBType.setEnabled(False)
        self.cbPCBType.setGeometry(QtCore.QRect(220, 100, 161, 21))
        self.cbPCBType.setCurrentText("")
        self.cbPCBType.setObjectName("cbPCBType")
        self.cbPCBType.addItem("")
        self.cbPCBType.setItemText(0, "")
        self.cbPCBType.addItem("")
        self.cbPCBType.addItem("")
        self.cbPCBType.addItem("")
        self.cbPCBType.addItem("")
        self.cbPCBType.addItem("")
        self.cbPCBType.addItem("")
        self.cbPCBType.addItem("")
        self.cbShape = QtWidgets.QComboBox(self.frame)
        self.cbShape.setGeometry(QtCore.QRect(220, 20, 161, 20))
        self.cbShape.setObjectName("cbShape")
        self.cbShape.addItem("")
        self.cbShape.setItemText(0, "")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbAssmRow = QtWidgets.QComboBox(self.frame)
        self.cbAssmRow.setEnabled(False)
        self.cbAssmRow.setGeometry(QtCore.QRect(250, 140, 51, 21))
        self.cbAssmRow.setCurrentText("")
        self.cbAssmRow.setObjectName("cbAssmRow")
        self.cbAssmRow.addItem("")
        self.cbAssmRow.setItemText(0, "")
        self.cbAssmRow.addItem("")
        self.cbAssmRow.addItem("")
        self.cbAssmRow.addItem("")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_22.setEnabled(False)
        self.lineEdit_22.setGeometry(QtCore.QRect(300, 140, 31, 20))
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.cbThickness = QtWidgets.QComboBox(self.frame)
        self.cbThickness.setGeometry(QtCore.QRect(220, 60, 161, 21))
        self.cbThickness.setObjectName("cbThickness")
        self.cbThickness.addItem("")
        self.cbThickness.setItemText(0, "")
        self.cbThickness.addItem("")
        self.cbThickness.addItem("")
        self.cbThickness.addItem("")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_14.setGeometry(QtCore.QRect(0, 20, 221, 20))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_19.setGeometry(QtCore.QRect(0, 100, 221, 20))
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_20.setGeometry(QtCore.QRect(0, 140, 221, 20))
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_21.setEnabled(False)
        self.lineEdit_21.setGeometry(QtCore.QRect(220, 140, 31, 20))
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.cbMaterial = QtWidgets.QComboBox(self.frame)
        self.cbMaterial.setGeometry(QtCore.QRect(220, 40, 161, 21))
        self.cbMaterial.setObjectName("cbMaterial")
        self.cbMaterial.addItem("")
        self.cbMaterial.setItemText(0, "")
        self.cbMaterial.addItem("")
        self.cbMaterial.addItem("")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 40, 71, 16))
        self.label_7.setObjectName("label_7")
        self.cbPartType = QtWidgets.QComboBox(Form)
        self.cbPartType.setGeometry(QtCore.QRect(40, 60, 121, 21))
        self.cbPartType.setObjectName("cbPartType")
        self.cbPartType.addItem("")
        self.cbPartType.addItem("")
        self.cbPartType.addItem("")
        self.cbPartType.addItem("")
        self.cbPartType.addItem("")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 111, 16))
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(470, 50, 581, 281))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pbGoToPart = QtWidgets.QPushButton(self.frame_2)
        self.pbGoToPart.setGeometry(QtCore.QRect(120, 250, 171, 21))
        self.pbGoToPart.setObjectName("pbGoToPart")
        self.leStatus = QtWidgets.QLineEdit(self.frame_2)
        self.leStatus.setGeometry(QtCore.QRect(70, 220, 221, 20))
        self.leStatus.setText("")
        self.leStatus.setReadOnly(True)
        self.leStatus.setObjectName("leStatus")
        self.lwTypeList = QtWidgets.QListWidget(self.frame_2)
        self.lwTypeList.setGeometry(QtCore.QRect(290, 20, 281, 201))
        self.lwTypeList.setMidLineWidth(1)
        self.lwTypeList.setObjectName("lwTypeList")
        self.lwPartList = QtWidgets.QListWidget(self.frame_2)
        self.lwPartList.setGeometry(QtCore.QRect(10, 20, 281, 201))
        self.lwPartList.setMidLineWidth(1)
        self.lwPartList.setObjectName("lwPartList")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_26.setGeometry(QtCore.QRect(10, 220, 61, 20))
        self.lineEdit_26.setReadOnly(True)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.pbClearResults = QtWidgets.QPushButton(self.frame_2)
        self.pbClearResults.setGeometry(QtCore.QRect(10, 250, 101, 21))
        self.pbClearResults.setObjectName("pbClearResults")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 0, 191, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(300, 0, 191, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        self.cbChannelDensity.setCurrentIndex(0)
        self.cbInstitution.setCurrentIndex(0)
        self.cbAssmCol.setCurrentIndex(0)
        self.cbPCBType.setCurrentIndex(0)
        self.cbShape.setCurrentIndex(0)
        self.cbAssmRow.setCurrentIndex(0)
        self.cbThickness.setCurrentIndex(0)
        self.cbMaterial.setCurrentIndex(0)
        self.cbPartType.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pbSearch.setText(_translate("Form", "Search"))
        self.pbClearParams.setText(_translate("Form", "Clear params"))
        self.ckUseDate.setText(_translate("Form", "Include"))
        self.cbChannelDensity.setItemText(1, _translate("Form", "HD"))
        self.cbChannelDensity.setItemText(2, _translate("Form", "LD"))
        self.cbInstitution.setItemText(1, _translate("Form", "CERN"))
        self.cbInstitution.setItemText(2, _translate("Form", "FNAL"))
        self.cbInstitution.setItemText(3, _translate("Form", "UCSB"))
        self.cbInstitution.setItemText(4, _translate("Form", "UMN"))
        self.cbInstitution.setItemText(5, _translate("Form", "HEPHY"))
        self.cbInstitution.setItemText(6, _translate("Form", "HPK"))
        self.cbInstitution.setItemText(7, _translate("Form", "CMU"))
        self.cbInstitution.setItemText(8, _translate("Form", "TTU"))
        self.cbInstitution.setItemText(9, _translate("Form", "IHEP"))
        self.cbInstitution.setItemText(10, _translate("Form", "TIFR"))
        self.cbInstitution.setItemText(11, _translate("Form", "NTU"))
        self.cbInstitution.setItemText(12, _translate("Form", "FSU"))
        self.lineEdit_17.setText(_translate("Form", "Resolution type"))
        self.lineEdit_13.setText(_translate("Form", "Institution"))
        self.lineEdit_15.setText(_translate("Form", "Baseplate material"))
        self.lineEdit_16.setText(_translate("Form", "Sensor thickness"))
        self.cbAssmCol.setItemText(1, _translate("Form", "1"))
        self.cbAssmCol.setItemText(2, _translate("Form", "2"))
        self.lineEdit_18.setText(_translate("Form", "Creation date (proto/module)"))
        self.cbPCBType.setItemText(1, _translate("Form", "HGCROCV1"))
        self.cbPCBType.setItemText(2, _translate("Form", "HGCROCV2"))
        self.cbPCBType.setItemText(3, _translate("Form", "HGCROCV3"))
        self.cbPCBType.setItemText(4, _translate("Form", "SKIROCV1"))
        self.cbPCBType.setItemText(5, _translate("Form", "SKIROCV2"))
        self.cbPCBType.setItemText(6, _translate("Form", "SKIROCV3"))
        self.cbPCBType.setItemText(7, _translate("Form", "HGCROC dummy"))
        self.cbShape.setItemText(1, _translate("Form", "Full"))
        self.cbShape.setItemText(2, _translate("Form", "Top"))
        self.cbShape.setItemText(3, _translate("Form", "Bottom"))
        self.cbShape.setItemText(4, _translate("Form", "Left"))
        self.cbShape.setItemText(5, _translate("Form", "Right"))
        self.cbShape.setItemText(6, _translate("Form", "Five"))
        self.cbShape.setItemText(7, _translate("Form", "Full"))
        self.cbShape.setItemText(8, _translate("Form", "Three"))
        self.cbAssmRow.setItemText(1, _translate("Form", "1"))
        self.cbAssmRow.setItemText(2, _translate("Form", "2"))
        self.cbAssmRow.setItemText(3, _translate("Form", "3"))
        self.lineEdit_22.setText(_translate("Form", "col"))
        self.cbThickness.setItemText(1, _translate("Form", "120um"))
        self.cbThickness.setItemText(2, _translate("Form", "200um"))
        self.cbThickness.setItemText(3, _translate("Form", "300um"))
        self.lineEdit_14.setText(_translate("Form", "Geometry"))
        self.lineEdit_19.setText(_translate("Form", "PCB ROC type"))
        self.lineEdit_20.setText(_translate("Form", "Assembly posn (proto/module)"))
        self.lineEdit_21.setText(_translate("Form", "row"))
        self.cbMaterial.setItemText(1, _translate("Form", "CuW"))
        self.cbMaterial.setItemText(2, _translate("Form", "PCB"))
        self.label_7.setText(_translate("Form", "Part type:"))
        self.cbPartType.setItemText(0, _translate("Form", "Baseplate"))
        self.cbPartType.setItemText(1, _translate("Form", "Sensor"))
        self.cbPartType.setItemText(2, _translate("Form", "PCB"))
        self.cbPartType.setItemText(3, _translate("Form", "Protomodule"))
        self.cbPartType.setItemText(4, _translate("Form", "Module"))
        self.label_3.setText(_translate("Form", "Part attributes:"))
        self.pbGoToPart.setText(_translate("Form", "Go to selected item"))
        self.lineEdit_26.setText(_translate("Form", "Status:"))
        self.pbClearResults.setText(_translate("Form", "Clear results"))
        self.label.setText(_translate("Form", "Search results:"))
        self.label_2.setText(_translate("Form", "Part type:"))
