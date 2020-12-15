#!/usr/bin/python3
def element_at(my_list, idx):
    x = len(my_list)
    if (idx < 0 or idx >= x):
        return (None)
    i = 0
    while (i <= idx):
        if (i == idx):
            return (my_list[i])
        i += 1
