# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore

# Form implementation generated from reading ui file 'designer//table_reduction_runs_editor.ui'
#
# Created: Wed Nov  4 10:29:21 2015
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.lambdaValue = QtGui.QLabel(self.centralwidget)
        self.lambdaValue.setObjectName("lambdaValue")
        self.horizontalLayout_7.addWidget(self.lambdaValue)
        self.lambdaUnits = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lambdaUnits.setFont(font)
        self.lambdaUnits.setObjectName("lambdaUnits")
        self.horizontalLayout_7.addWidget(self.lambdaUnits)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.data_groupBox = QtGui.QGroupBox(self.centralwidget)
        self.data_groupBox.setObjectName("data_groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.data_groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dataLineEdit = QtGui.QLineEdit(self.data_groupBox)
        self.dataLineEdit.setObjectName("dataLineEdit")
        self.horizontalLayout.addWidget(self.dataLineEdit)
        self.label_2 = QtGui.QLabel(self.data_groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(self.data_groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.oldDataRun = QtGui.QLabel(self.data_groupBox)
        self.oldDataRun.setObjectName("oldDataRun")
        self.horizontalLayout_2.addWidget(self.oldDataRun)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtGui.QLabel(self.data_groupBox)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.normRun = QtGui.QLabel(self.data_groupBox)
        self.normRun.setObjectName("normRun")
        self.horizontalLayout_3.addWidget(self.normRun)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.data_groupBox)
        self.norm_groupBox = QtGui.QGroupBox(self.centralwidget)
        self.norm_groupBox.setObjectName("norm_groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.norm_groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_14 = QtGui.QLabel(self.norm_groupBox)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.dataRun = QtGui.QLabel(self.norm_groupBox)
        self.dataRun.setObjectName("dataRun")
        self.horizontalLayout_4.addWidget(self.dataRun)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.normLineEdit = QtGui.QLineEdit(self.norm_groupBox)
        self.normLineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.normLineEdit.setStatusTip("")
        self.normLineEdit.setWhatsThis("")
        self.normLineEdit.setAccessibleName("")
        self.normLineEdit.setAccessibleDescription("")
        self.normLineEdit.setInputMask("")
        self.normLineEdit.setText("")
        self.normLineEdit.setObjectName("normLineEdit")
        self.horizontalLayout_10.addWidget(self.normLineEdit)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_21 = QtGui.QLabel(self.norm_groupBox)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_5.addWidget(self.label_21)
        self.oldNormRun = QtGui.QLabel(self.norm_groupBox)
        self.oldNormRun.setObjectName("oldNormRun")
        self.horizontalLayout_5.addWidget(self.oldNormRun)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addWidget(self.norm_groupBox)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtGui.QTableWidget(self.groupBox_3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.validRunLabel = QtGui.QLabel(self.groupBox_3)
        self.validRunLabel.setObjectName("validRunLabel")
        self.horizontalLayout_8.addWidget(self.validRunLabel)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.invalidRunLabel = QtGui.QLabel(self.groupBox_3)
        self.invalidRunLabel.setObjectName("invalidRunLabel")
        self.horizontalLayout_8.addWidget(self.invalidRunLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_6.addWidget(self.cancelButton)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.insertValidRunsButton = QtGui.QPushButton(self.centralwidget)
        self.insertValidRunsButton.setEnabled(False)
        self.insertValidRunsButton.setObjectName("insertValidRunsButton")
        self.horizontalLayout_6.addWidget(self.insertValidRunsButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), MainWindow.closeEvent)
        QtCore.QObject.connect(self.dataLineEdit, QtCore.SIGNAL("returnPressed()"), MainWindow.dataLineEditValidate)
        QtCore.QObject.connect(self.insertValidRunsButton, QtCore.SIGNAL("pressed()"), MainWindow.insertValidRunsButton)
        QtCore.QObject.connect(self.normLineEdit, QtCore.SIGNAL("returnPressed()"), MainWindow.normLineEditValidate)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Lambda requested:", None, QtGui.QApplication.UnicodeUTF8))
        self.lambdaValue.setText(QtGui.QApplication.translate("MainWindow", "10.5", None, QtGui.QApplication.UnicodeUTF8))
        self.lambdaUnits.setText(QtGui.QApplication.translate("MainWindow", "Angstroms", None, QtGui.QApplication.UnicodeUTF8))
        self.data_groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "New Data Run(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.dataLineEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "Enter Data Runs and Hit ENTER", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "ex: 10,15-20", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Old data run(s):", None, QtGui.QApplication.UnicodeUTF8))
        self.oldDataRun.setText(QtGui.QApplication.translate("MainWindow", "13445,45454,3454545", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Normalization run:", None, QtGui.QApplication.UnicodeUTF8))
        self.normRun.setText(QtGui.QApplication.translate("MainWindow", "4545545", None, QtGui.QApplication.UnicodeUTF8))
        self.norm_groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "New Normalization Run", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "Data run(s):", None, QtGui.QApplication.UnicodeUTF8))
        self.dataRun.setText(QtGui.QApplication.translate("MainWindow", "4545545,4545454,45454", None, QtGui.QApplication.UnicodeUTF8))
        self.normLineEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "Enter Normalization Run and Hit ENTER", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainWindow", "Old normalization  run:", None, QtGui.QApplication.UnicodeUTF8))
        self.oldNormRun.setText(QtGui.QApplication.translate("MainWindow", "13445", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Checking Matching Lambdas", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Lambda Requested", None, QtGui.QApplication.UnicodeUTF8))
        self.validRunLabel.setText(QtGui.QApplication.translate("MainWindow", "Valid Run (Matching Lambda Requested)", None, QtGui.QApplication.UnicodeUTF8))
        self.invalidRunLabel.setText(QtGui.QApplication.translate("MainWindow", "Invalid Run (No Matching Lambda Requested) ", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("MainWindow", "CANCEL", None, QtGui.QApplication.UnicodeUTF8))
        self.insertValidRunsButton.setText(QtGui.QApplication.translate("MainWindow", "INSERT VALID RUNS", None, QtGui.QApplication.UnicodeUTF8))

