#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = "Last digit of {} is {} {}"
b = abs(number) % 10
if b > 5:
    print(a.format(number, b, 'and is greater than 5'))
elif b < 6 and b != 0:
    print(a.format(number, b, 'and is less than 6 and not 0'))
elif b == 0:
    print(a.format(number, b, 'and is 0'))
