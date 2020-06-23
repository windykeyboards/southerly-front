"""
HELPER CODE
Used in the creation of a parsing method
Every key recorded by the keyboard interface has a unique scan code

To effectively pass this into the Teensy executable key codes each is needed
This function is written so that a user can execute it and find the scan code
for a key on their keyboard and add that to the parser if required

"""

import keyboard as keyboard

def print_key(key):
    """
    Used to print out the keycode

    :param key: Keycode from Pynput
    :return:
    """
    if key.event_type == 'down':
        print("Name {0}\tScan Code {1}".format(key.name, key.scan_code))


def listen():
    """
    Main function to call, will hook the keyboard
    """

    keyboard.hook(print_key)
    keyboard.wait('esc')

listen()