"""
Modified from the layout created by QtDesigner
Same source, but code layout beautified and simplified
"""

import re
import os
import json
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from python.macro_record import macro_parse
from pynput.keyboard import KeyCode, Key
from python.device_programming import macro_language_parse


class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        file = open('main_window.ui', 'r')
        self.ui = uic.loadUi(file)
        file.close()

        '''
        Data storage variables
        '''
        self.selected_key = 1
        # A dictionary of selected keys to macro recordings
        self.macros = {}

        '''
        User interaction assets
        '''

        self.ui.macro_name_label.setAutoFillBackground(False)
        self.ui.macro_name_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ui.macro_name_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ui.macro_name_label.setText("- recorded macro name -")

        self.ui.macro_name_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ui.macro_name_btn.setText("Name macro")
        self.ui.macro_name_btn.clicked.connect(self.label_macro)

        self.ui.macro_string_label.setMinimumSize(QtCore.QSize(0, 40))
        self.ui.macro_string_label.setAutoFillBackground(False)
        self.ui.macro_string_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ui.macro_string_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ui.macro_string_label.setText("- recorded macro string -")

        self.ui.record_macro_btn.setText("Record Macro")
        self.ui.record_macro_btn.clicked.connect(self.record_macro)

        self.ui.playback_macro_btn.setText("Playback Macro")
        self.ui.playback_macro_btn.clicked.connect(self.playback_macro)

        self.ui.save_macro_btn.setText("Save Macro")
        self.ui.save_macro_btn.clicked.connect(self.save_macro)

        self.ui.load_macro_btn.setText("Load Macro")
        self.ui.load_macro_btn.clicked.connect(self.load_macro)


        self.ui.program_device_btn.setText("Program Device")
        self.ui.program_device_btn.clicked.connect(self.program_device)

        '''
        Keycap buttons
        '''

        self.ui.keycap_one_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.ui.keycap_one_btn.setText("PushButton")
        self.ui.keycap_one_btn.clicked.connect(lambda: self.select_keyboard_button(1))

        self.ui.keycap_two_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.ui.keycap_two_btn.setText("PushButton")
        self.ui.keycap_two_btn.clicked.connect(lambda: self.select_keyboard_button(2))

        self.ui.keycap_three_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.ui.keycap_three_btn.setText("PushButton")
        self.ui.keycap_three_btn.clicked.connect(lambda: self.select_keyboard_button(3))


        self.ui.keycap_four_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.ui.keycap_four_btn.setText("PushButton")
        self.ui.keycap_four_btn.clicked.connect(lambda: self.select_keyboard_button(4))

        self.ui.keycap_five_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.ui.keycap_five_btn.setText("PushButton")
        self.ui.keycap_five_btn.clicked.connect(lambda: self.select_keyboard_button(5))

        self.ui.keycap_six_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.ui.keycap_six_btn.setText("PushButton")
        self.ui.keycap_six_btn.clicked.connect(lambda: self.select_keyboard_button(6))


        '''
        Setup Main Window
        '''
        self.select_keyboard_button(1)

        self.ui.show()

    def label_macro(self):
        """
        Open up a brief text dialog window that allows input
        Enter key terminates window
        Alters the macro_name_label

        :return: None
        """
        text, pressed = QtWidgets.QInputDialog.getText(self, "Label Macro", "Macro Name:",
                                                       QtWidgets.QLineEdit.Normal, "")
        if pressed and text != '':
            self.ui.macro_name_label.setText(text)
            self.macros[self.selected_key]['name'] = text

    def record_macro(self):
        """
        Shows that macro recording has started
        Starts the listener for macro recording
        Should display what the exit condition for the macro recording is
        When the macro finishes, display the recorded macro as a string

        Assign the macro recording to the currently selected key

        :return: None
        """

        self.set_stylesheet(self.ui.record_macro_btn, 'background-color:#FF0000;')
        self.ui.record_macro_btn.setText('RECORDING')
        self.ui.record_macro_btn.repaint()

        recorded_input = macro_parse.listen_to_keyboard()

        # bug fix, to remove
        # Add the vk into the list of recorded_input for later save/load of macro
        for key in recorded_input.keys():
            temp_key = recorded_input[key][1]
            if isinstance(temp_key, KeyCode):
                recorded_input[key].append(temp_key.vk)
            else:
                recorded_input[key].append(temp_key.value.vk)

        self.set_stylesheet(self.record_macro_btn, '')
        self.record_macro_btn.setText("Record Macro")

        self.macros[self.selected_key] = {}
        self.macros[self.selected_key]['key_events'] = recorded_input
        self.macros[self.selected_key]['name'] = self.ui.macro_name_label.text()

        temp_str = self.parse_macro_to_string(recorded_input)
        self.ui.macro_string_label.setText(temp_str)

    def playback_macro(self):
        """
        Replay the macro assigned to the currently selected key
        Show a visual indication the playback is taking place

        :return: None
        """
        if self.selected_key in self.macros.keys():
            self.set_stylesheet(self.playback_macro_btn, 'background-color:#FF0000;')
            self.ui.playback_macro_btn.setText('PLAYBACK')
            self.ui.playback_macro_btn.repaint()

            macro_parse.execute_recording(self.macros[self.selected_key]['key_events'])
            self.set_stylesheet(self.ui.playback_macro_btn, '')
            self.ui.playback_macro_btn.setText("Playback Macro")

    def load_macro(self):
        """
        Load all macros, names, and key assignments
        File format is json, save file chosen by user

        Loads all items into a temporary dictionary
        Then converts all chars/names of keys into proper key codes
        This allows easy playback and execution in keyboard_interface.py

        :return: None
        """

        cur_dir = os.path.dirname(os.path.realpath(__file__))
        file_query = QtWidgets.QFileDialog()
        load_file_path = file_query.getOpenFileName(directory=cur_dir,
                                                    filter='*.json')
        if load_file_path[0] == '':
            return

        temp_dict = json.load(open(load_file_path[0], 'r'))
        for key_num in temp_dict.keys():
            for key_events in temp_dict[key_num].keys():
                if key_events == 'name':
                    continue
                for time_key in temp_dict[key_num][key_events]:
                    key_code = temp_dict[key_num][key_events][time_key][1]
                    if 'Key.' in key_code:
                        temp_keycode = eval(key_code)
                    else:
                        temp_keycode = KeyCode.from_char(key_code)
                        # Add in vk if it is missing (only the case for char keycodes)
                        temp_keycode.vk = temp_dict[key_num][key_events][time_key][2]
                    temp_dict[key_num][key_events][time_key][1] = temp_keycode

        self.macros = {}
        for key_num in temp_dict.keys():
            # Integer key numbers get stored as strings
            self.macros[int(key_num)] = temp_dict[key_num]
            # And floats for timings are stored as strings also
            self.macros[int(key_num)]['key_events'] = {float(k): v for k, v in temp_dict[key_num]['key_events'].items()}

        self.select_keyboard_button(1)

    def save_macro(self):
        """
        Save all macros, names, and key assignments
        File format is json for simplicity
        File location and name to be chosen by user

        Keycodes are simplified to either a char, if available, or the key name
        # TODO look into vk implementation, is it a larger set?
        # TODO currently have to write in the vk code as a separate entry
        # This is because when loading macros not all fields of a Key are
        # automatically filled if we pass in a char, or vk, by itself

        :return: None
        """

        cur_dir = os.path.dirname(os.path.realpath(__file__))
        file_query = QtWidgets.QFileDialog()
        save_file_path = file_query.getSaveFileName(directory=cur_dir,
                                                    filter='*.json')
        if save_file_path[0] == '':
            return
        class KeyCodeEncoder(json.JSONEncoder):
            def default(self, obj):
                # Extract the useful info from the keys, nothing more
                if isinstance(obj, KeyCode):
                    return obj.char
                elif isinstance(obj, Key):
                    return 'Key.' + obj.name
                return json.JSONEncoder.default(self, obj)

        with open(save_file_path[0], 'w') as fp:
            json.dump(self.macros, fp, cls=KeyCodeEncoder, indent=4)

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
        print("Partially implemented program")

        macro_language_parse.create_macro_string(self.macros)

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
            self.set_stylesheet(self.ui.keycap_one_btn, '')
        if self.selected_key == 2:
            self.set_stylesheet(self.ui.keycap_two_btn, '')
        if self.selected_key == 3:
            self.set_stylesheet(self.ui.keycap_three_btn, '')
        if self.selected_key == 4:
            self.set_stylesheet(self.ui.keycap_four_btn, '')
        if self.selected_key == 5:
            self.set_stylesheet(self.ui.keycap_five_btn, '')
        if self.selected_key == 6:
            self.set_stylesheet(self.ui.keycap_six_btn, '')

        self.selected_key = key_button

        if self.selected_key == 1:
            self.set_stylesheet(self.ui.keycap_one_btn, 'background-color:#F4F9E1;')
        if self.selected_key == 2:
            self.set_stylesheet(self.ui.keycap_two_btn, 'background-color:#F4F9E1;')
        if self.selected_key == 3:
            self.set_stylesheet(self.ui.keycap_three_btn, 'background-color:#F4F9E1;')
        if self.selected_key == 4:
            self.set_stylesheet(self.ui.keycap_four_btn, 'background-color:#F4F9E1;')
        if self.selected_key == 5:
            self.set_stylesheet(self.ui.keycap_five_btn, 'background-color:#F4F9E1;')
        if self.selected_key == 6:
            self.set_stylesheet(self.ui.keycap_six_btn, 'background-color:#F4F9E1;')

        if self.selected_key in self.macros.keys():
            self.ui.macro_name_label.setText(self.macros[self.selected_key]['name'])
            self.ui.macro_string_label.setText(self.parse_macro_to_string(self.macros[self.selected_key]['key_events']))
        else:
            self.ui.macro_name_label.setText("- recorded macro name -")
            self.ui.macro_string_label.setText("- recorded macro string -")

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
