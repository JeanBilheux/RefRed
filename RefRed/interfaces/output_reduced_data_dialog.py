# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore

# Form implementation generated from reading ui file 'designer//output_reduced_data_dialog.ui'
#
# Created: Tue Feb 16 16:36:42 2016
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(544, 541)
        Dialog.setMinimumSize(QtCore.QSize(0, 500))
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.output4thColumnFlag = QtGui.QCheckBox(Dialog)
        self.output4thColumnFlag.setObjectName("output4thColumnFlag")
        self.verticalLayout.addWidget(self.output4thColumnFlag)
        self.frame_2 = QtGui.QFrame(Dialog)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.auto_qmin_button = QtGui.QRadioButton(self.frame_2)
        self.auto_qmin_button.setChecked(True)
        self.auto_qmin_button.setObjectName("auto_qmin_button")
        self.horizontalLayout_3.addWidget(self.auto_qmin_button)
        self.manual_qmin_frame = QtGui.QFrame(self.frame_2)
        self.manual_qmin_frame.setEnabled(False)
        self.manual_qmin_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.manual_qmin_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.manual_qmin_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.manual_qmin_frame.setObjectName("manual_qmin_frame")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.manual_qmin_frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtGui.QLabel(self.manual_qmin_frame)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.manual_qmin_value = QtGui.QLineEdit(self.manual_qmin_frame)
        self.manual_qmin_value.setMaximumSize(QtCore.QSize(16777215, 27))
        self.manual_qmin_value.setObjectName("manual_qmin_value")
        self.horizontalLayout_5.addWidget(self.manual_qmin_value)
        self.label_6 = QtGui.QLabel(self.manual_qmin_frame)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.horizontalLayout_3.addWidget(self.manual_qmin_frame)
        self.verticalLayout.addWidget(self.frame_2)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.dq0Value = QtGui.QLineEdit(self.groupBox)
        self.dq0Value.setObjectName("dq0Value")
        self.horizontalLayout.addWidget(self.dq0Value)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.dQoverQvalue = QtGui.QLineEdit(self.groupBox)
        self.dQoverQvalue.setObjectName("dQoverQvalue")
        self.horizontalLayout_2.addWidget(self.dQoverQvalue)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.usingLessErrorValueFlag = QtGui.QRadioButton(self.groupBox_3)
        self.usingLessErrorValueFlag.setChecked(True)
        self.usingLessErrorValueFlag.setObjectName("usingLessErrorValueFlag")
        self.verticalLayout_3.addWidget(self.usingLessErrorValueFlag)
        self.usingMeanValueFalg = QtGui.QRadioButton(self.groupBox_3)
        self.usingMeanValueFalg.setObjectName("usingMeanValueFalg")
        self.verticalLayout_3.addWidget(self.usingMeanValueFalg)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.one_ascii_format = QtGui.QRadioButton(self.groupBox_2)
        self.one_ascii_format.setChecked(True)
        self.one_ascii_format.setObjectName("one_ascii_format")
        self.verticalLayout_4.addWidget(self.one_ascii_format)
        self.n_ascii_format = QtGui.QRadioButton(self.groupBox_2)
        self.n_ascii_format.setObjectName("n_ascii_format")
        self.verticalLayout_4.addWidget(self.n_ascii_format)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.base_name_label = QtGui.QLabel(self.groupBox_2)
        self.base_name_label.setEnabled(False)
        self.base_name_label.setObjectName("base_name_label")
        self.horizontalLayout_4.addWidget(self.base_name_label)
        self.prefix_name_value = QtGui.QLineEdit(self.groupBox_2)
        self.prefix_name_value.setEnabled(False)
        self.prefix_name_value.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.prefix_name_value.setObjectName("prefix_name_value")
        self.horizontalLayout_4.addWidget(self.prefix_name_value)
        self.run_name_label = QtGui.QLabel(self.groupBox_2)
        self.run_name_label.setEnabled(False)
        self.run_name_label.setObjectName("run_name_label")
        self.horizontalLayout_4.addWidget(self.run_name_label)
        self.suffix_name_value = QtGui.QLineEdit(self.groupBox_2)
        self.suffix_name_value.setEnabled(False)
        self.suffix_name_value.setObjectName("suffix_name_value")
        self.horizontalLayout_4.addWidget(self.suffix_name_value)
        self.ext_name_label = QtGui.QLabel(self.groupBox_2)
        self.ext_name_label.setEnabled(False)
        self.ext_name_label.setObjectName("ext_name_label")
        self.horizontalLayout_4.addWidget(self.ext_name_label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.createAsciiButton = QtGui.QPushButton(Dialog)
        self.createAsciiButton.setObjectName("createAsciiButton")
        self.verticalLayout.addWidget(self.createAsciiButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.folder_error = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folder_error.sizePolicy().hasHeightForWidth())
        self.folder_error.setSizePolicy(sizePolicy)
        self.folder_error.setMaximumSize(QtCore.QSize(16777215, 25))
        self.folder_error.setAlignment(QtCore.Qt.AlignCenter)
        self.folder_error.setObjectName("folder_error")
        self.verticalLayout_2.addWidget(self.folder_error)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.createAsciiButton, QtCore.SIGNAL("clicked()"), Dialog.create_reduce_ascii_button_event)
        QtCore.QObject.connect(self.one_ascii_format, QtCore.SIGNAL("clicked()"), Dialog.output_format_radio_buttons_event)
        QtCore.QObject.connect(self.n_ascii_format, QtCore.SIGNAL("clicked()"), Dialog.output_format_radio_buttons_event)
        QtCore.QObject.connect(self.auto_qmin_button, QtCore.SIGNAL("clicked(bool)"), Dialog.auto_qmin_button)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Export ASCII", None, QtGui.QApplication.UnicodeUTF8))
        self.output4thColumnFlag.setText(QtGui.QApplication.translate("Dialog", "with 4th column (precision)", None, QtGui.QApplication.UnicodeUTF8))
        self.auto_qmin_button.setText(QtGui.QApplication.translate("Dialog", "Auto Qmin", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Qmin", None, QtGui.QApplication.UnicodeUTF8))
        self.manual_qmin_value.setText(QtGui.QApplication.translate("Dialog", "0.005", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "1/Å", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">dQ<span style=\" vertical-align:sub;\">0</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.dq0Value.setText(QtGui.QApplication.translate("Dialog", "0.0004", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "1/Å", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ΔQ<span style=\" vertical-align:sub;\">1</span>/Q</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.dQoverQvalue.setText(QtGui.QApplication.translate("Dialog", "0.005", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Dialog", "  How to treat overlap values", None, QtGui.QApplication.UnicodeUTF8))
        self.usingLessErrorValueFlag.setText(QtGui.QApplication.translate("Dialog", "use lowest error value", None, QtGui.QApplication.UnicodeUTF8))
        self.usingMeanValueFalg.setText(QtGui.QApplication.translate("Dialog", "use mean value", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "  Output format", None, QtGui.QApplication.UnicodeUTF8))
        self.one_ascii_format.setText(QtGui.QApplication.translate("Dialog", "1 Ascii File for All Reduced Data Set", None, QtGui.QApplication.UnicodeUTF8))
        self.n_ascii_format.setText(QtGui.QApplication.translate("Dialog", "n Ascii Files (one for Each Reduced Data Set)", None, QtGui.QApplication.UnicodeUTF8))
        self.base_name_label.setText(QtGui.QApplication.translate("Dialog", "Base Filenames:", None, QtGui.QApplication.UnicodeUTF8))
        self.prefix_name_value.setText(QtGui.QApplication.translate("Dialog", "REF_L_", None, QtGui.QApplication.UnicodeUTF8))
        self.run_name_label.setText(QtGui.QApplication.translate("Dialog", "_###_", None, QtGui.QApplication.UnicodeUTF8))
        self.suffix_name_value.setText(QtGui.QApplication.translate("Dialog", "reduced_data", None, QtGui.QApplication.UnicodeUTF8))
        self.ext_name_label.setText(QtGui.QApplication.translate("Dialog", ".txt", None, QtGui.QApplication.UnicodeUTF8))
        self.createAsciiButton.setText(QtGui.QApplication.translate("Dialog", "Create Ascii File ...", None, QtGui.QApplication.UnicodeUTF8))
        self.folder_error.setText(QtGui.QApplication.translate("Dialog", "CHECK FOLDER PERMISSION !", None, QtGui.QApplication.UnicodeUTF8))

