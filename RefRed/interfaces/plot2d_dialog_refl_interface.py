# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore

# Form implementation generated from reading ui file 'designer//plot2d_dialog_refl_interface.ui'
#
# Created: Tue Feb 16 12:53:36 2016
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1379, 1188)
        self.verticalLayout_4 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.y_pixel_vs_tof_plot = MPLWidgetNoLog(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_pixel_vs_tof_plot.sizePolicy().hasHeightForWidth())
        self.y_pixel_vs_tof_plot.setSizePolicy(sizePolicy)
        self.y_pixel_vs_tof_plot.setObjectName("y_pixel_vs_tof_plot")
        self.horizontalLayout.addWidget(self.y_pixel_vs_tof_plot)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_37 = QtGui.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_37.addItem(spacerItem)
        self.dataTOFmanualLabel = QtGui.QLabel(self.tab)
        self.dataTOFmanualLabel.setEnabled(True)
        self.dataTOFmanualLabel.setObjectName("dataTOFmanualLabel")
        self.horizontalLayout_37.addWidget(self.dataTOFmanualLabel)
        self.frame_13 = QtGui.QFrame(self.tab)
        self.frame_13.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_13.setLineWidth(0)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_38 = QtGui.QHBoxLayout(self.frame_13)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.horizontalLayout_39 = QtGui.QHBoxLayout()
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.tof_auto_flag = QtGui.QRadioButton(self.frame_13)
        self.tof_auto_flag.setChecked(True)
        self.tof_auto_flag.setAutoExclusive(True)
        self.tof_auto_flag.setObjectName("tof_auto_flag")
        self.horizontalLayout_39.addWidget(self.tof_auto_flag)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_39.addItem(spacerItem1)
        self.tof_manual_flag = QtGui.QRadioButton(self.frame_13)
        self.tof_manual_flag.setEnabled(True)
        self.tof_manual_flag.setAutoExclusive(True)
        self.tof_manual_flag.setObjectName("tof_manual_flag")
        self.horizontalLayout_39.addWidget(self.tof_manual_flag)
        self.horizontalLayout_38.addLayout(self.horizontalLayout_39)
        self.horizontalLayout_37.addWidget(self.frame_13)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_37.addItem(spacerItem2)
        self.tof_from_label = QtGui.QLabel(self.tab)
        self.tof_from_label.setEnabled(False)
        self.tof_from_label.setObjectName("tof_from_label")
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
        self.tof_from.setObjectName("tof_from")
        self.horizontalLayout_37.addWidget(self.tof_from)
        self.tof_from_units = QtGui.QLabel(self.tab)
        self.tof_from_units.setEnabled(False)
        self.tof_from_units.setObjectName("tof_from_units")
        self.horizontalLayout_37.addWidget(self.tof_from_units)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_37.addItem(spacerItem3)
        self.tof_to_label = QtGui.QLabel(self.tab)
        self.tof_to_label.setEnabled(False)
        self.tof_to_label.setObjectName("tof_to_label")
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
        self.tof_to.setObjectName("tof_to")
        self.horizontalLayout_37.addWidget(self.tof_to)
        self.tof_to_units = QtGui.QLabel(self.tab)
        self.tof_to_units.setEnabled(False)
        self.tof_to_units.setObjectName("tof_to_units")
        self.horizontalLayout_37.addWidget(self.tof_to_units)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_37.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_37)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.detector_plot = MPLWidgetNoLog(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.detector_plot.sizePolicy().hasHeightForWidth())
        self.detector_plot.setSizePolicy(sizePolicy)
        self.detector_plot.setObjectName("detector_plot")
        self.horizontalLayout_2.addWidget(self.detector_plot)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.frame_20 = QtGui.QFrame(self.tab_2)
        self.frame_20.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_20.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_54 = QtGui.QHBoxLayout(self.frame_20)
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.horizontalLayout_83 = QtGui.QHBoxLayout()
        self.horizontalLayout_83.setObjectName("horizontalLayout_83")
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_83.addItem(spacerItem5)
        self.low_res_flag = QtGui.QCheckBox(self.frame_20)
        self.low_res_flag.setChecked(True)
        self.low_res_flag.setObjectName("low_res_flag")
        self.horizontalLayout_83.addWidget(self.low_res_flag)
        self.low_res1_label = QtGui.QLabel(self.frame_20)
        self.low_res1_label.setObjectName("low_res1_label")
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
        self.low_res1.setObjectName("low_res1")
        self.horizontalLayout_83.addWidget(self.low_res1)
        self.low_res2_label = QtGui.QLabel(self.frame_20)
        self.low_res2_label.setObjectName("low_res2_label")
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
        self.low_res2.setObjectName("low_res2")
        self.horizontalLayout_83.addWidget(self.low_res2)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_83.addItem(spacerItem8)
        self.horizontalLayout_54.addLayout(self.horizontalLayout_83)
        self.verticalLayout_2.addWidget(self.frame_20)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_6.addWidget(self.tabWidget)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame = QtGui.QFrame(self.groupBox_4)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem9)
        self.peak2_label = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.peak2_label.setFont(font)
        self.peak2_label.setAccessibleDescription("")
        self.peak2_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.peak2_label.setObjectName("peak2_label")
        self.verticalLayout_13.addWidget(self.peak2_label)
        self.peak2 = QtGui.QSpinBox(self.frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.peak2.setPalette(palette)
        self.peak2.setMaximum(303)
        self.peak2.setObjectName("peak2")
        self.verticalLayout_13.addWidget(self.peak2)
        self.horizontalLayout_15.addLayout(self.verticalLayout_13)
        self.verticalLayout_12.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.peak1 = QtGui.QSpinBox(self.frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.peak1.setPalette(palette)
        self.peak1.setMaximum(303)
        self.peak1.setObjectName("peak1")
        self.verticalLayout_14.addWidget(self.peak1)
        self.peak1_label = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.peak1_label.setFont(font)
        self.peak1_label.setAccessibleDescription("")
        self.peak1_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.peak1_label.setObjectName("peak1_label")
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
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.back_flag = QtGui.QCheckBox(self.groupBox_3)
        self.back_flag.setObjectName("back_flag")
        self.verticalLayout_8.addWidget(self.back_flag)
        self.frame_2 = QtGui.QFrame(self.groupBox_3)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem11)
        self.back2_label = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.back2_label.setFont(font)
        self.back2_label.setAccessibleDescription("")
        self.back2_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.back2_label.setObjectName("back2_label")
        self.verticalLayout_9.addWidget(self.back2_label)
        self.back2 = QtGui.QSpinBox(self.frame_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.back2.setPalette(palette)
        self.back2.setMaximum(303)
        self.back2.setObjectName("back2")
        self.verticalLayout_9.addWidget(self.back2)
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem12)
        self.horizontalLayout_13.addLayout(self.verticalLayout_9)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem13 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem13)
        self.back1 = QtGui.QSpinBox(self.frame_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.back1.setPalette(palette)
        self.back1.setMaximum(303)
        self.back1.setObjectName("back1")
        self.verticalLayout_10.addWidget(self.back1)
        self.back1_label = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.back1_label.setFont(font)
        self.back1_label.setAccessibleDescription("")
        self.back1_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.back1_label.setObjectName("back1_label")
        self.verticalLayout_10.addWidget(self.back1_label)
        spacerItem14 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem14)
        self.horizontalLayout_14.addLayout(self.verticalLayout_10)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        self.verticalLayout_8.addWidget(self.frame_2)
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        self.clocking_box = QtGui.QGroupBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clocking_box.sizePolicy().hasHeightForWidth())
        self.clocking_box.setSizePolicy(sizePolicy)
        self.clocking_box.setObjectName("clocking_box")
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.clocking_box)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_6 = QtGui.QFrame(self.clocking_box)
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.frame_6)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.verticalLayout_18 = QtGui.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.clock2 = QtGui.QSpinBox(self.frame_6)
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
        self.clock2.setPalette(palette)
        self.clock2.setObjectName("clock2")
        self.verticalLayout_18.addWidget(self.clock2)
        spacerItem15 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem15)
        self.clock1 = QtGui.QSpinBox(self.frame_6)
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
        self.clock1.setPalette(palette)
        self.clock1.setMaximum(303)
        self.clock1.setObjectName("clock1")
        self.verticalLayout_18.addWidget(self.clock1)
        self.horizontalLayout_18.addLayout(self.verticalLayout_18)
        self.verticalLayout_16.addLayout(self.horizontalLayout_18)
        self.verticalLayout_15.addWidget(self.frame_6)
        self.horizontalLayout_4.addWidget(self.clocking_box)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.error_label = QtGui.QLabel(Dialog)
        self.error_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.error_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.error_label.setObjectName("error_label")
        self.verticalLayout_3.addWidget(self.error_label)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.back_flag, QtCore.SIGNAL("clicked(bool)"), Dialog.activate_or_not_back_widgets)
        QtCore.QObject.connect(self.peak1, QtCore.SIGNAL("editingFinished()"), Dialog.manual_input_peak1)
        QtCore.QObject.connect(self.peak2, QtCore.SIGNAL("editingFinished()"), Dialog.manual_input_peak2)
        QtCore.QObject.connect(self.back1, QtCore.SIGNAL("editingFinished()"), Dialog.manual_input_back1)
        QtCore.QObject.connect(self.back2, QtCore.SIGNAL("editingFinished()"), Dialog.manual_input_back2)
        QtCore.QObject.connect(self.tof_from, QtCore.SIGNAL("editingFinished()"), Dialog.manual_input_of_tof_field)
        QtCore.QObject.connect(self.low_res2, QtCore.SIGNAL("editingFinished()"), Dialog.manual_input_of_low_res_field)
        QtCore.QObject.connect(self.tof_manual_flag, QtCore.SIGNAL("clicked()"), Dialog.manual_auto_tof_clicked)
        QtCore.QObject.connect(self.low_res_flag, QtCore.SIGNAL("clicked(bool)"), Dialog.activate_or_not_low_res_widgets)
        QtCore.QObject.connect(self.low_res1, QtCore.SIGNAL("editingFinished()"), Dialog.manual_input_of_low_res_field)
        QtCore.QObject.connect(self.tof_to, QtCore.SIGNAL("editingFinished()"), Dialog.manual_input_of_tof_field)
        QtCore.QObject.connect(self.tof_auto_flag, QtCore.SIGNAL("clicked()"), Dialog.manual_auto_tof_clicked)
        QtCore.QObject.connect(self.clock1, QtCore.SIGNAL("editingFinished()"), Dialog.clock_spinbox)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "2D Selection Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.dataTOFmanualLabel.setText(QtGui.QApplication.translate("Dialog", "TOF range", None, QtGui.QApplication.UnicodeUTF8))
        self.tof_auto_flag.setText(QtGui.QApplication.translate("Dialog", "Auto", None, QtGui.QApplication.UnicodeUTF8))
        self.tof_manual_flag.setText(QtGui.QApplication.translate("Dialog", "Manual", None, QtGui.QApplication.UnicodeUTF8))
        self.tof_from_label.setText(QtGui.QApplication.translate("Dialog", "from", None, QtGui.QApplication.UnicodeUTF8))
        self.tof_from.setText(QtGui.QApplication.translate("Dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.tof_from_units.setText(QtGui.QApplication.translate("Dialog", "ms", None, QtGui.QApplication.UnicodeUTF8))
        self.tof_to_label.setText(QtGui.QApplication.translate("Dialog", "to", None, QtGui.QApplication.UnicodeUTF8))
        self.tof_to.setText(QtGui.QApplication.translate("Dialog", "200", None, QtGui.QApplication.UnicodeUTF8))
        self.tof_to_units.setText(QtGui.QApplication.translate("Dialog", "ms", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog", "Y Pixel vs TOF", None, QtGui.QApplication.UnicodeUTF8))
        self.low_res_flag.setText(QtGui.QApplication.translate("Dialog", "Low Resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.low_res1_label.setText(QtGui.QApplication.translate("Dialog", "From Pixel", None, QtGui.QApplication.UnicodeUTF8))
        self.low_res2_label.setText(QtGui.QApplication.translate("Dialog", "To Pixel", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Dialog", "Y pixel vs X pixel", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Dialog", "PEAK", None, QtGui.QApplication.UnicodeUTF8))
        self.peak2_label.setText(QtGui.QApplication.translate("Dialog", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.peak1_label.setText(QtGui.QApplication.translate("Dialog", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Dialog", "BACKGROUND", None, QtGui.QApplication.UnicodeUTF8))
        self.back_flag.setText(QtGui.QApplication.translate("Dialog", "with Back.", None, QtGui.QApplication.UnicodeUTF8))
        self.back2_label.setText(QtGui.QApplication.translate("Dialog", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.back1_label.setText(QtGui.QApplication.translate("Dialog", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.clocking_box.setTitle(QtGui.QApplication.translate("Dialog", "CLOCKING", None, QtGui.QApplication.UnicodeUTF8))
        self.error_label.setText(QtGui.QApplication.translate("Dialog", "(*) INVALID SELECTION", None, QtGui.QApplication.UnicodeUTF8))

from mplwidgetnolog import MPLWidgetNoLog
import icons_rc
