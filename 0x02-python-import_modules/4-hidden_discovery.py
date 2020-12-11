#!/usr/bin/python3

if __name__ == '__main__':
    import hidden_4
    x = dir(hidden_4)
    for i in x:
        if x[0] != '__':
            print(x)
