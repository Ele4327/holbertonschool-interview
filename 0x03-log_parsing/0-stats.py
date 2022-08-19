#!/usr/bin/python3
"""
    Write a script that reads stdin line by line and computes metrics
"""

import sys

dict_status_code = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}

size = 0

cont_lines = 0

try:
    for line in sys.stdin:
        log = line.split(" ")

        if len(log) > 2:
            code_value = log[-2]
            size_val_temp = int(log[-1])

            if code_value in dict_status_code.keys():
                dict_status_code[code_value] = \
                    dict_status_code[code_value] + 1
            size = size + size_val_temp
            cont_lines = cont_lines + 1

        if (cont_lines % 10) == 0:
            print("File size: {:d}".format(size))

            for key in sorted(dict_status_code.keys()):
                if dict_status_code[key] == 0:
                    continue
                print("{}: {}".format(key, dict_status_code[key]))
            cont_lines = 0

except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(size))
    for key in sorted(dict_status_code.keys()):
        if dict_status_code[key] == 0:
            continue
        print("{}: {}".format(key, dict_status_code[key]))
