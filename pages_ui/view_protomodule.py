# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_protomodule.ui'
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
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 160, 261, 421))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setMidLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setGeometry(QtCore.QRect(1, 40, 121, 20))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.leLocation = QtWidgets.QLineEdit(self.frame_2)
        self.leLocation.setEnabled(False)
        self.leLocation.setGeometry(QtCore.QRect(120, 40, 141, 20))
        self.leLocation.setText("")
        self.leLocation.setReadOnly(True)
        self.leLocation.setObjectName("leLocation")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(1, 110, 181, 21))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pbAddComment = QtWidgets.QPushButton(self.frame_2)
        self.pbAddComment.setGeometry(QtCore.QRect(0, 400, 101, 21))
        self.pbAddComment.setObjectName("pbAddComment")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_14.setGeometry(QtCore.QRect(1, 180, 141, 21))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pbDeleteComment = QtWidgets.QPushButton(self.frame_2)
        self.pbDeleteComment.setGeometry(QtCore.QRect(140, 180, 121, 21))
        self.pbDeleteComment.setObjectName("pbDeleteComment")
        self.pteWriteComment = QtWidgets.QPlainTextEdit(self.frame_2)
        self.pteWriteComment.setGeometry(QtCore.QRect(0, 330, 261, 71))
        self.pteWriteComment.setObjectName("pteWriteComment")
        self.listComments = QtWidgets.QListWidget(self.frame_2)
        self.listComments.setGeometry(QtCore.QRect(0, 200, 261, 121))
        self.listComments.setObjectName("listComments")
        self.lineEdit_52 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_52.setGeometry(QtCore.QRect(1, 20, 121, 21))
        self.lineEdit_52.setReadOnly(True)
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_38.setGeometry(QtCore.QRect(1, 1, 121, 20))
        self.lineEdit_38.setReadOnly(True)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.cbInsertUser = QtWidgets.QComboBox(self.frame_2)
        self.cbInsertUser.setEnabled(False)
        self.cbInsertUser.setGeometry(QtCore.QRect(120, 0, 141, 21))
        self.cbInsertUser.setObjectName("cbInsertUser")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_22.setGeometry(QtCore.QRect(1, 130, 181, 21))
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.cbShape = QtWidgets.QComboBox(self.frame_2)
        self.cbShape.setEnabled(False)
        self.cbShape.setGeometry(QtCore.QRect(180, 110, 81, 20))
        self.cbShape.setObjectName("cbShape")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_23.setGeometry(QtCore.QRect(1, 90, 181, 21))
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.cbType = QtWidgets.QComboBox(self.frame_2)
        self.cbType.setEnabled(False)
        self.cbType.setGeometry(QtCore.QRect(180, 90, 81, 20))
        self.cbType.setObjectName("cbType")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbGrade = QtWidgets.QComboBox(self.frame_2)
        self.cbGrade.setEnabled(False)
        self.cbGrade.setGeometry(QtCore.QRect(180, 130, 81, 21))
        self.cbGrade.setObjectName("cbGrade")
        self.cbGrade.addItem("")
        self.cbGrade.addItem("")
        self.cbGrade.addItem("")
        self.cbInstitution = QtWidgets.QComboBox(self.frame_2)
        self.cbInstitution.setEnabled(False)
        self.cbInstitution.setGeometry(QtCore.QRect(120, 20, 141, 21))
        self.cbInstitution.setObjectName("cbInstitution")
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
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 261, 111))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.pbSave = QtWidgets.QPushButton(self.frame_3)
        self.pbSave.setGeometry(QtCore.QRect(50, 60, 71, 21))
        self.pbSave.setObjectName("pbSave")
        self.pbEdit = QtWidgets.QPushButton(self.frame_3)
        self.pbEdit.setGeometry(QtCore.QRect(130, 30, 71, 21))
        self.pbEdit.setObjectName("pbEdit")
        self.pbCancel = QtWidgets.QPushButton(self.frame_3)
        self.pbCancel.setGeometry(QtCore.QRect(130, 60, 71, 21))
        self.pbCancel.setObjectName("pbCancel")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QtCore.QRect(1, 1, 151, 19))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.leID = QtWidgets.QLineEdit(self.frame_3)
        self.leID.setGeometry(QtCore.QRect(150, 0, 111, 20))
        self.leID.setText("")
        self.leID.setReadOnly(True)
        self.leID.setObjectName("leID")
        self.leStatus = QtWidgets.QLineEdit(self.frame_3)
        self.leStatus.setGeometry(QtCore.QRect(80, 90, 171, 20))
        self.leStatus.setText("")
        self.leStatus.setReadOnly(True)
        self.leStatus.setObjectName("leStatus")
        self.pbLoad = QtWidgets.QPushButton(self.frame_3)
        self.pbLoad.setGeometry(QtCore.QRect(50, 30, 71, 21))
        self.pbLoad.setObjectName("pbLoad")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_27.setGeometry(QtCore.QRect(10, 90, 71, 20))
        self.lineEdit_27.setReadOnly(True)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(330, 350, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(330, 80, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(330, 190, 221, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(330, 10, 271, 51))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(330, 100, 271, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.leSensor = QtWidgets.QLineEdit(self.frame)
        self.leSensor.setGeometry(QtCore.QRect(90, 20, 131, 20))
        self.leSensor.setText("")
        self.leSensor.setReadOnly(True)
        self.leSensor.setObjectName("leSensor")
        self.pbGoSensor = QtWidgets.QPushButton(self.frame)
        self.pbGoSensor.setGeometry(QtCore.QRect(220, 20, 51, 21))
        self.pbGoSensor.setObjectName("pbGoSensor")
        self.pbGoStepSensor = QtWidgets.QPushButton(self.frame)
        self.pbGoStepSensor.setGeometry(QtCore.QRect(220, 0, 51, 21))
        self.pbGoStepSensor.setObjectName("pbGoStepSensor")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_17.setGeometry(QtCore.QRect(0, 40, 91, 21))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.pbGoBaseplate = QtWidgets.QPushButton(self.frame)
        self.pbGoBaseplate.setGeometry(QtCore.QRect(220, 40, 51, 21))
        self.pbGoBaseplate.setObjectName("pbGoBaseplate")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_13.setGeometry(QtCore.QRect(0, 0, 91, 21))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.leBaseplate = QtWidgets.QLineEdit(self.frame)
        self.leBaseplate.setGeometry(QtCore.QRect(90, 40, 131, 20))
        self.leBaseplate.setText("")
        self.leBaseplate.setReadOnly(True)
        self.leBaseplate.setObjectName("leBaseplate")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_12.setGeometry(QtCore.QRect(0, 20, 91, 21))
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.sbStepSensor = QtWidgets.QSpinBox(self.frame)
        self.sbStepSensor.setGeometry(QtCore.QRect(170, 0, 51, 21))
        self.sbStepSensor.setReadOnly(True)
        self.sbStepSensor.setMinimum(-1)
        self.sbStepSensor.setMaximum(2147483647)
        self.sbStepSensor.setObjectName("sbStepSensor")
        self.cbInstitutionStepSensor = QtWidgets.QComboBox(self.frame)
        self.cbInstitutionStepSensor.setEnabled(False)
        self.cbInstitutionStepSensor.setGeometry(QtCore.QRect(90, 0, 81, 21))
        self.cbInstitutionStepSensor.setObjectName("cbInstitutionStepSensor")
        self.cbInstitutionStepSensor.addItem("")
        self.cbInstitutionStepSensor.addItem("")
        self.cbInstitutionStepSensor.addItem("")
        self.cbInstitutionStepSensor.addItem("")
        self.cbInstitutionStepSensor.addItem("")
        self.cbInstitutionStepSensor.addItem("")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(330, 210, 271, 101))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.dsbThickness = QtWidgets.QDoubleSpinBox(self.frame_4)
        self.dsbThickness.setGeometry(QtCore.QRect(190, 80, 81, 21))
        self.dsbThickness.setReadOnly(True)
        self.dsbThickness.setMinimum(-1.0)
        self.dsbThickness.setMaximum(100.0)
        self.dsbThickness.setSingleStep(0.01)
        self.dsbThickness.setObjectName("dsbThickness")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_19.setGeometry(QtCore.QRect(0, 0, 191, 21))
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(0, 80, 191, 21))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.dsbOffsetTranslationX = QtWidgets.QDoubleSpinBox(self.frame_4)
        self.dsbOffsetTranslationX.setGeometry(QtCore.QRect(190, 0, 81, 21))
        self.dsbOffsetTranslationX.setReadOnly(True)
        self.dsbOffsetTranslationX.setMinimum(-1000.0)
        self.dsbOffsetTranslationX.setMaximum(1000.0)
        self.dsbOffsetTranslationX.setSingleStep(0.1)
        self.dsbOffsetTranslationX.setObjectName("dsbOffsetTranslationX")
        self.dsbFlatness = QtWidgets.QDoubleSpinBox(self.frame_4)
        self.dsbFlatness.setGeometry(QtCore.QRect(190, 60, 81, 21))
        self.dsbFlatness.setReadOnly(True)
        self.dsbFlatness.setMinimum(-10.0)
        self.dsbFlatness.setMaximum(10.0)
        self.dsbFlatness.setSingleStep(0.01)
        self.dsbFlatness.setObjectName("dsbFlatness")
        self.dsbOffsetRotation = QtWidgets.QDoubleSpinBox(self.frame_4)
        self.dsbOffsetRotation.setGeometry(QtCore.QRect(190, 40, 81, 21))
        self.dsbOffsetRotation.setReadOnly(True)
        self.dsbOffsetRotation.setMinimum(-180.0)
        self.dsbOffsetRotation.setMaximum(180.0)
        self.dsbOffsetRotation.setSingleStep(0.1)
        self.dsbOffsetRotation.setObjectName("dsbOffsetRotation")
        self.dsbOffsetTranslationY = QtWidgets.QDoubleSpinBox(self.frame_4)
        self.dsbOffsetTranslationY.setGeometry(QtCore.QRect(190, 20, 81, 21))
        self.dsbOffsetTranslationY.setReadOnly(True)
        self.dsbOffsetTranslationY.setMinimum(-1000.0)
        self.dsbOffsetTranslationY.setMaximum(1000.0)
        self.dsbOffsetTranslationY.setSingleStep(0.1)
        self.dsbOffsetTranslationY.setObjectName("dsbOffsetTranslationY")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_24.setGeometry(QtCore.QRect(0, 20, 191, 21))
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_21.setGeometry(QtCore.QRect(0, 60, 191, 21))
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_20.setGeometry(QtCore.QRect(0, 40, 191, 21))
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setGeometry(QtCore.QRect(330, 370, 271, 41))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.leModule = QtWidgets.QLineEdit(self.frame_5)
        self.leModule.setGeometry(QtCore.QRect(90, 20, 131, 20))
        self.leModule.setText("")
        self.leModule.setReadOnly(True)
        self.leModule.setObjectName("leModule")
        self.sbStepPcb = QtWidgets.QSpinBox(self.frame_5)
        self.sbStepPcb.setGeometry(QtCore.QRect(170, 0, 51, 21))
        self.sbStepPcb.setReadOnly(True)
        self.sbStepPcb.setMinimum(-1)
        self.sbStepPcb.setMaximum(2147483647)
        self.sbStepPcb.setObjectName("sbStepPcb")
        self.pbGoModule = QtWidgets.QPushButton(self.frame_5)
        self.pbGoModule.setGeometry(QtCore.QRect(220, 20, 51, 21))
        self.pbGoModule.setObjectName("pbGoModule")
        self.pbGoStepPcb = QtWidgets.QPushButton(self.frame_5)
        self.pbGoStepPcb.setGeometry(QtCore.QRect(220, 0, 51, 21))
        self.pbGoStepPcb.setObjectName("pbGoStepPcb")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_18.setGeometry(QtCore.QRect(0, 0, 91, 21))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_8.setGeometry(QtCore.QRect(0, 20, 91, 21))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.cbInstitutionStepPcb = QtWidgets.QComboBox(self.frame_5)
        self.cbInstitutionStepPcb.setEnabled(False)
        self.cbInstitutionStepPcb.setGeometry(QtCore.QRect(90, 0, 81, 21))
        self.cbInstitutionStepPcb.setObjectName("cbInstitutionStepPcb")
        self.cbInstitutionStepPcb.addItem("")
        self.cbInstitutionStepPcb.addItem("")
        self.cbInstitutionStepPcb.addItem("")
        self.cbInstitutionStepPcb.addItem("")
        self.cbInstitutionStepPcb.addItem("")
        self.cbInstitutionStepPcb.addItem("")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 151, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        self.cbInsertUser.setCurrentIndex(-1)
        self.cbShape.setCurrentIndex(-1)
        self.cbType.setCurrentIndex(-1)
        self.cbGrade.setCurrentIndex(-1)
        self.cbInstitution.setCurrentIndex(-1)
        self.cbInstitutionStepSensor.setCurrentIndex(-1)
        self.cbInstitutionStepPcb.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_9.setText(_translate("Form", "Location"))
        self.lineEdit_10.setText(_translate("Form", "Geometry"))
        self.pbAddComment.setText(_translate("Form", "Add comment"))
        self.lineEdit_14.setText(_translate("Form", "Comments"))
        self.pbDeleteComment.setText(_translate("Form", "Delete selected"))
        self.lineEdit_52.setText(_translate("Form", "Institution"))
        self.lineEdit_38.setToolTip(_translate("Form", "height difference between highest and lowers corners"))
        self.lineEdit_38.setText(_translate("Form", "User name"))
        self.lineEdit_22.setText(_translate("Form", "Grade"))
        self.cbShape.setItemText(0, _translate("Form", "Full"))
        self.cbShape.setItemText(1, _translate("Form", "Top"))
        self.cbShape.setItemText(2, _translate("Form", "Bottom"))
        self.cbShape.setItemText(3, _translate("Form", "Left"))
        self.cbShape.setItemText(4, _translate("Form", "Right"))
        self.cbShape.setItemText(5, _translate("Form", "Five"))
        self.cbShape.setItemText(6, _translate("Form", "Full"))
        self.cbShape.setItemText(7, _translate("Form", "Three"))
        self.lineEdit_23.setText(_translate("Form", "Resolution type"))
        self.cbType.setItemText(0, _translate("Form", "HD"))
        self.cbType.setItemText(1, _translate("Form", "LD"))
        self.cbGrade.setItemText(0, _translate("Form", "Green"))
        self.cbGrade.setItemText(1, _translate("Form", "Yellow"))
        self.cbGrade.setItemText(2, _translate("Form", "Red"))
        self.cbInstitution.setItemText(0, _translate("Form", "CERN"))
        self.cbInstitution.setItemText(1, _translate("Form", "FNAL"))
        self.cbInstitution.setItemText(2, _translate("Form", "UCSB"))
        self.cbInstitution.setItemText(3, _translate("Form", "UMN"))
        self.cbInstitution.setItemText(4, _translate("Form", "HEPHY"))
        self.cbInstitution.setItemText(5, _translate("Form", "HPK"))
        self.cbInstitution.setItemText(6, _translate("Form", "CMU"))
        self.cbInstitution.setItemText(7, _translate("Form", "TTU"))
        self.cbInstitution.setItemText(8, _translate("Form", "IHEP"))
        self.cbInstitution.setItemText(9, _translate("Form", "TIFR"))
        self.cbInstitution.setItemText(10, _translate("Form", "NTU"))
        self.cbInstitution.setItemText(11, _translate("Form", "FSU"))
        self.pbSave.setText(_translate("Form", "Save"))
        self.pbEdit.setText(_translate("Form", "Edit"))
        self.pbCancel.setText(_translate("Form", "Cancel"))
        self.lineEdit.setText(_translate("Form", "Protomodule ID"))
        self.pbLoad.setText(_translate("Form", "Load"))
        self.lineEdit_27.setText(_translate("Form", "Status:"))
        self.label.setText(_translate("Form", "PCB placement"))
        self.label_2.setText(_translate("Form", "Sensor placement"))
        self.label_3.setText(_translate("Form", "Sensor placement qualification"))
        self.label_4.setText(_translate("Form", "Note:  protomodules are automatically created upon completion of a sensor step."))
        self.pbGoSensor.setText(_translate("Form", "Go to"))
        self.pbGoStepSensor.setText(_translate("Form", "Go to"))
        self.lineEdit_17.setText(_translate("Form", "Baseplate"))
        self.pbGoBaseplate.setText(_translate("Form", "Go to"))
        self.lineEdit_13.setText(_translate("Form", "Sensor step"))
        self.lineEdit_12.setText(_translate("Form", "Sensor"))
        self.cbInstitutionStepSensor.setItemText(0, _translate("Form", "CERN"))
        self.cbInstitutionStepSensor.setItemText(1, _translate("Form", "FNAL"))
        self.cbInstitutionStepSensor.setItemText(2, _translate("Form", "UCSB"))
        self.cbInstitutionStepSensor.setItemText(3, _translate("Form", "UMN"))
        self.cbInstitutionStepSensor.setItemText(4, _translate("Form", "HEPHY"))
        self.cbInstitutionStepSensor.setItemText(5, _translate("Form", "HPK"))
        self.lineEdit_19.setText(_translate("Form", "x translational offset (μm)"))
        self.lineEdit_4.setText(_translate("Form", "Thickness (mm)"))
        self.lineEdit_24.setText(_translate("Form", "y translational offset (μm)"))
        self.lineEdit_21.setText(_translate("Form", "Flatness (mm)"))
        self.lineEdit_20.setText(_translate("Form", "Rotational offset (°)"))
        self.pbGoModule.setText(_translate("Form", "Go to"))
        self.pbGoStepPcb.setText(_translate("Form", "Go to"))
        self.lineEdit_18.setText(_translate("Form", "PCB step"))
        self.lineEdit_8.setText(_translate("Form", "On module"))
        self.cbInstitutionStepPcb.setItemText(0, _translate("Form", "CERN"))
        self.cbInstitutionStepPcb.setItemText(1, _translate("Form", "FNAL"))
        self.cbInstitutionStepPcb.setItemText(2, _translate("Form", "UCSB"))
        self.cbInstitutionStepPcb.setItemText(3, _translate("Form", "UMN"))
        self.cbInstitutionStepPcb.setItemText(4, _translate("Form", "HEPHY"))
        self.cbInstitutionStepPcb.setItemText(5, _translate("Form", "HPK"))
        self.label_6.setText(_translate("Form", "Standard information"))
