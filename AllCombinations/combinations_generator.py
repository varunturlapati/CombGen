__author__ = 'Varun'
import os


def cgen(hash_of_lists):
    """
    hash_of_lists = {
        "l1": ["a", "b", "c"],
        "l2": ["0", "1"],
        "l3": ["p", "q", "r", "s", "t"],
        "l4": ["yes", "no"]
    }
    hash_of_lists = {
        "l1": range(0, 10, 1),
        "l3": ["p", "q", "r", "s", "t"],
        "l4": ["yes", "no"],
        "l5": range(111, 666, 111),
        "l6": [True, False]
    }
    """
    """
    Example: list1 = [0,1], list2 = [0,1], list3 = [0,1]
    Combinations -->
                            ---	0	0	0
            repeat_factor	|	0	0	1
                            |	0	1	0
                            ---	0	1	1
                                1	0	0
                                1	0	1
                                1	1	0
                                1	1	1
    """
    param_list = hash_of_lists.keys()
    num_lists = len(param_list)		# O(n) implicitly but should I worry about this or does Python worry about it?
    scratch_hash = {}
    combinations = 1

    for k1 in hash_of_lists.keys():     # O(n^2)
        scratch_hash[k1] = {}
        scratch_hash[k1]["length"] = len(hash_of_lists[k1])		# Implicitly O(n)
        combinations = combinations * scratch_hash[k1]["length"]
    print "Combinations = %s" % combinations

    prev_list_count = 1		# For 1st list, prev list is NA. So leave this as 1
    repeat_factor = 1
    scratch_matrix = []

    for params in range(num_lists):		# O(n) and explore if this explicit initialization is necessary
        scratch_matrix.append([])
    # print(str(scratch_matrix))	#Initialized scratch_matrix
    i = 0   # To track row numbers corresponding to param type for indexed access
    for my_list in param_list:		# For each list
        # scratch_matrix[i] = []
        # print("List is %s" % my_list)
        repeat_factor = repeat_factor * prev_list_count

        # Repeat_factor of param P (a picked list)= N1 * N2 * ... * NP-1
        # Once you pick a list, the number of times you execute a repeated pattern = combinations/repeat_factor
        for j in range(combinations/(scratch_hash[my_list]["length"]*repeat_factor)):
            for elem in hash_of_lists[my_list]:
                # print("Element is %s" % elem)
                for k in range(repeat_factor):
                    scratch_matrix[i].append(str(elem))     # Consider if we want to convert to string here itself
        prev_list_count = scratch_hash[my_list]["length"]
        i += 1
    # print str(scratch_matrix)

    # Transpose because I wrote this row-wise. Can be avoided if I can write column-wise directly.
    uber_matrix = zip(*scratch_matrix)
    """
    for r in range(num_lists):
        for c in range(combinations):
            print("%s <--> %s" % (scratch_matrix[r][c], scratch_matrix[c][r]))
            temp = scratch_matrix[r][c]
            scratch_matrix[r][c] = scratch_matrix[c][r]
            scratch_matrix[c][r] = temp
    """
    my_file_name = "varun_combinations"
    my_dest = "C:\Users\Varun\Desktop\Datos Rough"
    flag = True
    suffix = 1
    my_path = my_dest + "\\" + my_file_name
    print my_path

    while flag:
        if os.path.isfile(my_path + ".csv"):
            my_path += str(suffix)
            suffix += 1
        flag = False

    cfh = open(my_path + ".csv", 'w')

    header_row = ",".join(param_list)
    cfh.writelines(header_row + "\n")
    for comb in range(combinations):
        my_line = ",".join(uber_matrix[comb])
        cfh.writelines(my_line + "\n")
