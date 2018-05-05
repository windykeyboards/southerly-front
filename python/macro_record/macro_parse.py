import argparse
from python.macro_record import keyboard_interface


# TODO parse through events, finding relative timings
# Then allows the user options of:
# - playback
# - reduction of timing, either by a factor or as fast as possible

def parse_timings(events):
    relative_times = {}
    start_time = sorted(events.keys())[0]
    for dict_key in sorted(events.keys()):
        new_key = dict_key - start_time
        relative_times[new_key] = events[dict_key]

    return relative_times


to_parse = keyboard_interface.listen('')
parsed = parse_timings(to_parse)
keyboard_interface.execute(parsed)
