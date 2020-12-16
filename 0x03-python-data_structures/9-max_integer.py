#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maxv = 0
        for i in range(len(my_list)):
            if my_list[i] > maxv:
                maxv = my_list[i]
        return maxv
    else:
        return None