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
        zeroed_events[-1].time = 0  - start_time

    # TODO make this user configurable as required
    del(zeroed_events[-1])

    return zeroed_events


def execute_recording(key_events):
    # Pass on events to the keyboard interface to play it back
    keyboard_interface.execute(key_events)