# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore

# Form implementation generated from reading ui file 'designer//metadata_finder_interface.ui'
#
# Created: Thu Feb 18 16:17:43 2016
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
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.runNumberEdit = QtGui.QLineEdit(self.centralwidget)
        self.runNumberEdit.setText("")
        self.runNumberEdit.setObjectName("runNumberEdit")
        self.horizontalLayout.addWidget(self.runNumberEdit)
        self.inputErrorLabel = QtGui.QLabel(self.centralwidget)
        self.inputErrorLabel.setEnabled(True)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.inputErrorLabel.setFont(font)
        self.inputErrorLabel.setObjectName("inputErrorLabel")
        self.horizontalLayout.addWidget(self.inputErrorLabel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.searchLabel = QtGui.QLabel(self.centralwidget)
        self.searchLabel.setObjectName("searchLabel")
        self.horizontalLayout.addWidget(self.searchLabel)
        self.searchLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.horizontalLayout.addWidget(self.searchLineEdit)
        self.clearButton = QtGui.QPushButton(self.centralwidget)
        self.clearButton.setText("")
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.metadataTable = QtGui.QTableWidget(self.tab)
        self.metadataTable.setObjectName("metadataTable")
        self.metadataTable.setColumnCount(2)
        self.metadataTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.metadataTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.metadataTable.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.metadataTable)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.saveAsciiButton = QtGui.QPushButton(self.tab)
        self.saveAsciiButton.setObjectName("saveAsciiButton")
        self.horizontalLayout_3.addWidget(self.saveAsciiButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.configureTable = QtGui.QTableWidget(self.tab_2)
        self.configureTable.setObjectName("configureTable")
        self.configureTable.setColumnCount(4)
        self.configureTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.configureTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.configureTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.configureTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.configureTable.setHorizontalHeaderItem(3, item)
        self.verticalLayout_3.addWidget(self.configureTable)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.unselectAll = QtGui.QPushButton(self.tab_2)
        self.unselectAll.setEnabled(False)
        self.unselectAll.setObjectName("unselectAll")
        self.horizontalLayout_2.addWidget(self.unselectAll)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.exportConfiguration = QtGui.QPushButton(self.tab_2)
        self.exportConfiguration.setEnabled(False)
        self.exportConfiguration.setObjectName("exportConfiguration")
        self.horizontalLayout_2.addWidget(self.exportConfiguration)
        self.importConfiguration = QtGui.QPushButton(self.tab_2)
        self.importConfiguration.setEnabled(False)
        self.importConfiguration.setObjectName("importConfiguration")
        self.horizontalLayout_2.addWidget(self.importConfiguration)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.runNumberEdit, QtCore.SIGNAL("returnPressed()"), MainWindow.runNumberEditEvent)
        QtCore.QObject.connect(self.unselectAll, QtCore.SIGNAL("clicked()"), MainWindow.unselectAll)
        QtCore.QObject.connect(self.exportConfiguration, QtCore.SIGNAL("clicked()"), MainWindow.exportConfiguration)
        QtCore.QObject.connect(self.importConfiguration, QtCore.SIGNAL("clicked()"), MainWindow.importConfiguration)
        QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL("currentChanged(int)"), MainWindow.userChangedTab)
        QtCore.QObject.connect(self.saveAsciiButton, QtCore.SIGNAL("clicked()"), MainWindow.saveMetadataListAsAsciiFile)
        QtCore.QObject.connect(self.searchLineEdit, QtCore.SIGNAL("textEdited(QString)"), MainWindow.searchLineEditLive)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL("clicked()"), MainWindow.searchLineEditClear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Run(s) number:", None, QtGui.QApplication.UnicodeUTF8))
        self.runNumberEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "1234 or 1234,1236 or 1234-1238", None, QtGui.QApplication.UnicodeUTF8))
        self.inputErrorLabel.setText(QtGui.QApplication.translate("MainWindow", "ERROR WHILE PARSING ! CHECK YOUR INPUT  ", None, QtGui.QApplication.UnicodeUTF8))
        self.searchLabel.setText(QtGui.QApplication.translate("MainWindow", "loop", None, QtGui.QApplication.UnicodeUTF8))
        self.metadataTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Run #", None, QtGui.QApplication.UnicodeUTF8))
        self.metadataTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "IPTS", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAsciiButton.setText(QtGui.QApplication.translate("MainWindow", "Save List as ASCII ...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Metadata", None, QtGui.QApplication.UnicodeUTF8))
        self.configureTable.setSortingEnabled(True)
        self.configureTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Display ?", None, QtGui.QApplication.UnicodeUTF8))
        self.configureTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.configureTable.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.configureTable.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Units", None, QtGui.QApplication.UnicodeUTF8))
        self.unselectAll.setText(QtGui.QApplication.translate("MainWindow", "Unselect All", None, QtGui.QApplication.UnicodeUTF8))
        self.exportConfiguration.setText(QtGui.QApplication.translate("MainWindow", "Export Configuration ...", None, QtGui.QApplication.UnicodeUTF8))
        self.importConfiguration.setText(QtGui.QApplication.translate("MainWindow", "Import Configuration ...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Configuration", None, QtGui.QApplication.UnicodeUTF8))

