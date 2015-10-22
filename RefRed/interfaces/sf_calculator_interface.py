# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore

# Form implementation generated from reading ui file 'designer//sf_calculator_interface.ui'
#
# Created: Thu Oct 22 15:57:25 2015
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SFCalculatorInterface(object):
    def setupUi(self, SFCalculatorInterface):
        SFCalculatorInterface.setObjectName("SFCalculatorInterface")
        SFCalculatorInterface.resize(1656, 1221)
        self.centralwidget = QtGui.QWidget(SFCalculatorInterface)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.runSequenceLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.runSequenceLineEdit.setText("")
        self.runSequenceLineEdit.setObjectName("runSequenceLineEdit")
        self.horizontalLayout_2.addWidget(self.runSequenceLineEdit)
        self.incidentMediumComboBox = QtGui.QComboBox(self.centralwidget)
        self.incidentMediumComboBox.setMinimumSize(QtCore.QSize(300, 0))
        self.incidentMediumComboBox.setEditable(True)
        self.incidentMediumComboBox.setObjectName("incidentMediumComboBox")
        self.incidentMediumComboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.incidentMediumComboBox)
        self.toolButton = QtGui.QToolButton(self.centralwidget)
        self.toolButton.setEnabled(False)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yt_plot = MPLWidgetNoLog(self.centralwidget)
        self.yt_plot.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yt_plot.sizePolicy().hasHeightForWidth())
        self.yt_plot.setSizePolicy(sizePolicy)
        self.yt_plot.setObjectName("yt_plot")
        self.horizontalLayout.addWidget(self.yt_plot)
        self.yi_plot = MPLWidgetXLog(self.centralwidget)
        self.yi_plot.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yi_plot.sizePolicy().hasHeightForWidth())
        self.yi_plot.setSizePolicy(sizePolicy)
        self.yi_plot.setObjectName("yi_plot")
        self.horizontalLayout.addWidget(self.yi_plot)
        self.frame_11 = QtGui.QFrame(self.centralwidget)
        self.frame_11.setMaximumSize(QtCore.QSize(180, 16777215))
        self.frame_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_26 = QtGui.QVBoxLayout(self.frame_11)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_26.addItem(spacerItem)
        self.error_label = QtGui.QLabel(self.frame_11)
        self.error_label.setObjectName("error_label")
        self.verticalLayout_26.addWidget(self.error_label)
        self.verticalLayout_28 = QtGui.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.horizontalLayout_32 = QtGui.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.dataBackFromLabel = QtGui.QLabel(self.frame_11)
        self.dataBackFromLabel.setEnabled(False)
        self.dataBackFromLabel.setObjectName("dataBackFromLabel")
        self.horizontalLayout_32.addWidget(self.dataBackFromLabel)
        self.dataBackToValue = QtGui.QSpinBox(self.frame_11)
        self.dataBackToValue.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.dataBackToValue.setPalette(palette)
        self.dataBackToValue.setMinimum(-1)
        self.dataBackToValue.setMaximum(255)
        self.dataBackToValue.setProperty("value", 255)
        self.dataBackToValue.setObjectName("dataBackToValue")
        self.horizontalLayout_32.addWidget(self.dataBackToValue)
        self.back2_error = QtGui.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.back2_error.setFont(font)
        self.back2_error.setAccessibleDescription("")
        self.back2_error.setAlignment(QtCore.Qt.AlignCenter)
        self.back2_error.setObjectName("back2_error")
        self.horizontalLayout_32.addWidget(self.back2_error)
        self.verticalLayout_28.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_33 = QtGui.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.dataPeakFromLabel = QtGui.QLabel(self.frame_11)
        self.dataPeakFromLabel.setEnabled(False)
        self.dataPeakFromLabel.setObjectName("dataPeakFromLabel")
        self.horizontalLayout_33.addWidget(self.dataPeakFromLabel)
        self.dataPeakToValue = QtGui.QSpinBox(self.frame_11)
        self.dataPeakToValue.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.dataPeakToValue.setPalette(palette)
        self.dataPeakToValue.setMinimum(-1)
        self.dataPeakToValue.setMaximum(255)
        self.dataPeakToValue.setProperty("value", 255)
        self.dataPeakToValue.setObjectName("dataPeakToValue")
        self.horizontalLayout_33.addWidget(self.dataPeakToValue)
        self.peak2_error = QtGui.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.peak2_error.setFont(font)
        self.peak2_error.setAccessibleDescription("")
        self.peak2_error.setAlignment(QtCore.Qt.AlignCenter)
        self.peak2_error.setObjectName("peak2_error")
        self.horizontalLayout_33.addWidget(self.peak2_error)
        self.verticalLayout_28.addLayout(self.horizontalLayout_33)
        self.horizontalLayout_34 = QtGui.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.dataPeakToLabel = QtGui.QLabel(self.frame_11)
        self.dataPeakToLabel.setEnabled(False)
        self.dataPeakToLabel.setObjectName("dataPeakToLabel")
        self.horizontalLayout_34.addWidget(self.dataPeakToLabel)
        self.dataPeakFromValue = QtGui.QSpinBox(self.frame_11)
        self.dataPeakFromValue.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.dataPeakFromValue.setPalette(palette)
        self.dataPeakFromValue.setMinimum(-1)
        self.dataPeakFromValue.setMaximum(255)
        self.dataPeakFromValue.setProperty("value", 0)
        self.dataPeakFromValue.setObjectName("dataPeakFromValue")
        self.horizontalLayout_34.addWidget(self.dataPeakFromValue)
        self.peak1_error = QtGui.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.peak1_error.setFont(font)
        self.peak1_error.setAccessibleDescription("")
        self.peak1_error.setAlignment(QtCore.Qt.AlignCenter)
        self.peak1_error.setObjectName("peak1_error")
        self.horizontalLayout_34.addWidget(self.peak1_error)
        self.verticalLayout_28.addLayout(self.horizontalLayout_34)
        self.horizontalLayout_35 = QtGui.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.dataBackToLabel = QtGui.QLabel(self.frame_11)
        self.dataBackToLabel.setEnabled(False)
        self.dataBackToLabel.setObjectName("dataBackToLabel")
        self.horizontalLayout_35.addWidget(self.dataBackToLabel)
        self.dataBackFromValue = QtGui.QSpinBox(self.frame_11)
        self.dataBackFromValue.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.dataBackFromValue.setPalette(palette)
        self.dataBackFromValue.setMinimum(-1)
        self.dataBackFromValue.setMaximum(255)
        self.dataBackFromValue.setProperty("value", 0)
        self.dataBackFromValue.setObjectName("dataBackFromValue")
        self.horizontalLayout_35.addWidget(self.dataBackFromValue)
        self.back1_error = QtGui.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.back1_error.setFont(font)
        self.back1_error.setAccessibleDescription("")
        self.back1_error.setAlignment(QtCore.Qt.AlignCenter)
        self.back1_error.setObjectName("back1_error")
        self.horizontalLayout_35.addWidget(self.back1_error)
        self.verticalLayout_28.addLayout(self.horizontalLayout_35)
        self.dataBackgroundFlag = QtGui.QCheckBox(self.frame_11)
        self.dataBackgroundFlag.setEnabled(False)
        self.dataBackgroundFlag.setChecked(True)
        self.dataBackgroundFlag.setObjectName("dataBackgroundFlag")
        self.verticalLayout_28.addWidget(self.dataBackgroundFlag)
        self.verticalLayout_26.addLayout(self.verticalLayout_28)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_26.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.frame_11)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_40 = QtGui.QHBoxLayout()
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.dataTOFmanualLabel = QtGui.QLabel(self.centralwidget)
        self.dataTOFmanualLabel.setEnabled(False)
        self.dataTOFmanualLabel.setObjectName("dataTOFmanualLabel")
        self.horizontalLayout_40.addWidget(self.dataTOFmanualLabel)
        self.frame_14 = QtGui.QFrame(self.centralwidget)
        self.frame_14.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_14.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_14.setLineWidth(0)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_41 = QtGui.QHBoxLayout(self.frame_14)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.horizontalLayout_42 = QtGui.QHBoxLayout()
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.dataTOFautoMode = QtGui.QRadioButton(self.frame_14)
        self.dataTOFautoMode.setEnabled(False)
        self.dataTOFautoMode.setChecked(True)
        self.dataTOFautoMode.setAutoExclusive(True)
        self.dataTOFautoMode.setObjectName("dataTOFautoMode")
        self.horizontalLayout_42.addWidget(self.dataTOFautoMode)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_42.addItem(spacerItem2)
        self.dataTOFmanualMode = QtGui.QRadioButton(self.frame_14)
        self.dataTOFmanualMode.setEnabled(False)
        self.dataTOFmanualMode.setAutoExclusive(True)
        self.dataTOFmanualMode.setObjectName("dataTOFmanualMode")
        self.horizontalLayout_42.addWidget(self.dataTOFmanualMode)
        self.horizontalLayout_41.addLayout(self.horizontalLayout_42)
        self.horizontalLayout_40.addWidget(self.frame_14)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_40.addItem(spacerItem3)
        self.TOFmanualFromLabel = QtGui.QLabel(self.centralwidget)
        self.TOFmanualFromLabel.setEnabled(False)
        self.TOFmanualFromLabel.setObjectName("TOFmanualFromLabel")
        self.horizontalLayout_40.addWidget(self.TOFmanualFromLabel)
        self.TOFmanualFromValue = QtGui.QLineEdit(self.centralwidget)
        self.TOFmanualFromValue.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TOFmanualFromValue.sizePolicy().hasHeightForWidth())
        self.TOFmanualFromValue.setSizePolicy(sizePolicy)
        self.TOFmanualFromValue.setMinimumSize(QtCore.QSize(100, 0))
        self.TOFmanualFromValue.setMaximumSize(QtCore.QSize(100, 16777215))
        self.TOFmanualFromValue.setObjectName("TOFmanualFromValue")
        self.horizontalLayout_40.addWidget(self.TOFmanualFromValue)
        self.TOFmanualFromUnitsValue = QtGui.QLabel(self.centralwidget)
        self.TOFmanualFromUnitsValue.setEnabled(False)
        self.TOFmanualFromUnitsValue.setObjectName("TOFmanualFromUnitsValue")
        self.horizontalLayout_40.addWidget(self.TOFmanualFromUnitsValue)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_40.addItem(spacerItem4)
        self.TOFmanualToLabel = QtGui.QLabel(self.centralwidget)
        self.TOFmanualToLabel.setEnabled(False)
        self.TOFmanualToLabel.setObjectName("TOFmanualToLabel")
        self.horizontalLayout_40.addWidget(self.TOFmanualToLabel)
        self.TOFmanualToValue = QtGui.QLineEdit(self.centralwidget)
        self.TOFmanualToValue.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TOFmanualToValue.sizePolicy().hasHeightForWidth())
        self.TOFmanualToValue.setSizePolicy(sizePolicy)
        self.TOFmanualToValue.setMinimumSize(QtCore.QSize(100, 0))
        self.TOFmanualToValue.setMaximumSize(QtCore.QSize(100, 16777215))
        self.TOFmanualToValue.setObjectName("TOFmanualToValue")
        self.horizontalLayout_40.addWidget(self.TOFmanualToValue)
        self.TOFmanualToUnitsValue = QtGui.QLabel(self.centralwidget)
        self.TOFmanualToUnitsValue.setEnabled(False)
        self.TOFmanualToUnitsValue.setObjectName("TOFmanualToUnitsValue")
        self.horizontalLayout_40.addWidget(self.TOFmanualToUnitsValue)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_40.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_40)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 350))
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(16)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(45)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.sfFileNameLabel = QtGui.QLabel(self.centralwidget)
        self.sfFileNameLabel.setObjectName("sfFileNameLabel")
        self.horizontalLayout_3.addWidget(self.sfFileNameLabel)
        self.sfFileNameBrowseButton = QtGui.QPushButton(self.centralwidget)
        self.sfFileNameBrowseButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.sfFileNameBrowseButton.setObjectName("sfFileNameBrowseButton")
        self.horizontalLayout_3.addWidget(self.sfFileNameBrowseButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.sfFileNamePreview = QtGui.QPlainTextEdit(self.centralwidget)
        self.sfFileNamePreview.setEnabled(False)
        self.sfFileNamePreview.setMinimumSize(QtCore.QSize(0, 60))
        self.sfFileNamePreview.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.sfFileNamePreview.setObjectName("sfFileNamePreview")
        self.verticalLayout.addWidget(self.sfFileNamePreview)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.generateSFfileButton = QtGui.QPushButton(self.centralwidget)
        self.generateSFfileButton.setEnabled(False)
        self.generateSFfileButton.setObjectName("generateSFfileButton")
        self.horizontalLayout_4.addWidget(self.generateSFfileButton)
        self.exportButton = QtGui.QPushButton(self.centralwidget)
        self.exportButton.setEnabled(False)
        self.exportButton.setObjectName("exportButton")
        self.horizontalLayout_4.addWidget(self.exportButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        SFCalculatorInterface.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SFCalculatorInterface)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1656, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        SFCalculatorInterface.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SFCalculatorInterface)
        self.statusbar.setObjectName("statusbar")
        SFCalculatorInterface.setStatusBar(self.statusbar)
        self.actionLoadingConfiguration = QtGui.QAction(SFCalculatorInterface)
        self.actionLoadingConfiguration.setEnabled(False)
        self.actionLoadingConfiguration.setObjectName("actionLoadingConfiguration")
        self.actionSavingAsConfiguration = QtGui.QAction(SFCalculatorInterface)
        self.actionSavingAsConfiguration.setEnabled(False)
        self.actionSavingAsConfiguration.setObjectName("actionSavingAsConfiguration")
        self.actionSavingConfiguration = QtGui.QAction(SFCalculatorInterface)
        self.actionSavingConfiguration.setEnabled(False)
        self.actionSavingConfiguration.setObjectName("actionSavingConfiguration")
        self.actionEdit_Incident_Medium_List = QtGui.QAction(SFCalculatorInterface)
        self.actionEdit_Incident_Medium_List.setObjectName("actionEdit_Incident_Medium_List")
        self.clearSFconentFileMenu = QtGui.QAction(SFCalculatorInterface)
        self.clearSFconentFileMenu.setObjectName("clearSFconentFileMenu")
        self.menuFile.addAction(self.actionLoadingConfiguration)
        self.menuFile.addAction(self.actionSavingAsConfiguration)
        self.menuFile.addAction(self.actionSavingConfiguration)
        self.menuTools.addAction(self.clearSFconentFileMenu)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(SFCalculatorInterface)
        QtCore.QObject.connect(self.runSequenceLineEdit, QtCore.SIGNAL("returnPressed()"), SFCalculatorInterface.runSequenceLineEditEvent)
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL("customContextMenuRequested(QPoint)"), SFCalculatorInterface.tableWidgetRightClick)
        QtCore.QObject.connect(self.sfFileNameBrowseButton, QtCore.SIGNAL("clicked()"), SFCalculatorInterface.browseFile)
        QtCore.QObject.connect(self.actionSavingAsConfiguration, QtCore.SIGNAL("triggered()"), SFCalculatorInterface.savingAsConfiguration)
        QtCore.QObject.connect(self.dataTOFautoMode, QtCore.SIGNAL("clicked()"), SFCalculatorInterface.selectAutoTOF)
        QtCore.QObject.connect(self.dataTOFmanualMode, QtCore.SIGNAL("clicked()"), SFCalculatorInterface.selectManualTOF)
        QtCore.QObject.connect(self.actionLoadingConfiguration, QtCore.SIGNAL("triggered()"), SFCalculatorInterface.loadingConfiguration)
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL("cellClicked(int,int)"), SFCalculatorInterface.tableWidgetCellSelected)
        QtCore.QObject.connect(self.dataBackToValue, QtCore.SIGNAL("editingFinished()"), SFCalculatorInterface.back2SpinBoxValueChanged)
        QtCore.QObject.connect(self.dataBackFromValue, QtCore.SIGNAL("editingFinished()"), SFCalculatorInterface.back1SpinBoxValueChanged)
        QtCore.QObject.connect(self.dataPeakFromValue, QtCore.SIGNAL("editingFinished()"), SFCalculatorInterface.peak1SpinBoxValueChanged)
        QtCore.QObject.connect(self.dataPeakToValue, QtCore.SIGNAL("editingFinished()"), SFCalculatorInterface.peak2SpinBoxValueChanged)
        QtCore.QObject.connect(self.TOFmanualFromValue, QtCore.SIGNAL("returnPressed()"), SFCalculatorInterface.manualTOFtextFieldValidated)
        QtCore.QObject.connect(self.TOFmanualToValue, QtCore.SIGNAL("returnPressed()"), SFCalculatorInterface.manualTOFtextFieldValidated)
        QtCore.QObject.connect(self.incidentMediumComboBox, QtCore.SIGNAL("currentIndexChanged(int)"), SFCalculatorInterface.incidentMediumComboBoxChanged)
        QtCore.QObject.connect(self.actionSavingConfiguration, QtCore.SIGNAL("triggered()"), SFCalculatorInterface.savingConfiguration)
        QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL("clicked()"), SFCalculatorInterface.editIncidentMediumList)
        QtCore.QObject.connect(self.generateSFfileButton, QtCore.SIGNAL("clicked()"), SFCalculatorInterface.generateSFfile)
        QtCore.QObject.connect(self.exportButton, QtCore.SIGNAL("clicked()"), SFCalculatorInterface.exportScript)
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL("cellChanged(int,int)"), SFCalculatorInterface.tableWidgetCellEntered)
        QtCore.QObject.connect(self.clearSFconentFileMenu, QtCore.SIGNAL("triggered()"), SFCalculatorInterface.clearSFContentFile)
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL("itemSelectionChanged()"), SFCalculatorInterface.tableWidgetRowSelected)
        QtCore.QMetaObject.connectSlotsByName(SFCalculatorInterface)

    def retranslateUi(self, SFCalculatorInterface):
        SFCalculatorInterface.setWindowTitle(QtGui.QApplication.translate("SFCalculatorInterface", "SF Calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SFCalculatorInterface", "Run or Sequence of Runs:", None, QtGui.QApplication.UnicodeUTF8))
        self.runSequenceLineEdit.setToolTip(QtGui.QApplication.translate("SFCalculatorInterface", "1234 or 1234,1236,1239 or 1234-1238", None, QtGui.QApplication.UnicodeUTF8))
        self.incidentMediumComboBox.setItemText(0, QtGui.QApplication.translate("SFCalculatorInterface", "Select or Define Incident Medium ...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("SFCalculatorInterface", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.error_label.setText(QtGui.QApplication.translate("SFCalculatorInterface", "SELECTION ERROR", None, QtGui.QApplication.UnicodeUTF8))
        self.dataBackFromLabel.setText(QtGui.QApplication.translate("SFCalculatorInterface", "Back2", None, QtGui.QApplication.UnicodeUTF8))
        self.back2_error.setText(QtGui.QApplication.translate("SFCalculatorInterface", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.dataPeakFromLabel.setText(QtGui.QApplication.translate("SFCalculatorInterface", "Peak2", None, QtGui.QApplication.UnicodeUTF8))
        self.peak2_error.setText(QtGui.QApplication.translate("SFCalculatorInterface", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.dataPeakToLabel.setText(QtGui.QApplication.translate("SFCalculatorInterface", "Peak1", None, QtGui.QApplication.UnicodeUTF8))
        self.peak1_error.setText(QtGui.QApplication.translate("SFCalculatorInterface", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.dataBackToLabel.setText(QtGui.QApplication.translate("SFCalculatorInterface", "Back1", None, QtGui.QApplication.UnicodeUTF8))
        self.back1_error.setText(QtGui.QApplication.translate("SFCalculatorInterface", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.dataBackgroundFlag.setText(QtGui.QApplication.translate("SFCalculatorInterface", "with background", None, QtGui.QApplication.UnicodeUTF8))
        self.dataTOFmanualLabel.setText(QtGui.QApplication.translate("SFCalculatorInterface", "TOF range", None, QtGui.QApplication.UnicodeUTF8))
        self.dataTOFautoMode.setText(QtGui.QApplication.translate("SFCalculatorInterface", "Auto", None, QtGui.QApplication.UnicodeUTF8))
        self.dataTOFmanualMode.setText(QtGui.QApplication.translate("SFCalculatorInterface", "Manual", None, QtGui.QApplication.UnicodeUTF8))
        self.TOFmanualFromLabel.setText(QtGui.QApplication.translate("SFCalculatorInterface", "from", None, QtGui.QApplication.UnicodeUTF8))
        self.TOFmanualFromValue.setText(QtGui.QApplication.translate("SFCalculatorInterface", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.TOFmanualFromUnitsValue.setText(QtGui.QApplication.translate("SFCalculatorInterface", "ms", None, QtGui.QApplication.UnicodeUTF8))
        self.TOFmanualToLabel.setText(QtGui.QApplication.translate("SFCalculatorInterface", "to", None, QtGui.QApplication.UnicodeUTF8))
        self.TOFmanualToValue.setText(QtGui.QApplication.translate("SFCalculatorInterface", "200", None, QtGui.QApplication.UnicodeUTF8))
        self.TOFmanualToUnitsValue.setText(QtGui.QApplication.translate("SFCalculatorInterface", "ms", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("SFCalculatorInterface", "Run #", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("SFCalculatorInterface", "Nbr of Attenuators", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("SFCalculatorInterface", "lambda min", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("SFCalculatorInterface", "lambda max", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("SFCalculatorInterface", "p Charge", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("SFCalculatorInterface", "lambda Requested", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("SFCalculatorInterface", "S1W", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(7).setText(QtGui.QApplication.translate("SFCalculatorInterface", "S1H", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(8).setText(QtGui.QApplication.translate("SFCalculatorInterface", "SiW", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(9).setText(QtGui.QApplication.translate("SFCalculatorInterface", "SiH", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(10).setText(QtGui.QApplication.translate("SFCalculatorInterface", "Peak1", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(11).setText(QtGui.QApplication.translate("SFCalculatorInterface", "Peak2", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(12).setText(QtGui.QApplication.translate("SFCalculatorInterface", "Back1", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(13).setText(QtGui.QApplication.translate("SFCalculatorInterface", "Back2", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(14).setText(QtGui.QApplication.translate("SFCalculatorInterface", "TOF1 (ms)", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(15).setText(QtGui.QApplication.translate("SFCalculatorInterface", "TOF2 (ms)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SFCalculatorInterface", "SF File Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.sfFileNameLabel.setText(QtGui.QApplication.translate("SFCalculatorInterface", "N/A", None, QtGui.QApplication.UnicodeUTF8))
        self.sfFileNameBrowseButton.setText(QtGui.QApplication.translate("SFCalculatorInterface", "Browse ...", None, QtGui.QApplication.UnicodeUTF8))
        self.generateSFfileButton.setText(QtGui.QApplication.translate("SFCalculatorInterface", "GENERATE SCALING FACTORS", None, QtGui.QApplication.UnicodeUTF8))
        self.exportButton.setText(QtGui.QApplication.translate("SFCalculatorInterface", "EXPORT SCRIPT ...", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("SFCalculatorInterface", "Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("SFCalculatorInterface", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoadingConfiguration.setText(QtGui.QApplication.translate("SFCalculatorInterface", "Load ...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoadingConfiguration.setShortcut(QtGui.QApplication.translate("SFCalculatorInterface", "Meta+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSavingAsConfiguration.setText(QtGui.QApplication.translate("SFCalculatorInterface", "Save As ...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSavingAsConfiguration.setShortcut(QtGui.QApplication.translate("SFCalculatorInterface", "Meta+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSavingConfiguration.setText(QtGui.QApplication.translate("SFCalculatorInterface", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSavingConfiguration.setShortcut(QtGui.QApplication.translate("SFCalculatorInterface", "Meta+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Incident_Medium_List.setText(QtGui.QApplication.translate("SFCalculatorInterface", "Edit Incident Medium List ...", None, QtGui.QApplication.UnicodeUTF8))
        self.clearSFconentFileMenu.setText(QtGui.QApplication.translate("SFCalculatorInterface", "Clear Content SF File", None, QtGui.QApplication.UnicodeUTF8))

from mplwidgetnolog import MPLWidgetNoLog
from .mplwidgetxlog import MPLWidgetXLog
