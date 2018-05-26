"""
Modified from the layout created by QtDesigner
Same source, but code layout beautified and simplified
"""

import re
from PyQt5 import QtCore, QtGui, QtWidgets
from python.macro_record import macro_parse


class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # Set size
        self.setWindowTitle('Windy M1')
        self.setGeometry(600, 400, 440, 340)

        self.centralwidget = QtWidgets.QWidget()
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 471, 380))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        '''
        Data storage variables
        '''
        self.selected_key = 1
        # A dictionary of selected keys to macro recordings
        self.macros = {}

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
        self.macro_name_btn.clicked.connect(self.label_macro)

        self.macro_string_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.macro_string_label.setMinimumSize(QtCore.QSize(0, 40))
        self.macro_string_label.setAutoFillBackground(False)
        self.macro_string_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.macro_string_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.macro_string_label.setText("- recorded macro string -")

        self.record_macro_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.record_macro_btn.setText("Record Macro")
        self.record_macro_btn.clicked.connect(self.record_macro)

        self.playback_macro_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.playback_macro_btn.setText("Playback Macro")
        self.playback_macro_btn.clicked.connect(self.playback_macro)

        self.save_macro_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.save_macro_btn.setText("Save Macro")
        self.save_macro_btn.clicked.connect(self.save_macro)

        self.load_macro_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.load_macro_btn.setText("Load Macro")
        self.load_macro_btn.clicked.connect(self.load_macro)

        self.program_device_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.program_device_btn.setText("Program Device")
        self.program_device_btn.clicked.connect(self.program_device)

        '''
        Keycap buttons
        '''

        self.keycap_one_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.keycap_one_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.keycap_one_btn.setText("PushButton")
        self.keycap_one_btn.clicked.connect(lambda: self.select_keyboard_button(1))

        self.keycap_two_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.keycap_two_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.keycap_two_btn.setText("PushButton")
        self.keycap_two_btn.clicked.connect(lambda: self.select_keyboard_button(2))

        self.keycap_three_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.keycap_three_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.keycap_three_btn.setText("PushButton")
        self.keycap_three_btn.clicked.connect(lambda: self.select_keyboard_button(3))

        self.keycap_four_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.keycap_four_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.keycap_four_btn.setText("PushButton")
        self.keycap_four_btn.clicked.connect(lambda: self.select_keyboard_button(4))

        self.keycap_five_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.keycap_five_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.keycap_five_btn.setText("PushButton")
        self.keycap_five_btn.clicked.connect(lambda: self.select_keyboard_button(5))

        self.keycap_six_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.keycap_six_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.keycap_six_btn.setText("PushButton")
        self.keycap_six_btn.clicked.connect(lambda: self.select_keyboard_button(6))

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
        self.select_keyboard_button(1)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 525, 21))

        self.setLayout(self.verticalLayout)
        self.show()

    def label_macro(self):
        """
        Open up a brief text dialog window that allows input
        Enter key terminates window
        Alters the macro_name_label

        TODO Allocate into memory associated with current key selected

        :return: None
        """
        text, pressed = QtWidgets.QInputDialog.getText(self, "Label Macro", "Macro Name:",
                                                       QtWidgets.QLineEdit.Normal, "")
        if pressed and text != '':
            self.macro_name_label.setText(text)

    def record_macro(self):
        """
        Shows that macro recording has started
        Starts the listener for macro recording
        Should display what the exit condition for the macro recording is
        When the macro finishes, display the recorded macro as a string

        Assign the macro recording to the currently selected key

        :return: None
        """

        self.set_stylesheet(self.record_macro_btn, 'background-color:#FF0000;')
        self.record_macro_btn.setText('RECORDING')
        self.record_macro_btn.repaint()

        recorded_input = macro_parse.listen_to_keyboard()

        self.set_stylesheet(self.record_macro_btn, '')
        self.record_macro_btn.setText("Record Macro")

        self.macros[self.selected_key] = {}
        self.macros[self.selected_key]['key_events'] = recorded_input
        self.macros[self.selected_key]['name'] = self.macro_name_label.text()

        temp_str = self.parse_macro_to_string(recorded_input)
        self.macro_string_label.setText(temp_str)

    def playback_macro(self):
        """
        Replay the macro assigned to the currently selected key
        Show a visual indication the playback is taking place

        :return: None
        """
        if self.selected_key in self.macros.keys():
            self.set_stylesheet(self.playback_macro_btn, 'background-color:#FF0000;')
            self.playback_macro_btn.setText('PLAYBACK')
            self.playback_macro_btn.repaint()

            macro_parse.execute_recording(self.macros[self.selected_key]['key_events'])
            self.set_stylesheet(self.playback_macro_btn, '')
            self.playback_macro_btn.setText("Playback Macro")

    def load_macro(self):
        """
        Load all macros, names, and key assignments
        File format and place to save settings to be determined by save_macro

        TODO implement

        :return: None
        """
        print("Unimplemented load")

    def save_macro(self):
        """
        Save all macros, names, and key assignments
        File format and place to save settings to be determined

        TODO implement

        :return: None
        """
        print("Unimplemented save")

    def program_device(self):
        """
        Take all key macros stored
        Parse into the format we need for our controller
        Save to a file (optional)
        Open serial pipe to the controller
        Write to device

        TODO implement

        :return: None
        """
        print("Unimplemented program")

    def select_keyboard_button(self, key_button):
        """
        Assign the current key so macros are recorded properly
        Update macro label and string appropriately
        Change stylesheets to show selected key

        :param key_button: integer, 1 to 6
        :return: None
        """

        # TODO Refactor definition of keys to make this code simpler
        if self.selected_key == 1:
            self.set_stylesheet(self.keycap_one_btn, '')
        if self.selected_key == 2:
            self.set_stylesheet(self.keycap_two_btn, '')
        if self.selected_key == 3:
            self.set_stylesheet(self.keycap_three_btn, '')
        if self.selected_key == 4:
            self.set_stylesheet(self.keycap_four_btn, '')
        if self.selected_key == 5:
            self.set_stylesheet(self.keycap_five_btn, '')
        if self.selected_key == 6:
            self.set_stylesheet(self.keycap_six_btn, '')

        self.selected_key = key_button

        if self.selected_key == 1:
            self.set_stylesheet(self.keycap_one_btn, 'background-color:#F4F9E1;')
        if self.selected_key == 2:
            self.set_stylesheet(self.keycap_two_btn, 'background-color:#F4F9E1;')
        if self.selected_key == 3:
            self.set_stylesheet(self.keycap_three_btn, 'background-color:#F4F9E1;')
        if self.selected_key == 4:
            self.set_stylesheet(self.keycap_four_btn, 'background-color:#F4F9E1;')
        if self.selected_key == 5:
            self.set_stylesheet(self.keycap_five_btn, 'background-color:#F4F9E1;')
        if self.selected_key == 6:
            self.set_stylesheet(self.keycap_six_btn, 'background-color:#F4F9E1;')

        if self.selected_key in self.macros.keys():
            self.macro_name_label.setText(self.macros[self.selected_key]['name'])
            self.macro_string_label.setText(self.parse_macro_to_string(self.macros[self.selected_key]['key_events']))
        else:
            self.macro_name_label.setText("- recorded macro name -")
            self.macro_string_label.setText("- recorded macro string -")

    def parse_macro_to_string(self, macro_dict):
        """
        Used to set labels for the user, shows which keys were recorded

        :param macro_dict: Dictionary of timings to key actions
        :return:    String of concatenated keypresses
        """
        temp_str = ''
        for key in macro_dict.keys():
            try:
                temp_str = temp_str + macro_dict[key][0] + \
                           ' ' + macro_dict[key][1].name + '; '
            except:
                temp_str = temp_str + macro_dict[key][0] + \
                           ' ' + macro_dict[key][1].char + '; '

        temp_str = re.sub(r'press|release', '', temp_str)
        return temp_str

    def set_stylesheet(self, object, style_string):
        object.setStyleSheet(style_string)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    sys.exit(app.exec_())
