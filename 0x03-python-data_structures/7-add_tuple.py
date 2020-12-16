#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list1 = [0, 0]
    list2 = [0, 0]

    lena = len(tuple_a)
    lenb = len(tuple_b)

    if lena > 2 or lenb > 2:
        lena = 2
        lenb = 2

    for i in range(lena):
        list1[i] += tuple_a[i]
    for j in range(lenb):
        list2[j] += tuple_b[j]

    return (list1[0] + list2[0], list1[1] + list2[1])
