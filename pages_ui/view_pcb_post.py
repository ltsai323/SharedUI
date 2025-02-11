# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_pcb_post.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1097, 705)
        self.lineEdit_26 = QtWidgets.QLineEdit(Form)
        self.lineEdit_26.setGeometry(QtCore.QRect(10, 560, 61, 20))
        self.lineEdit_26.setReadOnly(True)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.listIssues = QtWidgets.QListWidget(Form)
        self.listIssues.setGeometry(QtCore.QRect(10, 390, 721, 171))
        self.listIssues.setObjectName("listIssues")
        self.leStatus = QtWidgets.QLineEdit(Form)
        self.leStatus.setGeometry(QtCore.QRect(70, 560, 171, 20))
        self.leStatus.setText("")
        self.leStatus.setReadOnly(True)
        self.leStatus.setObjectName("leStatus")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(770, 120, 101, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(290, 120, 161, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(510, 120, 161, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(680, 120, 71, 17))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(290, 290, 291, 16))
        self.label_8.setObjectName("label_8")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(770, 140, 311, 111))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_29.setGeometry(QtCore.QRect(0, 20, 71, 21))
        self.lineEdit_29.setReadOnly(True)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_28.setGeometry(QtCore.QRect(0, 0, 71, 21))
        self.lineEdit_28.setReadOnly(True)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_9.setGeometry(QtCore.QRect(0, 82, 131, 21))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.dsbCureTemperature = QtWidgets.QDoubleSpinBox(self.frame)
        self.dsbCureTemperature.setGeometry(QtCore.QRect(130, 48, 91, 26))
        self.dsbCureTemperature.setProperty("value", 70.0)
        self.dsbCureTemperature.setObjectName("dsbCureTemperature")
        self.pbCureStopNow = QtWidgets.QPushButton(self.frame)
        self.pbCureStopNow.setGeometry(QtCore.QRect(220, 20, 91, 21))
        self.pbCureStopNow.setObjectName("pbCureStopNow")
        self.dtCureStart = QtWidgets.QDateTimeEdit(self.frame)
        self.dtCureStart.setGeometry(QtCore.QRect(70, 0, 151, 21))
        self.dtCureStart.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dtCureStart.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.dtCureStart.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dtCureStart.setCalendarPopup(True)
        self.dtCureStart.setObjectName("dtCureStart")
        self.dtCureStop = QtWidgets.QDateTimeEdit(self.frame)
        self.dtCureStop.setGeometry(QtCore.QRect(70, 20, 151, 21))
        self.dtCureStop.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dtCureStop.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.dtCureStop.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dtCureStop.setCalendarPopup(True)
        self.dtCureStop.setObjectName("dtCureStop")
        self.sbCureHumidity = QtWidgets.QSpinBox(self.frame)
        self.sbCureHumidity.setGeometry(QtCore.QRect(130, 80, 91, 26))
        self.sbCureHumidity.setProperty("value", 10)
        self.sbCureHumidity.setObjectName("sbCureHumidity")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setGeometry(QtCore.QRect(0, 50, 131, 21))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pbCureStartNow = QtWidgets.QPushButton(self.frame)
        self.pbCureStartNow.setGeometry(QtCore.QRect(220, 0, 91, 21))
        self.pbCureStartNow.setObjectName("pbCureStartNow")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 201, 111))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.sbID = QtWidgets.QSpinBox(self.frame_2)
        self.sbID.setGeometry(QtCore.QRect(110, 0, 91, 21))
        self.sbID.setObjectName("sbID")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 111, 21))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_27.setGeometry(QtCore.QRect(0, 20, 111, 20))
        self.lineEdit_27.setReadOnly(True)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.pbSave = QtWidgets.QPushButton(self.frame_2)
        self.pbSave.setGeometry(QtCore.QRect(100, 50, 71, 21))
        self.pbSave.setObjectName("pbSave")
        self.pbCancel = QtWidgets.QPushButton(self.frame_2)
        self.pbCancel.setGeometry(QtCore.QRect(60, 80, 71, 21))
        self.pbCancel.setObjectName("pbCancel")
        self.pbEdit = QtWidgets.QPushButton(self.frame_2)
        self.pbEdit.setGeometry(QtCore.QRect(20, 50, 71, 21))
        self.pbEdit.setObjectName("pbEdit")
        self.cbInstitution = QtWidgets.QComboBox(self.frame_2)
        self.cbInstitution.setGeometry(QtCore.QRect(110, 20, 91, 21))
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
        self.frame_3.setGeometry(QtCore.QRect(10, 140, 751, 141))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.cbGrade6 = QtWidgets.QComboBox(self.frame_3)
        self.cbGrade6.setGeometry(QtCore.QRect(670, 120, 81, 21))
        self.cbGrade6.setObjectName("cbGrade6")
        self.cbGrade6.addItem("")
        self.cbGrade6.addItem("")
        self.cbGrade6.addItem("")
        self.dsbThickness1 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbThickness1.setGeometry(QtCore.QRect(580, 20, 81, 21))
        self.dsbThickness1.setReadOnly(False)
        self.dsbThickness1.setDecimals(3)
        self.dsbThickness1.setMinimum(-1.0)
        self.dsbThickness1.setMaximum(100.0)
        self.dsbThickness1.setSingleStep(0.1)
        self.dsbThickness1.setObjectName("dsbThickness1")
        self.dsbOffY1 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbOffY1.setGeometry(QtCore.QRect(350, 20, 71, 21))
        self.dsbOffY1.setReadOnly(False)
        self.dsbOffY1.setDecimals(0)
        self.dsbOffY1.setMinimum(-1000.0)
        self.dsbOffY1.setMaximum(1000.0)
        self.dsbOffY1.setSingleStep(0.01)
        self.dsbOffY1.setObjectName("dsbOffY1")
        self.cbGrade2 = QtWidgets.QComboBox(self.frame_3)
        self.cbGrade2.setGeometry(QtCore.QRect(670, 40, 81, 21))
        self.cbGrade2.setObjectName("cbGrade2")
        self.cbGrade2.addItem("")
        self.cbGrade2.addItem("")
        self.cbGrade2.addItem("")
        self.dsbFlatness1 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbFlatness1.setGeometry(QtCore.QRect(500, 20, 81, 21))
        self.dsbFlatness1.setReadOnly(False)
        self.dsbFlatness1.setDecimals(3)
        self.dsbFlatness1.setMinimum(-10.0)
        self.dsbFlatness1.setMaximum(10.0)
        self.dsbFlatness1.setSingleStep(0.1)
        self.dsbFlatness1.setObjectName("dsbFlatness1")
        self.cbGrade1 = QtWidgets.QComboBox(self.frame_3)
        self.cbGrade1.setGeometry(QtCore.QRect(670, 20, 81, 21))
        self.cbGrade1.setObjectName("cbGrade1")
        self.cbGrade1.addItem("")
        self.cbGrade1.addItem("")
        self.cbGrade1.addItem("")
        self.leModule3 = QtWidgets.QLineEdit(self.frame_3)
        self.leModule3.setGeometry(QtCore.QRect(80, 60, 141, 20))
        self.leModule3.setObjectName("leModule3")
        self.leModule2 = QtWidgets.QLineEdit(self.frame_3)
        self.leModule2.setGeometry(QtCore.QRect(80, 40, 141, 20))
        self.leModule2.setObjectName("leModule2")
        self.leModule6 = QtWidgets.QLineEdit(self.frame_3)
        self.leModule6.setGeometry(QtCore.QRect(80, 120, 141, 20))
        self.leModule6.setObjectName("leModule6")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_21.setGeometry(QtCore.QRect(280, 0, 71, 21))
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.dsbThickness3 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbThickness3.setGeometry(QtCore.QRect(580, 60, 81, 21))
        self.dsbThickness3.setReadOnly(False)
        self.dsbThickness3.setDecimals(3)
        self.dsbThickness3.setMinimum(-1.0)
        self.dsbThickness3.setMaximum(100.0)
        self.dsbThickness3.setSingleStep(0.1)
        self.dsbThickness3.setObjectName("dsbThickness3")
        self.pbGoModule5 = QtWidgets.QPushButton(self.frame_3)
        self.pbGoModule5.setGeometry(QtCore.QRect(220, 80, 51, 21))
        self.pbGoModule5.setObjectName("pbGoModule5")
        self.dsbFlatness6 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbFlatness6.setGeometry(QtCore.QRect(500, 120, 81, 21))
        self.dsbFlatness6.setReadOnly(False)
        self.dsbFlatness6.setDecimals(3)
        self.dsbFlatness6.setMinimum(-10.0)
        self.dsbFlatness6.setMaximum(10.0)
        self.dsbFlatness6.setSingleStep(0.1)
        self.dsbFlatness6.setObjectName("dsbFlatness6")
        self.dsbOffX3 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbOffX3.setGeometry(QtCore.QRect(280, 60, 71, 21))
        self.dsbOffX3.setReadOnly(False)
        self.dsbOffX3.setDecimals(0)
        self.dsbOffX3.setMinimum(-1000.0)
        self.dsbOffX3.setMaximum(1000.0)
        self.dsbOffX3.setSingleStep(0.01)
        self.dsbOffX3.setObjectName("dsbOffX3")
        self.pbGoModule2 = QtWidgets.QPushButton(self.frame_3)
        self.pbGoModule2.setGeometry(QtCore.QRect(220, 40, 51, 21))
        self.pbGoModule2.setObjectName("pbGoModule2")
        self.dsbOffY4 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbOffY4.setGeometry(QtCore.QRect(350, 80, 71, 21))
        self.dsbOffY4.setReadOnly(False)
        self.dsbOffY4.setDecimals(0)
        self.dsbOffY4.setMinimum(-1000.0)
        self.dsbOffY4.setMaximum(1000.0)
        self.dsbOffY4.setSingleStep(0.01)
        self.dsbOffY4.setObjectName("dsbOffY4")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_12.setGeometry(QtCore.QRect(0, 0, 71, 20))
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.dsbOffX2 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbOffX2.setGeometry(QtCore.QRect(280, 40, 71, 21))
        self.dsbOffX2.setReadOnly(False)
        self.dsbOffX2.setDecimals(0)
        self.dsbOffX2.setMinimum(-1000.0)
        self.dsbOffX2.setMaximum(1000.0)
        self.dsbOffX2.setSingleStep(0.01)
        self.dsbOffX2.setObjectName("dsbOffX2")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_23.setGeometry(QtCore.QRect(500, 0, 81, 21))
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.dsbOffX5 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbOffX5.setGeometry(QtCore.QRect(280, 100, 71, 21))
        self.dsbOffX5.setReadOnly(False)
        self.dsbOffX5.setDecimals(0)
        self.dsbOffX5.setMinimum(-1000.0)
        self.dsbOffX5.setMaximum(1000.0)
        self.dsbOffX5.setSingleStep(0.01)
        self.dsbOffX5.setObjectName("dsbOffX5")
        self.dsbFlatness5 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbFlatness5.setGeometry(QtCore.QRect(500, 100, 81, 21))
        self.dsbFlatness5.setReadOnly(False)
        self.dsbFlatness5.setDecimals(3)
        self.dsbFlatness5.setMinimum(-10.0)
        self.dsbFlatness5.setMaximum(10.0)
        self.dsbFlatness5.setSingleStep(0.1)
        self.dsbFlatness5.setObjectName("dsbFlatness5")
        self.dsbOffRot4 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbOffRot4.setGeometry(QtCore.QRect(420, 80, 71, 21))
        self.dsbOffRot4.setReadOnly(False)
        self.dsbOffRot4.setDecimals(3)
        self.dsbOffRot4.setMinimum(-180.0)
        self.dsbOffRot4.setMaximum(180.0)
        self.dsbOffRot4.setSingleStep(0.1)
        self.dsbOffRot4.setObjectName("dsbOffRot4")
        self.dsbOffRot1 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbOffRot1.setGeometry(QtCore.QRect(420, 20, 71, 21))
        self.dsbOffRot1.setReadOnly(False)
        self.dsbOffRot1.setDecimals(3)
        self.dsbOffRot1.setMinimum(-180.0)
        self.dsbOffRot1.setMaximum(180.0)
        self.dsbOffRot1.setSingleStep(0.1)
        self.dsbOffRot1.setObjectName("dsbOffRot1")
        self.dsbThickness6 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbThickness6.setGeometry(QtCore.QRect(580, 120, 81, 21))
        self.dsbThickness6.setReadOnly(False)
        self.dsbThickness6.setDecimals(3)
        self.dsbThickness6.setMinimum(-1.0)
        self.dsbThickness6.setMaximum(100.0)
        self.dsbThickness6.setSingleStep(0.1)
        self.dsbThickness6.setObjectName("dsbThickness6")
        self.leModule4 = QtWidgets.QLineEdit(self.frame_3)
        self.leModule4.setGeometry(QtCore.QRect(80, 80, 141, 20))
        self.leModule4.setObjectName("leModule4")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_17.setGeometry(QtCore.QRect(0, 60, 71, 20))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.leModule5 = QtWidgets.QLineEdit(self.frame_3)
        self.leModule5.setGeometry(QtCore.QRect(80, 100, 141, 20))
        self.leModule5.setObjectName("leModule5")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_31.setGeometry(QtCore.QRect(670, 0, 81, 21))
        self.lineEdit_31.setReadOnly(True)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.dsbOffY2 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbOffY2.setGeometry(QtCore.QRect(350, 40, 71, 21))
        self.dsbOffY2.setReadOnly(False)
        self.dsbOffY2.setDecimals(0)
        self.dsbOffY2.setMinimum(-1000.0)
        self.dsbOffY2.setMaximum(1000.0)
        self.dsbOffY2.setSingleStep(0.01)
        self.dsbOffY2.setObjectName("dsbOffY2")
        self.dsbOffY6 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbOffY6.setGeometry(QtCore.QRect(350, 120, 71, 21))
        self.dsbOffY6.setReadOnly(False)
        self.dsbOffY6.setDecimals(0)
        self.dsbOffY6.setMinimum(-1000.0)
        self.dsbOffY6.setMaximum(1000.0)
        self.dsbOffY6.setSingleStep(0.01)
        self.dsbOffY6.setObjectName("dsbOffY6")
        self.dsbOffRot6 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbOffRot6.setGeometry(QtCore.QRect(420, 120, 71, 21))
        self.dsbOffRot6.setReadOnly(False)
        self.dsbOffRot6.setDecimals(3)
        self.dsbOffRot6.setMinimum(-180.0)
        self.dsbOffRot6.setMaximum(180.0)
        self.dsbOffRot6.setSingleStep(0.1)
        self.dsbOffRot6.setObjectName("dsbOffRot6")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_14.setGeometry(QtCore.QRect(80, 0, 191, 20))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.dsbThickness2 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbThickness2.setGeometry(QtCore.QRect(580, 40, 81, 21))
        self.dsbThickness2.setReadOnly(False)
        self.dsbThickness2.setDecimals(3)
        self.dsbThickness2.setMinimum(-1.0)
        self.dsbThickness2.setMaximum(100.0)
        self.dsbThickness2.setSingleStep(0.1)
        self.dsbThickness2.setObjectName("dsbThickness2")
        self.dsbFlatness3 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbFlatness3.setGeometry(QtCore.QRect(500, 60, 81, 21))
        self.dsbFlatness3.setReadOnly(False)
        self.dsbFlatness3.setDecimals(3)
        self.dsbFlatness3.setMinimum(-10.0)
        self.dsbFlatness3.setMaximum(10.0)
        self.dsbFlatness3.setSingleStep(0.1)
        self.dsbFlatness3.setObjectName("dsbFlatness3")
        self.dsbThickness4 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbThickness4.setGeometry(QtCore.QRect(580, 80, 81, 21))
        self.dsbThickness4.setReadOnly(False)
        self.dsbThickness4.setDecimals(3)
        self.dsbThickness4.setMinimum(-1.0)
        self.dsbThickness4.setMaximum(100.0)
        self.dsbThickness4.setSingleStep(0.1)
        self.dsbThickness4.setObjectName("dsbThickness4")
        self.pbGoModule4 = QtWidgets.QPushButton(self.frame_3)
        self.pbGoModule4.setGeometry(QtCore.QRect(220, 120, 51, 21))
        self.pbGoModule4.setObjectName("pbGoModule4")
        self.pbGoModule6 = QtWidgets.QPushButton(self.frame_3)
        self.pbGoModule6.setGeometry(QtCore.QRect(220, 100, 51, 21))
        self.pbGoModule6.setObjectName("pbGoModule6")
        self.dsbFlatness4 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbFlatness4.setGeometry(QtCore.QRect(500, 80, 81, 21))
        self.dsbFlatness4.setReadOnly(False)
        self.dsbFlatness4.setDecimals(3)
        self.dsbFlatness4.setMinimum(-10.0)
        self.dsbFlatness4.setMaximum(10.0)
        self.dsbFlatness4.setSingleStep(0.1)
        self.dsbFlatness4.setObjectName("dsbFlatness4")
        self.pbGoModule3 = QtWidgets.QPushButton(self.frame_3)
        self.pbGoModule3.setGeometry(QtCore.QRect(220, 60, 51, 21))
        self.pbGoModule3.setObjectName("pbGoModule3")
        self.dsbOffX6 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbOffX6.setGeometry(QtCore.QRect(280, 120, 71, 21))
        self.dsbOffX6.setReadOnly(False)
        self.dsbOffX6.setDecimals(0)
        self.dsbOffX6.setMinimum(-1000.0)
        self.dsbOffX6.setMaximum(1000.0)
        self.dsbOffX6.setSingleStep(0.01)
        self.dsbOffX6.setObjectName("dsbOffX6")
        self.dsbThickness5 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbThickness5.setGeometry(QtCore.QRect(580, 100, 81, 21))
        self.dsbThickness5.setReadOnly(False)
        self.dsbThickness5.setDecimals(3)
        self.dsbThickness5.setMinimum(-1.0)
        self.dsbThickness5.setMaximum(100.0)
        self.dsbThickness5.setSingleStep(0.1)
        self.dsbThickness5.setObjectName("dsbThickness5")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_20.setGeometry(QtCore.QRect(0, 120, 71, 21))
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.dsbOffRot2 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbOffRot2.setGeometry(QtCore.QRect(420, 40, 71, 21))
        self.dsbOffRot2.setReadOnly(False)
        self.dsbOffRot2.setDecimals(3)
        self.dsbOffRot2.setMinimum(-180.0)
        self.dsbOffRot2.setMaximum(180.0)
        self.dsbOffRot2.setSingleStep(0.1)
        self.dsbOffRot2.setObjectName("dsbOffRot2")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_19.setGeometry(QtCore.QRect(0, 100, 71, 20))
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_22.setGeometry(QtCore.QRect(420, 0, 71, 21))
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.dsbOffRot5 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbOffRot5.setGeometry(QtCore.QRect(420, 100, 71, 21))
        self.dsbOffRot5.setReadOnly(False)
        self.dsbOffRot5.setDecimals(3)
        self.dsbOffRot5.setMinimum(-180.0)
        self.dsbOffRot5.setMaximum(180.0)
        self.dsbOffRot5.setSingleStep(0.1)
        self.dsbOffRot5.setObjectName("dsbOffRot5")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_15.setGeometry(QtCore.QRect(0, 20, 71, 20))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.dsbOffY3 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbOffY3.setGeometry(QtCore.QRect(350, 60, 71, 21))
        self.dsbOffY3.setReadOnly(False)
        self.dsbOffY3.setDecimals(0)
        self.dsbOffY3.setMinimum(-1000.0)
        self.dsbOffY3.setMaximum(1000.0)
        self.dsbOffY3.setSingleStep(0.01)
        self.dsbOffY3.setObjectName("dsbOffY3")
        self.dsbOffY5 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbOffY5.setGeometry(QtCore.QRect(350, 100, 71, 21))
        self.dsbOffY5.setReadOnly(False)
        self.dsbOffY5.setDecimals(0)
        self.dsbOffY5.setMinimum(-1000.0)
        self.dsbOffY5.setMaximum(1000.0)
        self.dsbOffY5.setSingleStep(0.01)
        self.dsbOffY5.setObjectName("dsbOffY5")
        self.cbGrade5 = QtWidgets.QComboBox(self.frame_3)
        self.cbGrade5.setGeometry(QtCore.QRect(670, 100, 81, 21))
        self.cbGrade5.setObjectName("cbGrade5")
        self.cbGrade5.addItem("")
        self.cbGrade5.addItem("")
        self.cbGrade5.addItem("")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_30.setGeometry(QtCore.QRect(580, 0, 81, 21))
        self.lineEdit_30.setReadOnly(True)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.cbGrade4 = QtWidgets.QComboBox(self.frame_3)
        self.cbGrade4.setGeometry(QtCore.QRect(670, 80, 81, 21))
        self.cbGrade4.setObjectName("cbGrade4")
        self.cbGrade4.addItem("")
        self.cbGrade4.addItem("")
        self.cbGrade4.addItem("")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_24.setGeometry(QtCore.QRect(350, 0, 71, 21))
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_16.setGeometry(QtCore.QRect(0, 40, 71, 20))
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_18.setGeometry(QtCore.QRect(0, 80, 71, 20))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.dsbFlatness2 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbFlatness2.setGeometry(QtCore.QRect(500, 40, 81, 21))
        self.dsbFlatness2.setReadOnly(False)
        self.dsbFlatness2.setDecimals(3)
        self.dsbFlatness2.setMinimum(-10.0)
        self.dsbFlatness2.setMaximum(10.0)
        self.dsbFlatness2.setSingleStep(0.1)
        self.dsbFlatness2.setObjectName("dsbFlatness2")
        self.cbGrade3 = QtWidgets.QComboBox(self.frame_3)
        self.cbGrade3.setGeometry(QtCore.QRect(670, 60, 81, 21))
        self.cbGrade3.setObjectName("cbGrade3")
        self.cbGrade3.addItem("")
        self.cbGrade3.addItem("")
        self.cbGrade3.addItem("")
        self.dsbOffX1 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbOffX1.setGeometry(QtCore.QRect(280, 20, 71, 21))
        self.dsbOffX1.setReadOnly(False)
        self.dsbOffX1.setDecimals(0)
        self.dsbOffX1.setMinimum(-1000.0)
        self.dsbOffX1.setMaximum(1000.0)
        self.dsbOffX1.setSingleStep(0.01)
        self.dsbOffX1.setObjectName("dsbOffX1")
        self.dsbOffX4 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbOffX4.setGeometry(QtCore.QRect(280, 80, 71, 21))
        self.dsbOffX4.setReadOnly(False)
        self.dsbOffX4.setDecimals(0)
        self.dsbOffX4.setMinimum(-1000.0)
        self.dsbOffX4.setMaximum(1000.0)
        self.dsbOffX4.setSingleStep(0.01)
        self.dsbOffX4.setObjectName("dsbOffX4")
        self.dsbOffRot3 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsbOffRot3.setGeometry(QtCore.QRect(420, 60, 71, 21))
        self.dsbOffRot3.setReadOnly(False)
        self.dsbOffRot3.setDecimals(3)
        self.dsbOffRot3.setMinimum(-180.0)
        self.dsbOffRot3.setMaximum(180.0)
        self.dsbOffRot3.setSingleStep(0.1)
        self.dsbOffRot3.setObjectName("dsbOffRot3")
        self.leModule1 = QtWidgets.QLineEdit(self.frame_3)
        self.leModule1.setGeometry(QtCore.QRect(80, 20, 141, 20))
        self.leModule1.setObjectName("leModule1")
        self.pbGoModule1 = QtWidgets.QPushButton(self.frame_3)
        self.pbGoModule1.setGeometry(QtCore.QRect(220, 20, 51, 21))
        self.pbGoModule1.setObjectName("pbGoModule1")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(290, 310, 331, 51))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.leXML = QtWidgets.QLineEdit(self.frame_4)
        self.leXML.setEnabled(True)
        self.leXML.setGeometry(QtCore.QRect(100, 0, 231, 20))
        self.leXML.setReadOnly(True)
        self.leXML.setObjectName("leXML")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_32.setGeometry(QtCore.QRect(0, 0, 101, 21))
        self.lineEdit_32.setReadOnly(True)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.pbAddFile = QtWidgets.QPushButton(self.frame_4)
        self.pbAddFile.setGeometry(QtCore.QRect(0, 20, 101, 31))
        self.pbAddFile.setObjectName("pbAddFile")

        self.retranslateUi(Form)
        self.cbInstitution.setCurrentIndex(-1)
        self.cbGrade6.setCurrentIndex(-1)
        self.cbGrade2.setCurrentIndex(-1)
        self.cbGrade1.setCurrentIndex(-1)
        self.cbGrade5.setCurrentIndex(-1)
        self.cbGrade4.setCurrentIndex(-1)
        self.cbGrade3.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_26.setText(_translate("Form", "Status:"))
        self.listIssues.setToolTip(_translate("Form", "list of issues"))
        self.label_3.setText(_translate("Form", "Curing"))
        self.label_4.setText(_translate("Form", "Placement offsets"))
        self.label_5.setText(_translate("Form", "Flatness & thickness"))
        self.label_6.setText(_translate("Form", "Quality"))
        self.label_8.setText(_translate("Form", "Load assembly measurements from XML"))
        self.lineEdit_29.setText(_translate("Form", "cure stop"))
        self.lineEdit_28.setText(_translate("Form", "cure start"))
        self.lineEdit_9.setText(_translate("Form", "cure humidity (%)"))
        self.pbCureStopNow.setText(_translate("Form", "set to now"))
        self.lineEdit_8.setText(_translate("Form", "cure temp (C)"))
        self.pbCureStartNow.setText(_translate("Form", "set to now"))
        self.lineEdit.setText(_translate("Form", "PCB step ID"))
        self.lineEdit_27.setText(_translate("Form", "Institution"))
        self.pbSave.setText(_translate("Form", "Save"))
        self.pbCancel.setText(_translate("Form", "Cancel"))
        self.pbEdit.setText(_translate("Form", "Edit"))
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
        self.cbGrade6.setItemText(0, _translate("Form", "Green"))
        self.cbGrade6.setItemText(1, _translate("Form", "Yellow"))
        self.cbGrade6.setItemText(2, _translate("Form", "Red"))
        self.cbGrade2.setItemText(0, _translate("Form", "Green"))
        self.cbGrade2.setItemText(1, _translate("Form", "Yellow"))
        self.cbGrade2.setItemText(2, _translate("Form", "Red"))
        self.cbGrade1.setItemText(0, _translate("Form", "Green"))
        self.cbGrade1.setItemText(1, _translate("Form", "Yellow"))
        self.cbGrade1.setItemText(2, _translate("Form", "Red"))
        self.lineEdit_21.setText(_translate("Form", "x (μm)"))
        self.pbGoModule5.setText(_translate("Form", "go to"))
        self.pbGoModule2.setText(_translate("Form", "go to"))
        self.lineEdit_12.setText(_translate("Form", "position"))
        self.lineEdit_23.setText(_translate("Form", "Flat (mm)"))
        self.lineEdit_17.setText(_translate("Form", "3 (2, 1)"))
        self.lineEdit_31.setText(_translate("Form", "Grade"))
        self.lineEdit_14.setText(_translate("Form", "Module serial"))
        self.pbGoModule4.setText(_translate("Form", "go to"))
        self.pbGoModule6.setText(_translate("Form", "go to"))
        self.pbGoModule3.setText(_translate("Form", "go to"))
        self.lineEdit_20.setText(_translate("Form", "6 (3, 2)"))
        self.lineEdit_19.setText(_translate("Form", "5 (3, 1)"))
        self.lineEdit_22.setText(_translate("Form", "θ (°)"))
        self.lineEdit_15.setText(_translate("Form", "1 (1, 1)"))
        self.cbGrade5.setItemText(0, _translate("Form", "Green"))
        self.cbGrade5.setItemText(1, _translate("Form", "Yellow"))
        self.cbGrade5.setItemText(2, _translate("Form", "Red"))
        self.lineEdit_30.setText(_translate("Form", "Thick (mm)"))
        self.cbGrade4.setItemText(0, _translate("Form", "Green"))
        self.cbGrade4.setItemText(1, _translate("Form", "Yellow"))
        self.cbGrade4.setItemText(2, _translate("Form", "Red"))
        self.lineEdit_24.setText(_translate("Form", "y (μm)"))
        self.lineEdit_16.setText(_translate("Form", "2 (1, 2)"))
        self.lineEdit_18.setText(_translate("Form", "4 (2, 2)"))
        self.cbGrade3.setItemText(0, _translate("Form", "Green"))
        self.cbGrade3.setItemText(1, _translate("Form", "Yellow"))
        self.cbGrade3.setItemText(2, _translate("Form", "Red"))
        self.pbGoModule1.setText(_translate("Form", "go to"))
        self.lineEdit_32.setText(_translate("Form", "Uploaded file"))
        self.pbAddFile.setText(_translate("Form", "Select file"))
