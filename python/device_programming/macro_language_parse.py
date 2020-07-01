"""
This takes in the key events given by the main_page methods and parses it to a .wkm file

The file structure looks like this
---------------------
syntax = "proto3";

package windy.keyboards;

message Macro {
    repeated Micro micros = 1;
}

message Micro {
    oneof action {
        int32 delay = 1;
        byte press = 2;
        byte release = 3;
    }
}
---------------------

Currently using the teensy library to interface with a machine
As such the identities of keys are masked hex as shown here:
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
from pkg_resources import resource_filename  # to read the text files in the module


def create_macro_string(key_events):
    mask_dict = masking_dict()

    buf_per_key ={}
    try:
        for button_num in sorted(key_events.keys()):
            protobuf = []
            protobuf.append('syntax = "proto3";')
            protobuf.append('package windy.keyboards;')
            protobuf.append('message Macro {repeated Micro micros = '  + str(button_num) + ';}')

            prev_time = 0
            for key_entry in key_events[button_num]['key_events']:
                macro_string = 'message Micro { oneof action { '
                wait_time = float(key_entry.time) * 1000 - prev_time
                prev_time = float(key_entry.time) * 1000
                key_action = key_entry.event_type
                if key_action =='down':
                    macro_string = macro_string + 'byte press ='
                if key_action == 'up':
                    macro_string = macro_string + 'byte release ='
                key = key_entry.scan_code
                # vk_code = get_vk(key)
                hex_code = mask_dict[key][-1]
                if hex_code == -1:
                    print('Sorry, but the key code \"{0}\" is not currently supported'.format(vk_code))
                    print('Please direct this error to https://github.com/windykeyboards/southerly-front')
                    continue
                macro_string = macro_string + hex_code + ';}}'

                # Add timing after the fact
                delay_string = 'message Micro { oneof action {int32 delay = ' + str(int(wait_time)) + ';}}'
                protobuf.append(macro_string)
                protobuf.append(delay_string)
            buf_per_key[button_num] = protobuf

    except:
        print('Unable to parse macro to macro string\nPossible Issues:\n')
        print('\tUnknown key code\n\tcorrupted key event dictionary\n\thex key code dictionary incomplete')
    print('\n'.join(protobuf))

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

    vk_map = resource_filename(__name__, 'scan_code_mappings.txt')
    hex_map = resource_filename(__name__, 'teensy_key_definitions.txt')

    mask_dict = {}
    with open(vk_map, 'r') as f:
        for line in f.readlines():
            temp_str = re.sub(r'[\ ]+', ' ', line)
            temp_str = re.sub(r'\n', '', temp_str)
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
