# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_tooling.ui'
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
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(650, 10, 251, 311))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_23.setGeometry(QtCore.QRect(0, 20, 111, 21))
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.sbAssemblyTrayID = QtWidgets.QSpinBox(self.frame)
        self.sbAssemblyTrayID.setGeometry(QtCore.QRect(130, 0, 51, 21))
        self.sbAssemblyTrayID.setMaximum(2147483647)
        self.sbAssemblyTrayID.setObjectName("sbAssemblyTrayID")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_13.setGeometry(QtCore.QRect(0, 70, 121, 21))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.pbAssemblyTrayDeleteComment = QtWidgets.QPushButton(self.frame)
        self.pbAssemblyTrayDeleteComment.setGeometry(QtCore.QRect(120, 70, 131, 21))
        self.pbAssemblyTrayDeleteComment.setObjectName("pbAssemblyTrayDeleteComment")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_15.setGeometry(QtCore.QRect(0, 0, 131, 21))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.pbAssemblyTrayEditNew = QtWidgets.QPushButton(self.frame)
        self.pbAssemblyTrayEditNew.setGeometry(QtCore.QRect(180, 0, 71, 21))
        self.pbAssemblyTrayEditNew.setObjectName("pbAssemblyTrayEditNew")
        self.listAssemblyTrayComments = QtWidgets.QListWidget(self.frame)
        self.listAssemblyTrayComments.setGeometry(QtCore.QRect(0, 90, 251, 121))
        self.listAssemblyTrayComments.setObjectName("listAssemblyTrayComments")
        self.pbAssemblyTrayAddComment = QtWidgets.QPushButton(self.frame)
        self.pbAssemblyTrayAddComment.setGeometry(QtCore.QRect(0, 290, 111, 21))
        self.pbAssemblyTrayAddComment.setObjectName("pbAssemblyTrayAddComment")
        self.pbAssemblyTraySave = QtWidgets.QPushButton(self.frame)
        self.pbAssemblyTraySave.setGeometry(QtCore.QRect(180, 20, 71, 21))
        self.pbAssemblyTraySave.setObjectName("pbAssemblyTraySave")
        self.pbAssemblyTrayCancel = QtWidgets.QPushButton(self.frame)
        self.pbAssemblyTrayCancel.setGeometry(QtCore.QRect(180, 40, 71, 21))
        self.pbAssemblyTrayCancel.setObjectName("pbAssemblyTrayCancel")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_18.setGeometry(QtCore.QRect(0, 40, 71, 21))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.pteAssemblyTrayWriteComment = QtWidgets.QPlainTextEdit(self.frame)
        self.pteAssemblyTrayWriteComment.setGeometry(QtCore.QRect(0, 220, 251, 71))
        self.pteAssemblyTrayWriteComment.setObjectName("pteAssemblyTrayWriteComment")
        self.leAssemblyTrayLocation = QtWidgets.QLineEdit(self.frame)
        self.leAssemblyTrayLocation.setGeometry(QtCore.QRect(70, 40, 111, 20))
        self.leAssemblyTrayLocation.setObjectName("leAssemblyTrayLocation")
        self.cbAssemblyTrayInstitution = QtWidgets.QComboBox(self.frame)
        self.cbAssemblyTrayInstitution.setGeometry(QtCore.QRect(110, 20, 71, 21))
        self.cbAssemblyTrayInstitution.setObjectName("cbAssemblyTrayInstitution")
        self.cbAssemblyTrayInstitution.addItem("")
        self.cbAssemblyTrayInstitution.setItemText(0, "")
        self.cbAssemblyTrayInstitution.addItem("")
        self.cbAssemblyTrayInstitution.addItem("")
        self.cbAssemblyTrayInstitution.addItem("")
        self.cbAssemblyTrayInstitution.addItem("")
        self.cbAssemblyTrayInstitution.addItem("")
        self.cbAssemblyTrayInstitution.addItem("")
        self.cbAssemblyTrayInstitution.addItem("")
        self.cbAssemblyTrayInstitution.addItem("")
        self.cbAssemblyTrayInstitution.addItem("")
        self.cbAssemblyTrayInstitution.addItem("")
        self.cbAssemblyTrayInstitution.addItem("")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(310, 350, 291, 311))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lePcbTrayLocation = QtWidgets.QLineEdit(self.frame_2)
        self.lePcbTrayLocation.setGeometry(QtCore.QRect(70, 40, 151, 20))
        self.lePcbTrayLocation.setObjectName("lePcbTrayLocation")
        self.listPcbTrayComments = QtWidgets.QListWidget(self.frame_2)
        self.listPcbTrayComments.setGeometry(QtCore.QRect(0, 90, 291, 121))
        self.listPcbTrayComments.setObjectName("listPcbTrayComments")
        self.sbPcbTrayID = QtWidgets.QSpinBox(self.frame_2)
        self.sbPcbTrayID.setGeometry(QtCore.QRect(170, 0, 51, 21))
        self.sbPcbTrayID.setMaximum(2147483647)
        self.sbPcbTrayID.setObjectName("sbPcbTrayID")
        self.pbPcbTrayEditNew = QtWidgets.QPushButton(self.frame_2)
        self.pbPcbTrayEditNew.setGeometry(QtCore.QRect(220, 0, 71, 21))
        self.pbPcbTrayEditNew.setObjectName("pbPcbTrayEditNew")
        self.pbPcbTrayCancel = QtWidgets.QPushButton(self.frame_2)
        self.pbPcbTrayCancel.setGeometry(QtCore.QRect(220, 40, 71, 21))
        self.pbPcbTrayCancel.setObjectName("pbPcbTrayCancel")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_20.setGeometry(QtCore.QRect(0, 40, 71, 21))
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.ptePcbTrayWriteComment = QtWidgets.QPlainTextEdit(self.frame_2)
        self.ptePcbTrayWriteComment.setGeometry(QtCore.QRect(0, 220, 291, 71))
        self.ptePcbTrayWriteComment.setObjectName("ptePcbTrayWriteComment")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_25.setGeometry(QtCore.QRect(0, 20, 151, 21))
        self.lineEdit_25.setReadOnly(True)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(0, 70, 161, 21))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pbPcbTrayAddComment = QtWidgets.QPushButton(self.frame_2)
        self.pbPcbTrayAddComment.setGeometry(QtCore.QRect(0, 290, 111, 21))
        self.pbPcbTrayAddComment.setObjectName("pbPcbTrayAddComment")
        self.pbPcbTrayDeleteComment = QtWidgets.QPushButton(self.frame_2)
        self.pbPcbTrayDeleteComment.setGeometry(QtCore.QRect(160, 70, 131, 21))
        self.pbPcbTrayDeleteComment.setObjectName("pbPcbTrayDeleteComment")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(0, 0, 171, 21))
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.pbPcbTraySave = QtWidgets.QPushButton(self.frame_2)
        self.pbPcbTraySave.setGeometry(QtCore.QRect(220, 20, 71, 21))
        self.pbPcbTraySave.setObjectName("pbPcbTraySave")
        self.cbPcbTrayInstitution = QtWidgets.QComboBox(self.frame_2)
        self.cbPcbTrayInstitution.setGeometry(QtCore.QRect(150, 20, 71, 21))
        self.cbPcbTrayInstitution.setObjectName("cbPcbTrayInstitution")
        self.cbPcbTrayInstitution.addItem("")
        self.cbPcbTrayInstitution.setItemText(0, "")
        self.cbPcbTrayInstitution.addItem("")
        self.cbPcbTrayInstitution.addItem("")
        self.cbPcbTrayInstitution.addItem("")
        self.cbPcbTrayInstitution.addItem("")
        self.cbPcbTrayInstitution.addItem("")
        self.cbPcbTrayInstitution.addItem("")
        self.cbPcbTrayInstitution.addItem("")
        self.cbPcbTrayInstitution.addItem("")
        self.cbPcbTrayInstitution.addItem("")
        self.cbPcbTrayInstitution.addItem("")
        self.cbPcbTrayInstitution.addItem("")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(10, 350, 251, 311))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pbPcbToolSave = QtWidgets.QPushButton(self.frame_3)
        self.pbPcbToolSave.setGeometry(QtCore.QRect(180, 20, 71, 21))
        self.pbPcbToolSave.setObjectName("pbPcbToolSave")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(0, 0, 131, 21))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.sbPcbToolID = QtWidgets.QSpinBox(self.frame_3)
        self.sbPcbToolID.setGeometry(QtCore.QRect(130, 0, 51, 21))
        self.sbPcbToolID.setMaximum(2147483647)
        self.sbPcbToolID.setObjectName("sbPcbToolID")
        self.pbPcbToolCancel = QtWidgets.QPushButton(self.frame_3)
        self.pbPcbToolCancel.setGeometry(QtCore.QRect(180, 40, 71, 21))
        self.pbPcbToolCancel.setObjectName("pbPcbToolCancel")
        self.pbPcbToolDeleteComment = QtWidgets.QPushButton(self.frame_3)
        self.pbPcbToolDeleteComment.setGeometry(QtCore.QRect(120, 70, 131, 21))
        self.pbPcbToolDeleteComment.setObjectName("pbPcbToolDeleteComment")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_24.setGeometry(QtCore.QRect(0, 20, 111, 21))
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.ptePcbToolWriteComment = QtWidgets.QPlainTextEdit(self.frame_3)
        self.ptePcbToolWriteComment.setGeometry(QtCore.QRect(0, 220, 251, 71))
        self.ptePcbToolWriteComment.setObjectName("ptePcbToolWriteComment")
        self.listPcbToolComments = QtWidgets.QListWidget(self.frame_3)
        self.listPcbToolComments.setGeometry(QtCore.QRect(0, 90, 251, 121))
        self.listPcbToolComments.setObjectName("listPcbToolComments")
        self.pbPcbToolAddComment = QtWidgets.QPushButton(self.frame_3)
        self.pbPcbToolAddComment.setGeometry(QtCore.QRect(0, 290, 111, 21))
        self.pbPcbToolAddComment.setObjectName("pbPcbToolAddComment")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(0, 70, 121, 21))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pbPcbToolEditNew = QtWidgets.QPushButton(self.frame_3)
        self.pbPcbToolEditNew.setGeometry(QtCore.QRect(180, 0, 71, 21))
        self.pbPcbToolEditNew.setObjectName("pbPcbToolEditNew")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_19.setGeometry(QtCore.QRect(0, 40, 71, 21))
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lePcbToolLocation = QtWidgets.QLineEdit(self.frame_3)
        self.lePcbToolLocation.setGeometry(QtCore.QRect(70, 40, 111, 20))
        self.lePcbToolLocation.setObjectName("lePcbToolLocation")
        self.cbPcbToolInstitution = QtWidgets.QComboBox(self.frame_3)
        self.cbPcbToolInstitution.setGeometry(QtCore.QRect(110, 20, 71, 21))
        self.cbPcbToolInstitution.setObjectName("cbPcbToolInstitution")
        self.cbPcbToolInstitution.addItem("")
        self.cbPcbToolInstitution.setItemText(0, "")
        self.cbPcbToolInstitution.addItem("")
        self.cbPcbToolInstitution.addItem("")
        self.cbPcbToolInstitution.addItem("")
        self.cbPcbToolInstitution.addItem("")
        self.cbPcbToolInstitution.addItem("")
        self.cbPcbToolInstitution.addItem("")
        self.cbPcbToolInstitution.addItem("")
        self.cbPcbToolInstitution.addItem("")
        self.cbPcbToolInstitution.addItem("")
        self.cbPcbToolInstitution.addItem("")
        self.cbPcbToolInstitution.addItem("")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(310, 10, 291, 311))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_22.setGeometry(QtCore.QRect(0, 20, 151, 21))
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.sbSensorTrayID = QtWidgets.QSpinBox(self.frame_4)
        self.sbSensorTrayID.setGeometry(QtCore.QRect(170, 0, 51, 21))
        self.sbSensorTrayID.setMaximum(2147483647)
        self.sbSensorTrayID.setObjectName("sbSensorTrayID")
        self.pbSensorTrayAddComment = QtWidgets.QPushButton(self.frame_4)
        self.pbSensorTrayAddComment.setGeometry(QtCore.QRect(0, 290, 111, 21))
        self.pbSensorTrayAddComment.setObjectName("pbSensorTrayAddComment")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(0, 70, 161, 21))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_10.setGeometry(QtCore.QRect(0, 0, 171, 21))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_17.setGeometry(QtCore.QRect(0, 40, 71, 21))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.pteSensorTrayWriteComment = QtWidgets.QPlainTextEdit(self.frame_4)
        self.pteSensorTrayWriteComment.setGeometry(QtCore.QRect(0, 220, 291, 71))
        self.pteSensorTrayWriteComment.setObjectName("pteSensorTrayWriteComment")
        self.pbSensorTrayEditNew = QtWidgets.QPushButton(self.frame_4)
        self.pbSensorTrayEditNew.setGeometry(QtCore.QRect(220, 0, 71, 21))
        self.pbSensorTrayEditNew.setObjectName("pbSensorTrayEditNew")
        self.pbSensorTraySave = QtWidgets.QPushButton(self.frame_4)
        self.pbSensorTraySave.setGeometry(QtCore.QRect(220, 20, 71, 21))
        self.pbSensorTraySave.setObjectName("pbSensorTraySave")
        self.listSensorTrayComments = QtWidgets.QListWidget(self.frame_4)
        self.listSensorTrayComments.setGeometry(QtCore.QRect(0, 90, 291, 121))
        self.listSensorTrayComments.setObjectName("listSensorTrayComments")
        self.leSensorTrayLocation = QtWidgets.QLineEdit(self.frame_4)
        self.leSensorTrayLocation.setGeometry(QtCore.QRect(70, 40, 151, 20))
        self.leSensorTrayLocation.setObjectName("leSensorTrayLocation")
        self.pbSensorTrayDeleteComment = QtWidgets.QPushButton(self.frame_4)
        self.pbSensorTrayDeleteComment.setGeometry(QtCore.QRect(160, 70, 131, 21))
        self.pbSensorTrayDeleteComment.setObjectName("pbSensorTrayDeleteComment")
        self.pbSensorTrayCancel = QtWidgets.QPushButton(self.frame_4)
        self.pbSensorTrayCancel.setGeometry(QtCore.QRect(220, 40, 71, 21))
        self.pbSensorTrayCancel.setObjectName("pbSensorTrayCancel")
        self.cbSensorTrayInstitution = QtWidgets.QComboBox(self.frame_4)
        self.cbSensorTrayInstitution.setGeometry(QtCore.QRect(150, 20, 71, 21))
        self.cbSensorTrayInstitution.setObjectName("cbSensorTrayInstitution")
        self.cbSensorTrayInstitution.addItem("")
        self.cbSensorTrayInstitution.setItemText(0, "")
        self.cbSensorTrayInstitution.addItem("")
        self.cbSensorTrayInstitution.addItem("")
        self.cbSensorTrayInstitution.addItem("")
        self.cbSensorTrayInstitution.addItem("")
        self.cbSensorTrayInstitution.addItem("")
        self.cbSensorTrayInstitution.addItem("")
        self.cbSensorTrayInstitution.addItem("")
        self.cbSensorTrayInstitution.addItem("")
        self.cbSensorTrayInstitution.addItem("")
        self.cbSensorTrayInstitution.addItem("")
        self.cbSensorTrayInstitution.addItem("")
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setGeometry(QtCore.QRect(10, 10, 251, 311))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pbSensorToolCancel = QtWidgets.QPushButton(self.frame_5)
        self.pbSensorToolCancel.setGeometry(QtCore.QRect(180, 40, 71, 21))
        self.pbSensorToolCancel.setObjectName("pbSensorToolCancel")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(0, 70, 121, 21))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.leSensorToolLocation = QtWidgets.QLineEdit(self.frame_5)
        self.leSensorToolLocation.setGeometry(QtCore.QRect(70, 40, 111, 20))
        self.leSensorToolLocation.setObjectName("leSensorToolLocation")
        self.sbSensorToolID = QtWidgets.QSpinBox(self.frame_5)
        self.sbSensorToolID.setGeometry(QtCore.QRect(130, 0, 51, 21))
        self.sbSensorToolID.setMaximum(2147483647)
        self.sbSensorToolID.setObjectName("sbSensorToolID")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_21.setGeometry(QtCore.QRect(0, 20, 111, 21))
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.listSensorToolComments = QtWidgets.QListWidget(self.frame_5)
        self.listSensorToolComments.setGeometry(QtCore.QRect(0, 90, 251, 121))
        self.listSensorToolComments.setObjectName("listSensorToolComments")
        self.pbSensorToolSave = QtWidgets.QPushButton(self.frame_5)
        self.pbSensorToolSave.setGeometry(QtCore.QRect(180, 20, 71, 21))
        self.pbSensorToolSave.setObjectName("pbSensorToolSave")
        self.pbSensorToolDeleteComment = QtWidgets.QPushButton(self.frame_5)
        self.pbSensorToolDeleteComment.setGeometry(QtCore.QRect(120, 70, 131, 21))
        self.pbSensorToolDeleteComment.setObjectName("pbSensorToolDeleteComment")
        self.pbSensorToolEditNew = QtWidgets.QPushButton(self.frame_5)
        self.pbSensorToolEditNew.setGeometry(QtCore.QRect(180, 0, 71, 21))
        self.pbSensorToolEditNew.setObjectName("pbSensorToolEditNew")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_16.setGeometry(QtCore.QRect(0, 40, 71, 21))
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.pbSensorToolAddComment = QtWidgets.QPushButton(self.frame_5)
        self.pbSensorToolAddComment.setGeometry(QtCore.QRect(0, 290, 111, 21))
        self.pbSensorToolAddComment.setObjectName("pbSensorToolAddComment")
        self.pteSensorToolWriteComment = QtWidgets.QPlainTextEdit(self.frame_5)
        self.pteSensorToolWriteComment.setGeometry(QtCore.QRect(0, 220, 251, 71))
        self.pteSensorToolWriteComment.setObjectName("pteSensorToolWriteComment")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 131, 21))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.cbSensorToolInstitution = QtWidgets.QComboBox(self.frame_5)
        self.cbSensorToolInstitution.setGeometry(QtCore.QRect(110, 20, 71, 21))
        self.cbSensorToolInstitution.setObjectName("cbSensorToolInstitution")
        self.cbSensorToolInstitution.addItem("")
        self.cbSensorToolInstitution.setItemText(0, "")
        self.cbSensorToolInstitution.addItem("")
        self.cbSensorToolInstitution.addItem("")
        self.cbSensorToolInstitution.addItem("")
        self.cbSensorToolInstitution.addItem("")
        self.cbSensorToolInstitution.addItem("")
        self.cbSensorToolInstitution.addItem("")
        self.cbSensorToolInstitution.addItem("")
        self.cbSensorToolInstitution.addItem("")
        self.cbSensorToolInstitution.addItem("")
        self.cbSensorToolInstitution.addItem("")
        self.cbSensorToolInstitution.addItem("")

        self.retranslateUi(Form)
        self.cbAssemblyTrayInstitution.setCurrentIndex(0)
        self.cbPcbTrayInstitution.setCurrentIndex(0)
        self.cbPcbToolInstitution.setCurrentIndex(0)
        self.cbSensorTrayInstitution.setCurrentIndex(0)
        self.cbSensorToolInstitution.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_23.setText(_translate("Form", "Institution"))
        self.lineEdit_13.setText(_translate("Form", "Comments"))
        self.pbAssemblyTrayDeleteComment.setText(_translate("Form", "delete selected"))
        self.lineEdit_15.setText(_translate("Form", "Assembly Tray"))
        self.pbAssemblyTrayEditNew.setText(_translate("Form", "edit/new"))
        self.pbAssemblyTrayAddComment.setText(_translate("Form", "add comment"))
        self.pbAssemblyTraySave.setText(_translate("Form", "save"))
        self.pbAssemblyTrayCancel.setText(_translate("Form", "cancel"))
        self.lineEdit_18.setText(_translate("Form", "Location"))
        self.cbAssemblyTrayInstitution.setItemText(1, _translate("Form", "CERN"))
        self.cbAssemblyTrayInstitution.setItemText(2, _translate("Form", "FNAL"))
        self.cbAssemblyTrayInstitution.setItemText(3, _translate("Form", "UCSB"))
        self.cbAssemblyTrayInstitution.setItemText(4, _translate("Form", "UMN"))
        self.cbAssemblyTrayInstitution.setItemText(5, _translate("Form", "HEPHY"))
        self.cbAssemblyTrayInstitution.setItemText(6, _translate("Form", "HPK"))
        self.cbAssemblyTrayInstitution.setItemText(7, _translate("Form", "CMU"))
        self.cbAssemblyTrayInstitution.setItemText(8, _translate("Form", "TTU"))
        self.cbAssemblyTrayInstitution.setItemText(9, _translate("Form", "IHEP"))
        self.cbAssemblyTrayInstitution.setItemText(10, _translate("Form", "TIFR"))
        self.cbAssemblyTrayInstitution.setItemText(11, _translate("Form", "NEU"))
        self.pbPcbTrayEditNew.setText(_translate("Form", "edit/new"))
        self.pbPcbTrayCancel.setText(_translate("Form", "cancel"))
        self.lineEdit_20.setText(_translate("Form", "Location"))
        self.lineEdit_25.setText(_translate("Form", "Institution"))
        self.lineEdit_8.setText(_translate("Form", "Comments"))
        self.pbPcbTrayAddComment.setText(_translate("Form", "add comment"))
        self.pbPcbTrayDeleteComment.setText(_translate("Form", "delete selected"))
        self.lineEdit_12.setText(_translate("Form", "PCB Component Tray"))
        self.pbPcbTraySave.setText(_translate("Form", "save"))
        self.cbPcbTrayInstitution.setItemText(1, _translate("Form", "CERN"))
        self.cbPcbTrayInstitution.setItemText(2, _translate("Form", "FNAL"))
        self.cbPcbTrayInstitution.setItemText(3, _translate("Form", "UCSB"))
        self.cbPcbTrayInstitution.setItemText(4, _translate("Form", "UMN"))
        self.cbPcbTrayInstitution.setItemText(5, _translate("Form", "HEPHY"))
        self.cbPcbTrayInstitution.setItemText(6, _translate("Form", "HPK"))
        self.cbPcbTrayInstitution.setItemText(7, _translate("Form", "CMU"))
        self.cbPcbTrayInstitution.setItemText(8, _translate("Form", "TTU"))
        self.cbPcbTrayInstitution.setItemText(9, _translate("Form", "IHEP"))
        self.cbPcbTrayInstitution.setItemText(10, _translate("Form", "TIFR"))
        self.cbPcbTrayInstitution.setItemText(11, _translate("Form", "NEU"))
        self.pbPcbToolSave.setText(_translate("Form", "save"))
        self.lineEdit_5.setText(_translate("Form", "PCB tool"))
        self.pbPcbToolCancel.setText(_translate("Form", "cancel"))
        self.pbPcbToolDeleteComment.setText(_translate("Form", "delete selected"))
        self.lineEdit_24.setText(_translate("Form", "Institution"))
        self.pbPcbToolAddComment.setText(_translate("Form", "add comment"))
        self.lineEdit_4.setText(_translate("Form", "Comments"))
        self.pbPcbToolEditNew.setText(_translate("Form", "edit/new"))
        self.lineEdit_19.setText(_translate("Form", "Location"))
        self.cbPcbToolInstitution.setItemText(1, _translate("Form", "CERN"))
        self.cbPcbToolInstitution.setItemText(2, _translate("Form", "FNAL"))
        self.cbPcbToolInstitution.setItemText(3, _translate("Form", "UCSB"))
        self.cbPcbToolInstitution.setItemText(4, _translate("Form", "UMN"))
        self.cbPcbToolInstitution.setItemText(5, _translate("Form", "HEPHY"))
        self.cbPcbToolInstitution.setItemText(6, _translate("Form", "HPK"))
        self.cbPcbToolInstitution.setItemText(7, _translate("Form", "CMU"))
        self.cbPcbToolInstitution.setItemText(8, _translate("Form", "TTU"))
        self.cbPcbToolInstitution.setItemText(9, _translate("Form", "IHEP"))
        self.cbPcbToolInstitution.setItemText(10, _translate("Form", "TIFR"))
        self.cbPcbToolInstitution.setItemText(11, _translate("Form", "NEU"))
        self.lineEdit_22.setText(_translate("Form", "Institution"))
        self.pbSensorTrayAddComment.setText(_translate("Form", "add comment"))
        self.lineEdit_9.setText(_translate("Form", "Comments"))
        self.lineEdit_10.setText(_translate("Form", "Sensor Component Tray"))
        self.lineEdit_17.setText(_translate("Form", "Location"))
        self.pbSensorTrayEditNew.setText(_translate("Form", "edit/new"))
        self.pbSensorTraySave.setText(_translate("Form", "save"))
        self.pbSensorTrayDeleteComment.setText(_translate("Form", "delete selected"))
        self.pbSensorTrayCancel.setText(_translate("Form", "cancel"))
        self.cbSensorTrayInstitution.setItemText(1, _translate("Form", "CERN"))
        self.cbSensorTrayInstitution.setItemText(2, _translate("Form", "FNAL"))
        self.cbSensorTrayInstitution.setItemText(3, _translate("Form", "UCSB"))
        self.cbSensorTrayInstitution.setItemText(4, _translate("Form", "UMN"))
        self.cbSensorTrayInstitution.setItemText(5, _translate("Form", "HEPHY"))
        self.cbSensorTrayInstitution.setItemText(6, _translate("Form", "HPK"))
        self.cbSensorTrayInstitution.setItemText(7, _translate("Form", "CMU"))
        self.cbSensorTrayInstitution.setItemText(8, _translate("Form", "TTU"))
        self.cbSensorTrayInstitution.setItemText(9, _translate("Form", "IHEP"))
        self.cbSensorTrayInstitution.setItemText(10, _translate("Form", "TIFR"))
        self.cbSensorTrayInstitution.setItemText(11, _translate("Form", "NEU"))
        self.pbSensorToolCancel.setText(_translate("Form", "cancel"))
        self.lineEdit_3.setText(_translate("Form", "Comments"))
        self.lineEdit_21.setText(_translate("Form", "Institution"))
        self.pbSensorToolSave.setText(_translate("Form", "save"))
        self.pbSensorToolDeleteComment.setText(_translate("Form", "delete selected"))
        self.pbSensorToolEditNew.setText(_translate("Form", "edit/new"))
        self.lineEdit_16.setText(_translate("Form", "Location"))
        self.pbSensorToolAddComment.setText(_translate("Form", "add comment"))
        self.lineEdit.setText(_translate("Form", "Sensor tool"))
        self.cbSensorToolInstitution.setItemText(1, _translate("Form", "CERN"))
        self.cbSensorToolInstitution.setItemText(2, _translate("Form", "FNAL"))
        self.cbSensorToolInstitution.setItemText(3, _translate("Form", "UCSB"))
        self.cbSensorToolInstitution.setItemText(4, _translate("Form", "UMN"))
        self.cbSensorToolInstitution.setItemText(5, _translate("Form", "HEPHY"))
        self.cbSensorToolInstitution.setItemText(6, _translate("Form", "HPK"))
        self.cbSensorToolInstitution.setItemText(7, _translate("Form", "CMU"))
        self.cbSensorToolInstitution.setItemText(8, _translate("Form", "TTU"))
        self.cbSensorToolInstitution.setItemText(9, _translate("Form", "IHEP"))
        self.cbSensorToolInstitution.setItemText(10, _translate("Form", "TIFR"))
        self.cbSensorToolInstitution.setItemText(11, _translate("Form", "NEU"))
