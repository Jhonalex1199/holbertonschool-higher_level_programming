#!/usr/bin/python3
def roman_to_int(roman):
    num_r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0

    if roman is None or type(roman) != str:
        return 0

    for x in range(len(roman)):
        if x > 0 and num_r[roman[x]] > num_r[roman[x - 1]]:
            res += num_r[roman[x]] - 2 * num_r[roman[x - 1]]
        else:
            res += num_r[roman[x]]
    return res
