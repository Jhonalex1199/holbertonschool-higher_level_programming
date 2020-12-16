#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maxv = my_list[0]
        for i in my_list:
            if i > maxv:
                maxv = i
        return maxv
    else:
        return None
