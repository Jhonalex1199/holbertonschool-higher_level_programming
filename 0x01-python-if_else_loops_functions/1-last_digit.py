#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Lastd = number % 10
if Lastd == 0:
    print('Last digit of {} is {} and is 0'.format(number, Lastd))
elif Lastd > 5:
    print('Last digit of {} is {} and is greater than 5'.format(number, Lastd))
elif Lastd != 0 and Lastd < 6:
    print('Last digit of', number, 'is', Lastd, 'and is less than 6 and not 0')
