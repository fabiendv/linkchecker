# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/options.ui'
#
# Created: Wed May 18 21:15:07 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Options(object):
    def setupUi(self, Options):
        Options.setObjectName(_fromUtf8("Options"))
        Options.setWindowModality(QtCore.Qt.ApplicationModal)
        Options.resize(278, 240)
        self.verticalLayout = QtGui.QVBoxLayout(Options)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Options)
        self.tabWidget.setToolTip(_fromUtf8(""))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.gui_options = QtGui.QWidget()
        self.gui_options.setToolTip(_fromUtf8(""))
        self.gui_options.setObjectName(_fromUtf8("gui_options"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.gui_options)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_8 = QtGui.QLabel(self.gui_options)
        self.label_8.setMinimumSize(QtCore.QSize(240, 0))
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_3.addWidget(self.label_8)
        self.line = QtGui.QFrame(self.gui_options)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.frame = QtGui.QFrame(self.gui_options)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout = QtGui.QFormLayout(self.frame)
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setVerticalSpacing(2)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.recursionlevel = QtGui.QSpinBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recursionlevel.sizePolicy().hasHeightForWidth())
        self.recursionlevel.setSizePolicy(sizePolicy)
        self.recursionlevel.setMinimumSize(QtCore.QSize(0, 25))
        self.recursionlevel.setMinimum(-1)
        self.recursionlevel.setMaximum(100)
        self.recursionlevel.setProperty(_fromUtf8("value"), -1)
        self.recursionlevel.setObjectName(_fromUtf8("recursionlevel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.recursionlevel)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.verbose = QtGui.QCheckBox(self.frame)
        self.verbose.setEnabled(True)
        self.verbose.setText(_fromUtf8(""))
        self.verbose.setObjectName(_fromUtf8("verbose"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.verbose)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.debug = QtGui.QCheckBox(self.frame)
        self.debug.setText(_fromUtf8(""))
        self.debug.setObjectName(_fromUtf8("debug"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.debug)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtGui.QFormLayout.LabelRole, spacerItem)
        self.verticalLayout_3.addWidget(self.frame)
        self.widget = QtGui.QWidget(self.gui_options)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.closeButton = QtGui.QPushButton(self.widget)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout_3.addWidget(self.widget)
        self.tabWidget.addTab(self.gui_options, _fromUtf8(""))
        self.config_options = QtGui.QWidget()
        self.config_options.setToolTip(_fromUtf8(""))
        self.config_options.setObjectName(_fromUtf8("config_options"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.config_options)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_9 = QtGui.QLabel(self.config_options)
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_5.addWidget(self.label_9)
        self.line_2 = QtGui.QFrame(self.config_options)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_5.addWidget(self.line_2)
        self.frame_2 = QtGui.QFrame(self.config_options)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setToolTip(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_4.addWidget(self.label_6)
        self.sys_config_button = QtGui.QPushButton(self.frame_2)
        self.sys_config_button.setEnabled(False)
        self.sys_config_button.setToolTip(_fromUtf8(""))
        self.sys_config_button.setObjectName(_fromUtf8("sys_config_button"))
        self.verticalLayout_4.addWidget(self.sys_config_button)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem1)
        self.label_7 = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_4.addWidget(self.label_7)
        self.user_config_button = QtGui.QPushButton(self.frame_2)
        self.user_config_button.setEnabled(False)
        self.user_config_button.setToolTip(_fromUtf8(""))
        self.user_config_button.setObjectName(_fromUtf8("user_config_button"))
        self.verticalLayout_4.addWidget(self.user_config_button)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.tabWidget.addTab(self.config_options, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Options)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Options)

    def retranslateUi(self, Options):
        Options.setWindowTitle(_("Linkchecker options"))
        self.label_8.setText(_("The most common check options are configurable. They override any configuration file settings."))
        self.label.setToolTip(_("Check recursively all links up to given depth. A negative depth will enable infinite recursion."))
        self.label.setText(_("Recursive depth"))
        self.recursionlevel.setToolTip(_("Check recursively all links up to given depth. A negative depth will enable infinite recursion."))
        self.label_2.setToolTip(_("Log all checked URLs once. Default is to log only errors and warnings."))
        self.label_2.setText(_("Verbose output"))
        self.verbose.setToolTip(_("Log all checked URLs once. Default is to log only errors and warnings."))
        self.label_4.setText(_("Debug"))
        self.closeButton.setText(_("Close"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gui_options), _("GUI options"))
        self.label_9.setText(_("The configuration files can be edited with an integrated text editor."))
        self.label_6.setText(_("System configuration file"))
        self.sys_config_button.setText(_("Edit"))
        self.label_7.setToolTip(_("Overrides system wide configuration file settings."))
        self.label_7.setText(QtGui.QApplication.translate("Options", "User configuration file\n"
"(overrides system configuration)", None, QtGui.QApplication.UnicodeUTF8))
        self.user_config_button.setText(_("Edit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.config_options), _("Configuration files"))

