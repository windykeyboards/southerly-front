"""
Used in the creation of a parsing method
Every key recorded by pynput has a unique key code

To effectively pass this into the Teensy executable key codes each is needed
This function is written so that a user can execute it and find the keycode
for a key on their keyboard and add that to the parser if required

"""

import time
from pynput.keyboard import Key, Listener

def print_key(key):
    """
    Used to print out the keycode

    :param key: Keycode from Pynput
    :return:
    """
    if hasattr(key, 'value'):
        print('{0} - {1}'.format(key, key.value.vk))
    else:
        print('{0} - {1}'.format(key, key.vk))


def return_only(key):
    """
    The listener requires a function, but we don't need the releases
d    """
    return


def listen():
    """
    Main function to call, will implement a listener and return these events
    Should return raw dictionary with no parsing having occured


    :param exit_condition:  Key, or list of key events, to stop the listener
    :return:                Dictionary of times, to press/release and key codes
    """

    with Listener(
            on_press=print_key,
            on_release=return_only) as listener:
        listener.join()


listen()