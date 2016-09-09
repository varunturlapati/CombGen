__author__ = 'Varun'

import os
import combinations_generator
#import openpyxl

source_csv_parent = "C:\Users\Varun\Desktop\Datos Rough"
source_csv_filename = "input_params_values.csv"
#source_csv_filename = "input_params_values_diff.xls"
source = source_csv_parent + "\\" + source_csv_filename


if not os.path.isfile(source):
    print("Your file doesn't exist. Quitting!")
    exit(-1)
else:
    sfh = open(source, 'r')
    in_dict = {}
    csv_lines = sfh.readlines()
    for my_line in csv_lines:
        my_line.replace("\n", "")
        my_list = my_line.split(",")
        my_key = my_list.pop(0)
        print my_list
        #my_list[-1].strip("\n")
        last_elem = my_list.pop().replace("\n", "")
        my_list.append(last_elem)
        print my_list
        in_dict[my_key] = my_list
    combinations_generator.cgen(in_dict)
