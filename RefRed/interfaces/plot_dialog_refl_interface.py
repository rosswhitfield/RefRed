# -*- coding: utf-8 -*-
# @PydevCodeAnalysisIgnore

# Form implementation generated from reading ui file 'designer//plot_dialog_refl_interface.ui'
#
# Created: Fri May 20 10:03:31 2016
#      by: qtpy UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(s):
        return s


try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)


except AttributeError:

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1232, 999)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.plot_pixel_vs_counts = MPLWidgetXLog(self.tab)
        self.plot_pixel_vs_counts.setObjectName(_fromUtf8("plot_pixel_vs_counts"))
        self.horizontalLayout.addWidget(self.plot_pixel_vs_counts)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.frame = QtWidgets.QFrame(self.groupBox_4)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem)
        self.john_peak2_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.john_peak2_label.setFont(font)
        self.john_peak2_label.setAccessibleDescription(_fromUtf8(""))
        self.john_peak2_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.john_peak2_label.setObjectName(_fromUtf8("john_peak2_label"))
        self.verticalLayout_13.addWidget(self.john_peak2_label)
        self.john_peak2 = QtWidgets.QSpinBox(self.frame)
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
        self.john_peak2.setPalette(palette)
        self.john_peak2.setMaximum(303)
        self.john_peak2.setObjectName(_fromUtf8("john_peak2"))
        self.verticalLayout_13.addWidget(self.john_peak2)
        self.horizontalLayout_15.addLayout(self.verticalLayout_13)
        self.verticalLayout_12.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.john_peak1 = QtWidgets.QSpinBox(self.frame)
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
        self.john_peak1.setPalette(palette)
        self.john_peak1.setMaximum(303)
        self.john_peak1.setObjectName(_fromUtf8("john_peak1"))
        self.verticalLayout_14.addWidget(self.john_peak1)
        self.john_peak1_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.john_peak1_label.setFont(font)
        self.john_peak1_label.setAccessibleDescription(_fromUtf8(""))
        self.john_peak1_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.john_peak1_label.setObjectName(_fromUtf8("john_peak1_label"))
        self.verticalLayout_14.addWidget(self.john_peak1_label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem1)
        self.horizontalLayout_16.addLayout(self.verticalLayout_14)
        self.verticalLayout_12.addLayout(self.horizontalLayout_16)
        self.verticalLayout_11.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.frame_2 = QtWidgets.QFrame(self.groupBox_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.john_back_flag = QtWidgets.QCheckBox(self.frame_2)
        self.john_back_flag.setObjectName(_fromUtf8("john_back_flag"))
        self.verticalLayout_9.addWidget(self.john_back_flag)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem2)
        self.john_back2_label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.john_back2_label.setFont(font)
        self.john_back2_label.setAccessibleDescription(_fromUtf8(""))
        self.john_back2_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.john_back2_label.setObjectName(_fromUtf8("john_back2_label"))
        self.verticalLayout_9.addWidget(self.john_back2_label)
        self.john_back2 = QtWidgets.QSpinBox(self.frame_2)
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
        self.john_back2.setPalette(palette)
        self.john_back2.setMaximum(303)
        self.john_back2.setObjectName(_fromUtf8("john_back2"))
        self.verticalLayout_9.addWidget(self.john_back2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem3)
        self.horizontalLayout_13.addLayout(self.verticalLayout_9)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem4)
        self.john_back1 = QtWidgets.QSpinBox(self.frame_2)
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
        self.john_back1.setPalette(palette)
        self.john_back1.setMaximum(303)
        self.john_back1.setObjectName(_fromUtf8("john_back1"))
        self.verticalLayout_10.addWidget(self.john_back1)
        self.john_back1_label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.john_back1_label.setFont(font)
        self.john_back1_label.setAccessibleDescription(_fromUtf8(""))
        self.john_back1_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.john_back1_label.setObjectName(_fromUtf8("john_back1_label"))
        self.verticalLayout_10.addWidget(self.john_back1_label)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem5)
        self.horizontalLayout_14.addLayout(self.verticalLayout_10)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        self.verticalLayout_8.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.john_clocking_box = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.john_clocking_box.sizePolicy().hasHeightForWidth())
        self.john_clocking_box.setSizePolicy(sizePolicy)
        self.john_clocking_box.setObjectName(_fromUtf8("john_clocking_box"))
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.john_clocking_box)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.frame_6 = QtWidgets.QFrame(self.john_clocking_box)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.john_clock2 = QtWidgets.QSpinBox(self.frame_6)
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
        self.john_clock2.setPalette(palette)
        self.john_clock2.setMaximum(303)
        self.john_clock2.setObjectName(_fromUtf8("john_clock2"))
        self.verticalLayout_17.addWidget(self.john_clock2)
        self.horizontalLayout_17.addLayout(self.verticalLayout_17)
        self.verticalLayout_16.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem6)
        self.john_clock1 = QtWidgets.QSpinBox(self.frame_6)
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
        self.john_clock1.setPalette(palette)
        self.john_clock1.setMaximum(303)
        self.john_clock1.setObjectName(_fromUtf8("john_clock1"))
        self.verticalLayout_18.addWidget(self.john_clock1)
        self.horizontalLayout_18.addLayout(self.verticalLayout_18)
        self.verticalLayout_16.addLayout(self.horizontalLayout_18)
        self.verticalLayout_15.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.john_clocking_box)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.plot_counts_vs_pixel = MPLWidget(self.tab_2)
        self.plot_counts_vs_pixel.setObjectName(_fromUtf8("plot_counts_vs_pixel"))
        self.verticalLayout.addWidget(self.plot_counts_vs_pixel)
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.frame_3 = QtWidgets.QFrame(self.groupBox)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.jim_peak1_label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.jim_peak1_label.setFont(font)
        self.jim_peak1_label.setAccessibleDescription(_fromUtf8(""))
        self.jim_peak1_label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.jim_peak1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.jim_peak1_label.setObjectName(_fromUtf8("jim_peak1_label"))
        self.horizontalLayout_4.addWidget(self.jim_peak1_label)
        self.jim_peak1 = QtWidgets.QSpinBox(self.frame_3)
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
        self.jim_peak1.setPalette(palette)
        self.jim_peak1.setMaximum(303)
        self.jim_peak1.setObjectName(_fromUtf8("jim_peak1"))
        self.horizontalLayout_4.addWidget(self.jim_peak1)
        self.jim_peak2 = QtWidgets.QSpinBox(self.frame_3)
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
        self.jim_peak2.setPalette(palette)
        self.jim_peak2.setMaximum(303)
        self.jim_peak2.setObjectName(_fromUtf8("jim_peak2"))
        self.horizontalLayout_4.addWidget(self.jim_peak2)
        self.jim_peak2_label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.jim_peak2_label.setFont(font)
        self.jim_peak2_label.setAccessibleDescription(_fromUtf8(""))
        self.jim_peak2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.jim_peak2_label.setObjectName(_fromUtf8("jim_peak2_label"))
        self.horizontalLayout_4.addWidget(self.jim_peak2_label)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.frame_4 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.jim_back_flag = QtWidgets.QCheckBox(self.frame_4)
        self.jim_back_flag.setObjectName(_fromUtf8("jim_back_flag"))
        self.horizontalLayout_5.addWidget(self.jim_back_flag)
        spacerItem9 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.jim_back1_label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.jim_back1_label.setFont(font)
        self.jim_back1_label.setAccessibleDescription(_fromUtf8(""))
        self.jim_back1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.jim_back1_label.setObjectName(_fromUtf8("jim_back1_label"))
        self.horizontalLayout_5.addWidget(self.jim_back1_label)
        self.jim_back1 = QtWidgets.QSpinBox(self.frame_4)
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
        self.jim_back1.setPalette(palette)
        self.jim_back1.setMaximum(303)
        self.jim_back1.setObjectName(_fromUtf8("jim_back1"))
        self.horizontalLayout_5.addWidget(self.jim_back1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.jim_back2 = QtWidgets.QSpinBox(self.frame_4)
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
        self.jim_back2.setPalette(palette)
        self.jim_back2.setMaximum(303)
        self.jim_back2.setObjectName(_fromUtf8("jim_back2"))
        self.horizontalLayout_5.addWidget(self.jim_back2)
        self.jim_back2_label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.jim_back2_label.setFont(font)
        self.jim_back2_label.setAccessibleDescription(_fromUtf8(""))
        self.jim_back2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.jim_back2_label.setObjectName(_fromUtf8("jim_back2_label"))
        self.horizontalLayout_5.addWidget(self.jim_back2_label)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.horizontalLayout_6.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.jim_clocking_box = QtWidgets.QGroupBox(self.tab_2)
        self.jim_clocking_box.setObjectName(_fromUtf8("jim_clocking_box"))
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.jim_clocking_box)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.frame_5 = QtWidgets.QFrame(self.jim_clocking_box)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.jim_clock1 = QtWidgets.QSpinBox(self.frame_5)
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
        self.jim_clock1.setPalette(palette)
        self.jim_clock1.setMaximum(303)
        self.jim_clock1.setObjectName(_fromUtf8("jim_clock1"))
        self.horizontalLayout_8.addWidget(self.jim_clock1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem12)
        self.jim_clock2 = QtWidgets.QSpinBox(self.frame_5)
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
        self.jim_clock2.setPalette(palette)
        self.jim_clock2.setMaximum(303)
        self.jim_clock2.setObjectName(_fromUtf8("jim_clock2"))
        self.horizontalLayout_8.addWidget(self.jim_clock2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        self.horizontalLayout_7.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.jim_clocking_box)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.invalid_selection_label = QtWidgets.QLabel(Dialog)
        self.invalid_selection_label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.invalid_selection_label.setObjectName(_fromUtf8("invalid_selection_label"))
        self.verticalLayout_3.addWidget(self.invalid_selection_label)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(
            self.jim_peak1, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Dialog.jim_peak1_spinbox_signal
        )
        QtCore.QObject.connect(
            self.john_peak1, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Dialog.john_peak1_spinbox_signal
        )
        QtCore.QObject.connect(
            self.jim_peak2, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Dialog.jim_peak2_spinbox_signal
        )
        QtCore.QObject.connect(
            self.john_peak2, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Dialog.john_peak2_spinbox_signal
        )
        QtCore.QObject.connect(
            self.jim_back1, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Dialog.jim_back1_spinbox_signal
        )
        QtCore.QObject.connect(
            self.john_back1, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Dialog.john_back1_spinbox_signal
        )
        QtCore.QObject.connect(
            self.jim_back2, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Dialog.jim_back2_spinbox_signal
        )
        QtCore.QObject.connect(
            self.john_back2, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Dialog.john_back2_spinbox_signal
        )
        QtCore.QObject.connect(
            self.jim_back_flag, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Dialog.jim_back_flag_clicked
        )
        QtCore.QObject.connect(
            self.john_back_flag, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Dialog.john_back_flag_clicked
        )
        QtCore.QObject.connect(
            self.jim_clock1, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Dialog.jim_clock_spinbox_signal
        )
        QtCore.QObject.connect(
            self.jim_clock2, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Dialog.jim_clock_spinbox_signal
        )
        QtCore.QObject.connect(
            self.john_clock1, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Dialog.john_clock_spinbox_signal
        )
        QtCore.QObject.connect(
            self.john_clock2, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Dialog.john_clock_spinbox_signal
        )
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Selection Tool", None))
        self.groupBox_4.setTitle(_translate("Dialog", "PEAK", None))
        self.john_peak2_label.setText(_translate("Dialog", "*", None))
        self.john_peak1_label.setText(_translate("Dialog", "*", None))
        self.groupBox_3.setTitle(_translate("Dialog", "BACKGROUND", None))
        self.john_back_flag.setText(_translate("Dialog", "with Back.", None))
        self.john_back2_label.setText(_translate("Dialog", "*", None))
        self.john_back1_label.setText(_translate("Dialog", "*", None))
        self.john_clocking_box.setTitle(_translate("Dialog", "CLOCKING", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "John", None))
        self.groupBox.setTitle(_translate("Dialog", "PEAK", None))
        self.jim_peak1_label.setText(_translate("Dialog", "*", None))
        self.jim_peak2_label.setText(_translate("Dialog", "*", None))
        self.groupBox_2.setTitle(_translate("Dialog", "BACKGROUND", None))
        self.jim_back_flag.setText(_translate("Dialog", "with Background", None))
        self.jim_back1_label.setText(_translate("Dialog", "*", None))
        self.jim_back2_label.setText(_translate("Dialog", "*", None))
        self.jim_clocking_box.setTitle(_translate("Dialog", "CLOCKING", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Jim", None))
        self.invalid_selection_label.setText(_translate("Dialog", "(*)    INVALID SELECTION", None))


from .mplwidget import MPLWidget
from .mplwidgetxlog import MPLWidgetXLog
from . import icons_rc
