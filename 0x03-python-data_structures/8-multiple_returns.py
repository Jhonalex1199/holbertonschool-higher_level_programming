#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        tuple = (len(sentence), sentence[0])
    else:
        tuple = len(sentence), None
    return tuple
