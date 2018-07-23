"""
This takes in the key events given by the main_page methods and parses it as such:

p - press, signifies the press of a key
t - time, in ms to wait
u - release, represents the release of a key

Currently using the teensy library to interface with a machine
As such the identifies of keys are masked hex as shown here:
https://github.com/PaulStoffregen/cores/blob/master/teensy/keylayouts.h

An example of the parsed events would be
p,E001
t,250
p,F022
r,F022
t,100
r,E001

"""

import re
from pkg_resources import resource_filename # to read the text files in the module


def get_vk(key):
    """
    Unique identifies of keys in pynput are the "virtual key" numbers
    """
    if hasattr(key, 'value'):
        return key.value.vk
    else:
        return key.vk

def create_macro_string(key_events):

    mask_dict = masking_dict()

    try:
        for button_num in sorted(key_events.keys()):
            macro_string = ''
            prev_time = 0
            for time_key in sorted(key_events[button_num]['key_events'].keys()):
                wait_time = float(time_key)*1000 - prev_time
                prev_time = float(time_key)*1000
                key_action = key_events[button_num]['key_events'][time_key][0]
                mod_key = 'p,'
                if key_action == 'release':
                    mod_key = 'r,'
                key = key_events[button_num]['key_events'][time_key][1]
                vk_code = get_vk(key)
                hex_code = mask_dict[vk_code][-1]
                if hex_code == -1:
                    print('Sorry, but the key code \"{0}\" is not currently supported'.format(vk_code))
                    print('Please direct this error to https://github.com/windykeyboards/southerly-front')
                    continue

                macro_string += 't,' + str(int(wait_time)) + '\n'
                macro_string += mod_key + hex_code + '\n'
            print(macro_string)
    except:
        print('Unable to parse macro to macro string\nPossible Issues:\n')
        print('\tUnknown key code\n\tcorrupted key event dictionary\n\thex key code dictionary incomplete')


def masking_dict():
    """
    Teensy uses different masks and values for different keys

    The Virtual Key numbers are mapped to a Teensy Key code
    - Found in vk_key_mappings.txt, created by hand
    This Teensy key code is then mapped to a hex value
    - Found in teensy_key_definitions.txt, copied from the first part of:
      https://github.com/PaulStoffregen/cores/blob/master/teensy/keylayouts.h


    :return: dictionary of virtual key to a list of teensy key name, and hex value
    """

    vk_map = resource_filename(__name__, 'vk_key_mappings.txt')
    hex_map = resource_filename(__name__, 'teensy_key_definitions.txt')

    mask_dict = {}
    with open(vk_map, 'r') as f:
        for line in f.readlines():
            temp_str = re.sub(r'[\ ]+', ' ', line)
            temp_str = re.sub(r'\n','', temp_str)
            mask_dict[int(temp_str.split(' ')[0])] = [temp_str.split(' ')[1]]

    hex_dict = {}
    with open(hex_map, 'r') as f:
        for line in f.readlines():
            temp_str = re.sub(r'[\ ]+', ' ', line)
            string_part = temp_str.split(' ')
            if 'x' in string_part[3]:
                hex_dict[string_part[1]] = hex(int(string_part[3], 16) + int(string_part[5], 16))
                # Have to convert two hex numbers
            else:
                hex_dict[string_part[1]] = hex(int(string_part[3]) + int(string_part[5], 16))
                # First number is an integer in base 10 already


    for key in mask_dict.keys():
        if mask_dict[key][0] == 'None':
            mask_dict[key].append('None')
            continue
        mask_dict[key].append(hex_dict[mask_dict[key][0]])

    return mask_dict

masking_dict()