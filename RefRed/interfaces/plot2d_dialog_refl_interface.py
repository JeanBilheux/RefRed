# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore

# Form implementation generated from reading ui file 'designer//plot2d_dialog_refl_interface.ui'
#
# Created: Thu Sep 17 12:42:54 2015
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1379, 1188)
        self.verticalLayout_4 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.y_pixel_vs_tof_plot = MPLWidgetNoLog(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_pixel_vs_tof_plot.sizePolicy().hasHeightForWidth())
        self.y_pixel_vs_tof_plot.setSizePolicy(sizePolicy)
        self.y_pixel_vs_tof_plot.setObjectName(_fromUtf8("y_pixel_vs_tof_plot"))
        self.horizontalLayout.addWidget(self.y_pixel_vs_tof_plot)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_37 = QtGui.QHBoxLayout()
        self.horizontalLayout_37.setObjectName(_fromUtf8("horizontalLayout_37"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_37.addItem(spacerItem)
        self.dataTOFmanualLabel = QtGui.QLabel(self.tab)
        self.dataTOFmanualLabel.setEnabled(True)
        self.dataTOFmanualLabel.setObjectName(_fromUtf8("dataTOFmanualLabel"))
        self.horizontalLayout_37.addWidget(self.dataTOFmanualLabel)
        self.frame_13 = QtGui.QFrame(self.tab)
        self.frame_13.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_13.setLineWidth(0)
        self.frame_13.setObjectName(_fromUtf8("frame_13"))
        self.horizontalLayout_38 = QtGui.QHBoxLayout(self.frame_13)
        self.horizontalLayout_38.setObjectName(_fromUtf8("horizontalLayout_38"))
        self.horizontalLayout_39 = QtGui.QHBoxLayout()
        self.horizontalLayout_39.setObjectName(_fromUtf8("horizontalLayout_39"))
        self.tof_auto_flag = QtGui.QRadioButton(self.frame_13)
        self.tof_auto_flag.setChecked(True)
        self.tof_auto_flag.setAutoExclusive(True)
        self.tof_auto_flag.setObjectName(_fromUtf8("tof_auto_flag"))
        self.horizontalLayout_39.addWidget(self.tof_auto_flag)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_39.addItem(spacerItem1)
        self.tof_manual_flag = QtGui.QRadioButton(self.frame_13)
        self.tof_manual_flag.setEnabled(True)
        self.tof_manual_flag.setAutoExclusive(True)
        self.tof_manual_flag.setObjectName(_fromUtf8("tof_manual_flag"))
        self.horizontalLayout_39.addWidget(self.tof_manual_flag)
        self.horizontalLayout_38.addLayout(self.horizontalLayout_39)
        self.horizontalLayout_37.addWidget(self.frame_13)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_37.addItem(spacerItem2)
        self.tof_from_label = QtGui.QLabel(self.tab)
        self.tof_from_label.setEnabled(False)
        self.tof_from_label.setObjectName(_fromUtf8("tof_from_label"))
        self.horizontalLayout_37.addWidget(self.tof_from_label)
        self.tof_from = QtGui.QLineEdit(self.tab)
        self.tof_from.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tof_from.sizePolicy().hasHeightForWidth())
        self.tof_from.setSizePolicy(sizePolicy)
        self.tof_from.setMinimumSize(QtCore.QSize(100, 0))
        self.tof_from.setMaximumSize(QtCore.QSize(100, 16777215))
        self.tof_from.setObjectName(_fromUtf8("tof_from"))
        self.horizontalLayout_37.addWidget(self.tof_from)
        self.tof_from_units = QtGui.QLabel(self.tab)
        self.tof_from_units.setEnabled(False)
        self.tof_from_units.setObjectName(_fromUtf8("tof_from_units"))
        self.horizontalLayout_37.addWidget(self.tof_from_units)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_37.addItem(spacerItem3)
        self.tof_to_label = QtGui.QLabel(self.tab)
        self.tof_to_label.setEnabled(False)
        self.tof_to_label.setObjectName(_fromUtf8("tof_to_label"))
        self.horizontalLayout_37.addWidget(self.tof_to_label)
        self.tof_to = QtGui.QLineEdit(self.tab)
        self.tof_to.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tof_to.sizePolicy().hasHeightForWidth())
        self.tof_to.setSizePolicy(sizePolicy)
        self.tof_to.setMinimumSize(QtCore.QSize(100, 0))
        self.tof_to.setMaximumSize(QtCore.QSize(100, 16777215))
        self.tof_to.setObjectName(_fromUtf8("tof_to"))
        self.horizontalLayout_37.addWidget(self.tof_to)
        self.tof_to_units = QtGui.QLabel(self.tab)
        self.tof_to_units.setEnabled(False)
        self.tof_to_units.setObjectName(_fromUtf8("tof_to_units"))
        self.horizontalLayout_37.addWidget(self.tof_to_units)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_37.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_37)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.detector_plot = MPLWidgetNoLog(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.detector_plot.sizePolicy().hasHeightForWidth())
        self.detector_plot.setSizePolicy(sizePolicy)
        self.detector_plot.setObjectName(_fromUtf8("detector_plot"))
        self.horizontalLayout_2.addWidget(self.detector_plot)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.frame_20 = QtGui.QFrame(self.tab_2)
        self.frame_20.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_20.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_20.setObjectName(_fromUtf8("frame_20"))
        self.horizontalLayout_54 = QtGui.QHBoxLayout(self.frame_20)
        self.horizontalLayout_54.setObjectName(_fromUtf8("horizontalLayout_54"))
        self.horizontalLayout_83 = QtGui.QHBoxLayout()
        self.horizontalLayout_83.setObjectName(_fromUtf8("horizontalLayout_83"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_83.addItem(spacerItem5)
        self.low_res_flag = QtGui.QCheckBox(self.frame_20)
        self.low_res_flag.setChecked(True)
        self.low_res_flag.setObjectName(_fromUtf8("low_res_flag"))
        self.horizontalLayout_83.addWidget(self.low_res_flag)
        self.low_res1_label = QtGui.QLabel(self.frame_20)
        self.low_res1_label.setObjectName(_fromUtf8("low_res1_label"))
        self.horizontalLayout_83.addWidget(self.low_res1_label)
        spacerItem6 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_83.addItem(spacerItem6)
        self.low_res1 = QtGui.QSpinBox(self.frame_20)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.low_res1.setPalette(palette)
        self.low_res1.setMaximum(255)
        self.low_res1.setProperty("value", 50)
        self.low_res1.setObjectName(_fromUtf8("low_res1"))
        self.horizontalLayout_83.addWidget(self.low_res1)
        self.low_res2_label = QtGui.QLabel(self.frame_20)
        self.low_res2_label.setObjectName(_fromUtf8("low_res2_label"))
        self.horizontalLayout_83.addWidget(self.low_res2_label)
        spacerItem7 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_83.addItem(spacerItem7)
        self.low_res2 = QtGui.QSpinBox(self.frame_20)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.low_res2.setPalette(palette)
        self.low_res2.setMaximum(303)
        self.low_res2.setProperty("value", 250)
        self.low_res2.setObjectName(_fromUtf8("low_res2"))
        self.horizontalLayout_83.addWidget(self.low_res2)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_83.addItem(spacerItem8)
        self.horizontalLayout_54.addLayout(self.horizontalLayout_83)
        self.verticalLayout_2.addWidget(self.frame_20)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.tabWidget)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.frame = QtGui.QFrame(self.groupBox_4)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem9)
        self.peak2_label = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.peak2_label.setFont(font)
        self.peak2_label.setAccessibleDescription(_fromUtf8(""))
        self.peak2_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.peak2_label.setObjectName(_fromUtf8("peak2_label"))
        self.verticalLayout_13.addWidget(self.peak2_label)
        self.peak2 = QtGui.QSpinBox(self.frame)
        self.peak2.setMaximum(303)
        self.peak2.setObjectName(_fromUtf8("peak2"))
        self.verticalLayout_13.addWidget(self.peak2)
        self.horizontalLayout_15.addLayout(self.verticalLayout_13)
        self.verticalLayout_12.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.peak1 = QtGui.QSpinBox(self.frame)
        self.peak1.setMaximum(303)
        self.peak1.setObjectName(_fromUtf8("peak1"))
        self.verticalLayout_14.addWidget(self.peak1)
        self.peak1_label = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.peak1_label.setFont(font)
        self.peak1_label.setAccessibleDescription(_fromUtf8(""))
        self.peak1_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.peak1_label.setObjectName(_fromUtf8("peak1_label"))
        self.verticalLayout_14.addWidget(self.peak1_label)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem10)
        self.horizontalLayout_16.addLayout(self.verticalLayout_14)
        self.verticalLayout_12.addLayout(self.horizontalLayout_16)
        self.verticalLayout_11.addWidget(self.frame)
        self.horizontalLayout_4.addWidget(self.groupBox_4)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.back_flag = QtGui.QCheckBox(self.groupBox_3)
        self.back_flag.setObjectName(_fromUtf8("back_flag"))
        self.verticalLayout_8.addWidget(self.back_flag)
        self.frame_2 = QtGui.QFrame(self.groupBox_3)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem11)
        self.back2_label = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.back2_label.setFont(font)
        self.back2_label.setAccessibleDescription(_fromUtf8(""))
        self.back2_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.back2_label.setObjectName(_fromUtf8("back2_label"))
        self.verticalLayout_9.addWidget(self.back2_label)
        self.back2 = QtGui.QSpinBox(self.frame_2)
        self.back2.setMaximum(303)
        self.back2.setObjectName(_fromUtf8("back2"))
        self.verticalLayout_9.addWidget(self.back2)
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem12)
        self.horizontalLayout_13.addLayout(self.verticalLayout_9)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        spacerItem13 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem13)
        self.back1 = QtGui.QSpinBox(self.frame_2)
        self.back1.setMaximum(303)
        self.back1.setObjectName(_fromUtf8("back1"))
        self.verticalLayout_10.addWidget(self.back1)
        self.back1_label = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.back1_label.setFont(font)
        self.back1_label.setAccessibleDescription(_fromUtf8(""))
        self.back1_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.back1_label.setObjectName(_fromUtf8("back1_label"))
        self.verticalLayout_10.addWidget(self.back1_label)
        spacerItem14 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem14)
        self.horizontalLayout_14.addLayout(self.verticalLayout_10)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        self.verticalLayout_8.addWidget(self.frame_2)
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.error_label = QtGui.QLabel(Dialog)
        self.error_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.error_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.error_label.setObjectName(_fromUtf8("error_label"))
        self.verticalLayout_3.addWidget(self.error_label)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.back_flag, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Dialog.activate_or_not_back_widgets)
        QtCore.QObject.connect(self.peak1, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Dialog.manual_input_peak1)
        QtCore.QObject.connect(self.peak2, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Dialog.manual_input_peak2)
        QtCore.QObject.connect(self.back1, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Dialog.manual_input_back1)
        QtCore.QObject.connect(self.back2, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Dialog.manual_input_back2)
        QtCore.QObject.connect(self.tof_from, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Dialog.manual_input_of_tof_field)
        QtCore.QObject.connect(self.low_res2, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Dialog.manual_input_of_low_res_field)
        QtCore.QObject.connect(self.tof_manual_flag, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.manual_auto_tof_clicked)
        QtCore.QObject.connect(self.low_res_flag, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Dialog.activate_or_not_low_res_widgets)
        QtCore.QObject.connect(self.low_res1, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Dialog.manual_input_of_low_res_field)
        QtCore.QObject.connect(self.tof_to, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Dialog.manual_input_of_tof_field)
        QtCore.QObject.connect(self.tof_auto_flag, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.manual_auto_tof_clicked)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "2D Selection Tool", None))
        self.dataTOFmanualLabel.setText(_translate("Dialog", "TOF range", None))
        self.tof_auto_flag.setText(_translate("Dialog", "Auto", None))
        self.tof_manual_flag.setText(_translate("Dialog", "Manual", None))
        self.tof_from_label.setText(_translate("Dialog", "from", None))
        self.tof_from.setText(_translate("Dialog", "0", None))
        self.tof_from_units.setText(_translate("Dialog", "ms", None))
        self.tof_to_label.setText(_translate("Dialog", "to", None))
        self.tof_to.setText(_translate("Dialog", "200", None))
        self.tof_to_units.setText(_translate("Dialog", "ms", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Y Pixel vs TOF", None))
        self.low_res_flag.setText(_translate("Dialog", "Low Resolution", None))
        self.low_res1_label.setText(_translate("Dialog", "From Pixel", None))
        self.low_res2_label.setText(_translate("Dialog", "To Pixel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Y pixel vs X pixel", None))
        self.groupBox_4.setTitle(_translate("Dialog", "PEAK", None))
        self.peak2_label.setText(_translate("Dialog", "*", None))
        self.peak1_label.setText(_translate("Dialog", "*", None))
        self.groupBox_3.setTitle(_translate("Dialog", "BACKGROUND", None))
        self.back_flag.setText(_translate("Dialog", "with Back.", None))
        self.back2_label.setText(_translate("Dialog", "*", None))
        self.back1_label.setText(_translate("Dialog", "*", None))
        self.error_label.setText(_translate("Dialog", "(*) INVALID SELECTION", None))

from mplwidgetnolog import MPLWidgetNoLog
import icons_rc
