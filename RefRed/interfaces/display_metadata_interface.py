# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore

# Form implementation generated from reading ui file 'designer//display_metadata_interface.ui'
#
# Created: Fri May 20 10:03:29 2016
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.searchLabel = QtGui.QLabel(self.centralwidget)
        self.searchLabel.setObjectName(_fromUtf8("searchLabel"))
        self.horizontalLayout_3.addWidget(self.searchLabel)
        self.searchLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.searchLineEdit.setObjectName(_fromUtf8("searchLineEdit"))
        self.horizontalLayout_3.addWidget(self.searchLineEdit)
        self.clearButton = QtGui.QPushButton(self.centralwidget)
        self.clearButton.setText(_fromUtf8(""))
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout_3.addWidget(self.clearButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Metadata = QtGui.QWidget()
        self.Metadata.setObjectName(_fromUtf8("Metadata"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.Metadata)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.metadataTable = QtGui.QTableWidget(self.Metadata)
        self.metadataTable.setObjectName(_fromUtf8("metadataTable"))
        self.metadataTable.setColumnCount(3)
        self.metadataTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.metadataTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.metadataTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.metadataTable.setHorizontalHeaderItem(2, item)
        self.verticalLayout_4.addWidget(self.metadataTable)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.saveMetadataAsAsciiButton = QtGui.QPushButton(self.Metadata)
        self.saveMetadataAsAsciiButton.setEnabled(False)
        self.saveMetadataAsAsciiButton.setObjectName(_fromUtf8("saveMetadataAsAsciiButton"))
        self.horizontalLayout_2.addWidget(self.saveMetadataAsAsciiButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.Metadata, _fromUtf8(""))
        self.Configure = QtGui.QWidget()
        self.Configure.setObjectName(_fromUtf8("Configure"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.Configure)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.configureTable = QtGui.QTableWidget(self.Configure)
        self.configureTable.setAlternatingRowColors(True)
        self.configureTable.setObjectName(_fromUtf8("configureTable"))
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
        self.configureTable.horizontalHeader().setSortIndicatorShown(False)
        self.configureTable.verticalHeader().setSortIndicatorShown(False)
        self.verticalLayout_5.addWidget(self.configureTable)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.unselectAllButton = QtGui.QPushButton(self.Configure)
        self.unselectAllButton.setObjectName(_fromUtf8("unselectAllButton"))
        self.horizontalLayout.addWidget(self.unselectAllButton)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.exportConfigurationButton = QtGui.QPushButton(self.Configure)
        self.exportConfigurationButton.setObjectName(_fromUtf8("exportConfigurationButton"))
        self.horizontalLayout.addWidget(self.exportConfigurationButton)
        self.importConfigurationButton = QtGui.QPushButton(self.Configure)
        self.importConfigurationButton.setObjectName(_fromUtf8("importConfigurationButton"))
        self.horizontalLayout.addWidget(self.importConfigurationButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.Configure, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL(_fromUtf8("currentChanged(int)")), MainWindow.userChangedTab)
        QtCore.QObject.connect(self.saveMetadataAsAsciiButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.saveMetadataListAsAscii)
        QtCore.QObject.connect(self.exportConfigurationButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.exportConfiguration)
        QtCore.QObject.connect(self.importConfigurationButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.importConfiguration)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.clearSearchLineEdit)
        QtCore.QObject.connect(self.unselectAllButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.unselectAll)
        QtCore.QObject.connect(self.searchLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), MainWindow.liveEditSearchLineEdit)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.searchLabel.setText(_translate("MainWindow", "loop", None))
        item = self.metadataTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.metadataTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value", None))
        item = self.metadataTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Units", None))
        self.saveMetadataAsAsciiButton.setText(_translate("MainWindow", "Save List of Metadata as ASCII ...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Metadata), _translate("MainWindow", "Metadata", None))
        item = self.configureTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Display ?", None))
        item = self.configureTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.configureTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Value", None))
        item = self.configureTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Units", None))
        self.unselectAllButton.setText(_translate("MainWindow", "Unselect All", None))
        self.exportConfigurationButton.setText(_translate("MainWindow", "Export Configuration ...", None))
        self.importConfigurationButton.setText(_translate("MainWindow", "Import Configuration ...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Configure), _translate("MainWindow", "Configure", None))

