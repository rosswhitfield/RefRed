# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore

# Form implementation generated from reading ui file 'designer/table_reduction_runs_editor.ui'
#
# Created: Thu Jul 23 12:02:41 2015
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_7.addWidget(self.label_5)
        self.lambdaValue = QtGui.QLabel(self.centralwidget)
        self.lambdaValue.setObjectName(_fromUtf8("lambdaValue"))
        self.horizontalLayout_7.addWidget(self.lambdaValue)
        self.lambdaUnits = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lambdaUnits.setFont(font)
        self.lambdaUnits.setObjectName(_fromUtf8("lambdaUnits"))
        self.horizontalLayout_7.addWidget(self.lambdaUnits)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.data_groupBox = QtGui.QGroupBox(self.centralwidget)
        self.data_groupBox.setObjectName(_fromUtf8("data_groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.data_groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.dataLineEdit = QtGui.QLineEdit(self.data_groupBox)
        self.dataLineEdit.setObjectName(_fromUtf8("dataLineEdit"))
        self.horizontalLayout.addWidget(self.dataLineEdit)
        self.label_2 = QtGui.QLabel(self.data_groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.data_groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.oldDataRun = QtGui.QLabel(self.data_groupBox)
        self.oldDataRun.setObjectName(_fromUtf8("oldDataRun"))
        self.horizontalLayout_2.addWidget(self.oldDataRun)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_8 = QtGui.QLabel(self.data_groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_3.addWidget(self.label_8)
        self.normRun = QtGui.QLabel(self.data_groupBox)
        self.normRun.setObjectName(_fromUtf8("normRun"))
        self.horizontalLayout_3.addWidget(self.normRun)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.data_groupBox)
        self.norm_groupBox = QtGui.QGroupBox(self.centralwidget)
        self.norm_groupBox.setObjectName(_fromUtf8("norm_groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.norm_groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_14 = QtGui.QLabel(self.norm_groupBox)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_4.addWidget(self.label_14)
        self.dataRun = QtGui.QLabel(self.norm_groupBox)
        self.dataRun.setObjectName(_fromUtf8("dataRun"))
        self.horizontalLayout_4.addWidget(self.dataRun)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.normLineEdit = QtGui.QLineEdit(self.norm_groupBox)
        self.normLineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.normLineEdit.setStatusTip(_fromUtf8(""))
        self.normLineEdit.setWhatsThis(_fromUtf8(""))
        self.normLineEdit.setAccessibleName(_fromUtf8(""))
        self.normLineEdit.setAccessibleDescription(_fromUtf8(""))
        self.normLineEdit.setInputMask(_fromUtf8(""))
        self.normLineEdit.setText(_fromUtf8(""))
        self.normLineEdit.setObjectName(_fromUtf8("normLineEdit"))
        self.horizontalLayout_10.addWidget(self.normLineEdit)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_21 = QtGui.QLabel(self.norm_groupBox)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_5.addWidget(self.label_21)
        self.oldNormRun = QtGui.QLabel(self.norm_groupBox)
        self.oldNormRun.setObjectName(_fromUtf8("oldNormRun"))
        self.horizontalLayout_5.addWidget(self.oldNormRun)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addWidget(self.norm_groupBox)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tableWidget = QtGui.QTableWidget(self.groupBox_3)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.validRunLabel = QtGui.QLabel(self.groupBox_3)
        self.validRunLabel.setObjectName(_fromUtf8("validRunLabel"))
        self.horizontalLayout_8.addWidget(self.validRunLabel)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.invalidRunLabel = QtGui.QLabel(self.groupBox_3)
        self.invalidRunLabel.setObjectName(_fromUtf8("invalidRunLabel"))
        self.horizontalLayout_8.addWidget(self.invalidRunLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout_6.addWidget(self.cancelButton)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.insertValidRunsButton = QtGui.QPushButton(self.centralwidget)
        self.insertValidRunsButton.setEnabled(False)
        self.insertValidRunsButton.setObjectName(_fromUtf8("insertValidRunsButton"))
        self.horizontalLayout_6.addWidget(self.insertValidRunsButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.closeEvent)
        QtCore.QObject.connect(self.dataLineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), MainWindow.dataLineEditValidate)
        QtCore.QObject.connect(self.insertValidRunsButton, QtCore.SIGNAL(_fromUtf8("pressed()")), MainWindow.insertValidRunsButton)
        QtCore.QObject.connect(self.normLineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), MainWindow.normLineEditValidate)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_5.setText(_translate("MainWindow", "Lambda requested:", None))
        self.lambdaValue.setText(_translate("MainWindow", "10.5", None))
        self.lambdaUnits.setText(_translate("MainWindow", "Angstroms", None))
        self.data_groupBox.setTitle(_translate("MainWindow", "New Data Run(s)", None))
        self.dataLineEdit.setToolTip(_translate("MainWindow", "Enter Data Runs and Hit ENTER", None))
        self.label_2.setText(_translate("MainWindow", "ex: 10,15-20", None))
        self.label_3.setText(_translate("MainWindow", "Old data run(s):", None))
        self.oldDataRun.setText(_translate("MainWindow", "13445,45454,3454545", None))
        self.label_8.setText(_translate("MainWindow", "Normalization run:", None))
        self.normRun.setText(_translate("MainWindow", "4545545", None))
        self.norm_groupBox.setTitle(_translate("MainWindow", "New Normalization Run", None))
        self.label_14.setText(_translate("MainWindow", "Data run(s):", None))
        self.dataRun.setText(_translate("MainWindow", "4545545,4545454,45454", None))
        self.normLineEdit.setToolTip(_translate("MainWindow", "Enter Normalization Run and Hit ENTER", None))
        self.label_21.setText(_translate("MainWindow", "Old normalization  run:", None))
        self.oldNormRun.setText(_translate("MainWindow", "13445", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Checking Matching Lambdas", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Data", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Lambda Requested", None))
        self.validRunLabel.setText(_translate("MainWindow", "Valid Run (Matching Lambda Requested)", None))
        self.invalidRunLabel.setText(_translate("MainWindow", "Invalid Run (No Matching Lambda Requested) ", None))
        self.cancelButton.setText(_translate("MainWindow", "CANCEL", None))
        self.insertValidRunsButton.setText(_translate("MainWindow", "INSERT VALID RUNS", None))

