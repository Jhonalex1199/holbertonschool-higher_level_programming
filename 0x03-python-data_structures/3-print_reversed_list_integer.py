#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    xlist = []
    xlist = my_list.copy()
    xlist.reverse()
    i = 0
    while (i < len(xlist)):
        print("{:d}".format(xlist[i]))
        i +=1
