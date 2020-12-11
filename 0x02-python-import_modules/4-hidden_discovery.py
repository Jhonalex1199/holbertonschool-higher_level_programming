#!/usr/bin/python3
import hidden_4

x = dir(hidden_4)
if __name__ == '__main__':
    for i in x:
        if i[0] != '_':
            print(i)
