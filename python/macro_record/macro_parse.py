from python.macro_record import keyboard_interface

# TODO allows the user options of:
# - playback
# - reduction of timing, either by a factor or as fast as possible

def listen_to_keyboard():
    """
    Listen to keyboard strokes
    :return: parsed keyboard strokes, a list of Keyboard Events
    """
    to_parse = keyboard_interface.listen('')
    return parse_timings(to_parse)


def parse_timings(keyboard_strokes):
    """
    Sanitise the keyboard strokes by making the first event start at 0 seconds
    Remove the keystroke that is used to terminate the sequence

    :param keyboard_strokes:    list of keyboard Events
    :return:                    list of keyboard events
    """

    zeroed_events = []
    start_time = 0
    for event in keyboard_strokes:
        if start_time == 0:
            start_time = event.time
        zeroed_events.append(event)
        zeroed_events[-1].time = event.time - start_time

    # TODO make this user configurable as required
    try:
        del(zeroed_events[-1])
    except IndexError:
        print("List assignment out of range")
    return zeroed_events

def parse_to_string(keyboard_strokes):
    """
    Used to set labels for the user, shows which keys were recorded

    :param macro_dict:  Dictionary of timings to key actions
    :return:            String of concatenated keypresses
    """
    temp_str = ''
    for key in keyboard_strokes:
        if key.event_type == "down":
            temp_str = temp_str + key.name + '; '

    return temp_str

def execute_recording(key_events):
    # Pass on events to the keyboard interface to play it back
    keyboard_interface.execute(key_events)