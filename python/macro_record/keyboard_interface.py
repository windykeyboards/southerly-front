import time
import sched
from pynput.keyboard import Key, Listener, Controller

# TODO enable a customisable exit recording sequence
# TODO discover why function key is not detected

KEY_EVENTS = {}
EXIT_COND = Key.esc


def on_press(key):
    KEY_EVENTS[time.time()] = ['press', key]


def on_release(key):
    if key == EXIT_COND:
        # Stop listener
        # print(KEY_EVENTS)
        return False
    KEY_EVENTS[time.time()] = ['release', key]


def listen(exit_condition):
    """
    Main function to call, will implement a listener and return these events
    Should return raw dictionary with no parsing having occured


    :param exit_condition:  Key, or list of key events, to stop the listener
    :return:                Dictionary of times, to press/release and key codes
    """
    EXIT_COND = Key.esc
    global KEY_EVENTS
    KEY_EVENTS = {} # Clear each time else it stays in memory
    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    return KEY_EVENTS


def press(keyboard, keycode):
    keyboard.press(keycode)


def release(keyboard, keycode):
    keyboard.release(keycode)


def execute(macro):
    """
    For each key event in the macro, press/release
    This occurs with a strict timing attached for each executed event

    :param macro:   Dictionary of times to an event, and key code
    :return:        None
    """

    scheduler = sched.scheduler(time.time, time.sleep)
    control = Controller()
    for dict_key in macro:
        if macro[dict_key][0] == 'press':
            scheduler.enter(dict_key, 1, press, (control, macro[dict_key][1]))
        else:
            scheduler.enter(dict_key, 1, release, (control, macro[dict_key][1]))

    print('Executing function now')
    scheduler.run()
    print('Execution complete')