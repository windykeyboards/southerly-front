"""
Modified from the layout created by QtDesigner
Same source, but code layout beautified and simplified
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        # Set size
        MainWindow.resize(525, 440)
        MainWindow.setBaseSize(QtCore.QSize(90, 90))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 471, 380))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        '''
        User interaction assets
        '''

        self.macro_name_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.macro_name_label.setAutoFillBackground(False)
        self.macro_name_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.macro_name_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.macro_name_label.setText("- recorded macro name -")

        self.macro_name_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.macro_name_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.macro_name_btn.setText("Name macro")

        self.macro_string_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.macro_string_label.setMinimumSize(QtCore.QSize(0, 40))
        self.macro_string_label.setAutoFillBackground(False)
        self.macro_string_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.macro_string_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.macro_string_label.setText("- recorded macro string -")

        self.record_macro_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.record_macro_btn.setText("Record Macro")

        self.playback_macro_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.playback_macro_btn.setText("Playback Macro")

        self.save_macro_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.save_macro_btn.setText("Save Macro")

        self.load_macro_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.load_macro_btn.setText("Load Macro")

        self.program_device_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.program_device_btn.setText("Program Device")

        '''
        Keycap buttons
        '''

        self.keycap_one_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.keycap_one_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.keycap_one_btn.setText("PushButton")

        self.keycap_two_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.keycap_two_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.keycap_two_btn.setText("PushButton")

        self.keycap_three_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.keycap_three_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.keycap_three_btn.setText("PushButton")

        self.keycap_four_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.keycap_four_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.keycap_four_btn.setText("PushButton")

        self.keycap_five_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.keycap_five_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.keycap_five_btn.setText("PushButton")

        self.keycap_six_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.keycap_six_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.keycap_six_btn.setText("PushButton")

        '''
        Spacer items
        '''
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Minimum)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed,
                                            QtWidgets.QSizePolicy.Minimum)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)

        '''
        Line items
        '''
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)

        '''
        Add all items into layouts
        '''
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.addWidget(self.macro_name_label)
        self.horizontalLayout_6.addItem(spacerItem)
        self.horizontalLayout_6.addWidget(self.macro_name_btn)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addWidget(self.macro_string_label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.addWidget(self.record_macro_btn)
        self.horizontalLayout_4.addWidget(self.playback_macro_btn)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.addWidget(self.save_macro_btn)
        self.horizontalLayout_5.addWidget(self.load_macro_btn)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.horizontalLayout_5.addWidget(self.program_device_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.addWidget(self.keycap_one_btn)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_3.addWidget(self.keycap_two_btn)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_3.addWidget(self.keycap_three_btn)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.addWidget(self.keycap_four_btn)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_2.addWidget(self.keycap_five_btn)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.horizontalLayout_2.addWidget(self.keycap_six_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        '''
        Setup Main Window
        '''
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 525, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
