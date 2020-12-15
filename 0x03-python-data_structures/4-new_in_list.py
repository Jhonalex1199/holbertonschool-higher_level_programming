#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (my_list):
        x = len(my_list)
        my_list2 = my_list.copy()
        if (idx < 0 or idx >= x):
            return (my_list2)
        i = 0
        while (i <= idx):
            if (i == idx):
                my_list2[idx] = element
            i += 1
        return (my_list2)
