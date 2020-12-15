#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (my_list):
        x = len(my_list)
        if (idx < 0 or idx >= x):
            return (my_list)
        i = 0
        while (i <= idx):
            if (i == idx):
                my_list[idx] = element
            i += 1
        return (my_list)
        my_list.insert(idx, element)
        return (my_list)
