__author__ = 'Varun'

import csv
import os
from itertools import combinations, chain

GB_TO_KB = 1024 * 1024
MB_TO_KB = 1024
MIN_TO_SEC = 60
HOUR_TO_SEC = 3600
DAY_TO_SEC = 24 * 3600

param_list = [
    {'init_db_size_in_GB_list': [1, 10]},
    {'doc_size_in_KB_list': [1, 1024]},
    {'source_change_rate_in_MBPS_list': [0.1, 10]},
    {'num_schedules_per_policy_list': [1, 3]},
    {'retention_time_in_hours_list': [4, 8]},
    {'num_dbs_list': [1, 5]},
    {'num_coll_per_db_list': [1, 5]},
    {'num_shards_list': [1, 2]}
]
#{'version_interval_min_list': [15, 60]},


def gen_csv():
    """
    os.chdir("C:\Users\Varun\Desktop\Datos Rough")
    num_of_combinations = 1
    for count in range(len(param_list)):
        my_dict = param_list[count]
        temp_list = my_dict.values()[0]
        temp_list_len = len(temp_list)
        num_of_combinations = num_of_combinations * temp_list_len
    my_lines = []
    for i in range(num_of_combinations):
        my_lines[i] = ""
    #with open('MiniMVPRunsParams.csv', 'wb') as csvfile:
    #    my_csv = csv.writer(csvfile, delimiter=',')
    """
    print("Hi Varun!")

if __name__ == "__main__":
    gen_csv()
