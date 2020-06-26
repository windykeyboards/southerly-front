import time
import keyboard as keyboard

# TODO enable a customisable exit recording sequence
# TODO discover why function key is not detected

EXIT_COND = 'esc'

def listen(exit_condition):
    """
    Main function to call, will implement a listener and return these events
    Should return raw dictionary with no parsing having occured


    :param exit_condition:  Key, or list of key events, to stop the listener
    :return:                List of time ordered keyboard events
    """

    # Collect events until released
    # TODO use the passed exit condition
    start_time = time.process_time()
    keyboard.start_recording()
    while True:
        if keyboard.is_pressed('esc'):
            recorded_keys = keyboard.stop_recording()
            break
        elif time.process_time() - 30 > start_time:
            recorded_keys = keyboard.stop_recording()
            break

    return recorded_keys

    #return keyboard.record(until=EXIT_COND)


def execute(macro, speedup=1):
    """
    For each key event in the macro, press/release
    This occurs with a strict timing attached for each executed event

    :param macro:   List of time ordered keyboard events
    :param speedup  Integer speed up value for playback. Default = 1
    :return:        None
    """

    keyboard.play(macro, speed_factor=speedup)