# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore

# Form implementation generated from reading ui file 'designer//metadata_finder_interface.ui'
#
# Created: Tue Aug 11 13:51:21 2015
#      by: PyQt4 UI code generator 4.11.3
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
        Dialog.resize(993, 767)
        self.verticalLayout_5 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.runNumberEdit = QtGui.QLineEdit(Dialog)
        self.runNumberEdit.setObjectName(_fromUtf8("runNumberEdit"))
        self.horizontalLayout.addWidget(self.runNumberEdit)
        self.inputErrorLabel = QtGui.QLabel(Dialog)
        self.inputErrorLabel.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inputErrorLabel.setFont(font)
        self.inputErrorLabel.setObjectName(_fromUtf8("inputErrorLabel"))
        self.horizontalLayout.addWidget(self.inputErrorLabel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.searchLabel = QtGui.QLabel(Dialog)
        self.searchLabel.setObjectName(_fromUtf8("searchLabel"))
        self.horizontalLayout.addWidget(self.searchLabel)
        self.searchLineEdit = QtGui.QLineEdit(Dialog)
        self.searchLineEdit.setObjectName(_fromUtf8("searchLineEdit"))
        self.horizontalLayout.addWidget(self.searchLineEdit)
        self.clearButton = QtGui.QPushButton(Dialog)
        self.clearButton.setText(_fromUtf8(""))
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.metadataTable = QtGui.QTableWidget(self.tab)
        self.metadataTable.setObjectName(_fromUtf8("metadataTable"))
        self.metadataTable.setColumnCount(2)
        self.metadataTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.metadataTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.metadataTable.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.metadataTable)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.saveAsciiButton = QtGui.QPushButton(self.tab)
        self.saveAsciiButton.setObjectName(_fromUtf8("saveAsciiButton"))
        self.horizontalLayout_3.addWidget(self.saveAsciiButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.configureTable = QtGui.QTableWidget(self.tab_2)
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
        self.verticalLayout_3.addWidget(self.configureTable)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.unselectAll = QtGui.QPushButton(self.tab_2)
        self.unselectAll.setEnabled(False)
        self.unselectAll.setObjectName(_fromUtf8("unselectAll"))
        self.horizontalLayout_2.addWidget(self.unselectAll)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.exportConfiguration = QtGui.QPushButton(self.tab_2)
        self.exportConfiguration.setEnabled(False)
        self.exportConfiguration.setObjectName(_fromUtf8("exportConfiguration"))
        self.horizontalLayout_2.addWidget(self.exportConfiguration)
        self.importConfiguration = QtGui.QPushButton(self.tab_2)
        self.importConfiguration.setEnabled(False)
        self.importConfiguration.setObjectName(_fromUtf8("importConfiguration"))
        self.horizontalLayout_2.addWidget(self.importConfiguration)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.runNumberEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), Dialog.runNumberEditEvent)
        QtCore.QObject.connect(self.unselectAll, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.unselectAll)
        QtCore.QObject.connect(self.exportConfiguration, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.exportConfiguration)
        QtCore.QObject.connect(self.importConfiguration, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.importConfiguration)
        QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL(_fromUtf8("currentChanged(int)")), Dialog.userChangedTab)
        QtCore.QObject.connect(self.saveAsciiButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.saveMetadataListAsAsciiFile)
        QtCore.QObject.connect(self.searchLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), Dialog.searchLineEditLive)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.searchLineEditClear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Metadata Finder", None))
        self.label.setText(_translate("Dialog", "Run(s) number:", None))
        self.runNumberEdit.setToolTip(_translate("Dialog", "1234 or 1234,1236 or 1234-1238", None))
        self.runNumberEdit.setText(_translate("Dialog", "124622", None))
        self.inputErrorLabel.setText(_translate("Dialog", "ERROR WHILE PARSING ! CHECK YOUR INPUT  ", None))
        self.searchLabel.setText(_translate("Dialog", "loop", None))
        item = self.metadataTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Run #", None))
        item = self.metadataTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "IPTS", None))
        self.saveAsciiButton.setText(_translate("Dialog", "Save List as ASCII ...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Metadata", None))
        self.configureTable.setSortingEnabled(True)
        item = self.configureTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Display ?", None))
        item = self.configureTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Name", None))
        item = self.configureTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Value", None))
        item = self.configureTable.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Units", None))
        self.unselectAll.setText(_translate("Dialog", "Unselect All", None))
        self.exportConfiguration.setText(_translate("Dialog", "Export Configuration ...", None))
        self.importConfiguration.setText(_translate("Dialog", "Import Configuration ...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Configuration", None))

