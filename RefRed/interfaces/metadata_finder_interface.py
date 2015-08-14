# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore

# Form implementation generated from reading ui file 'designer//metadata_finder_interface.ui'
#
# Created: Fri Aug 14 09:32:05 2015
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(993, 767)
        self.verticalLayout_5 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.runNumberEdit = QtGui.QLineEdit(Dialog)
        self.runNumberEdit.setObjectName("runNumberEdit")
        self.horizontalLayout.addWidget(self.runNumberEdit)
        self.inputErrorLabel = QtGui.QLabel(Dialog)
        self.inputErrorLabel.setEnabled(True)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.inputErrorLabel.setFont(font)
        self.inputErrorLabel.setObjectName("inputErrorLabel")
        self.horizontalLayout.addWidget(self.inputErrorLabel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.searchLabel = QtGui.QLabel(Dialog)
        self.searchLabel.setObjectName("searchLabel")
        self.horizontalLayout.addWidget(self.searchLabel)
        self.searchLineEdit = QtGui.QLineEdit(Dialog)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.horizontalLayout.addWidget(self.searchLineEdit)
        self.clearButton = QtGui.QPushButton(Dialog)
        self.clearButton.setText("")
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.tabWidget = QtGui.QTabWidget(Dialog)
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

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.runNumberEdit, QtCore.SIGNAL("returnPressed()"), Dialog.runNumberEditEvent)
        QtCore.QObject.connect(self.unselectAll, QtCore.SIGNAL("clicked()"), Dialog.unselectAll)
        QtCore.QObject.connect(self.exportConfiguration, QtCore.SIGNAL("clicked()"), Dialog.exportConfiguration)
        QtCore.QObject.connect(self.importConfiguration, QtCore.SIGNAL("clicked()"), Dialog.importConfiguration)
        QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL("currentChanged(int)"), Dialog.userChangedTab)
        QtCore.QObject.connect(self.saveAsciiButton, QtCore.SIGNAL("clicked()"), Dialog.saveMetadataListAsAsciiFile)
        QtCore.QObject.connect(self.searchLineEdit, QtCore.SIGNAL("textEdited(QString)"), Dialog.searchLineEditLive)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL("clicked()"), Dialog.searchLineEditClear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Metadata Finder", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Run(s) number:", None, QtGui.QApplication.UnicodeUTF8))
        self.runNumberEdit.setToolTip(QtGui.QApplication.translate("Dialog", "1234 or 1234,1236 or 1234-1238", None, QtGui.QApplication.UnicodeUTF8))
        self.runNumberEdit.setText(QtGui.QApplication.translate("Dialog", "124622", None, QtGui.QApplication.UnicodeUTF8))
        self.inputErrorLabel.setText(QtGui.QApplication.translate("Dialog", "ERROR WHILE PARSING ! CHECK YOUR INPUT  ", None, QtGui.QApplication.UnicodeUTF8))
        self.searchLabel.setText(QtGui.QApplication.translate("Dialog", "loop", None, QtGui.QApplication.UnicodeUTF8))
        self.metadataTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Dialog", "Run #", None, QtGui.QApplication.UnicodeUTF8))
        self.metadataTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Dialog", "IPTS", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAsciiButton.setText(QtGui.QApplication.translate("Dialog", "Save List as ASCII ...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog", "Metadata", None, QtGui.QApplication.UnicodeUTF8))
        self.configureTable.setSortingEnabled(True)
        self.configureTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Dialog", "Display ?", None, QtGui.QApplication.UnicodeUTF8))
        self.configureTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Dialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.configureTable.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Dialog", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.configureTable.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("Dialog", "Units", None, QtGui.QApplication.UnicodeUTF8))
        self.unselectAll.setText(QtGui.QApplication.translate("Dialog", "Unselect All", None, QtGui.QApplication.UnicodeUTF8))
        self.exportConfiguration.setText(QtGui.QApplication.translate("Dialog", "Export Configuration ...", None, QtGui.QApplication.UnicodeUTF8))
        self.importConfiguration.setText(QtGui.QApplication.translate("Dialog", "Import Configuration ...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Dialog", "Configuration", None, QtGui.QApplication.UnicodeUTF8))

