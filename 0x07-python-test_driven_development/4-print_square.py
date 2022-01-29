#!/usr/bin/python3
''' contains a function that prints a square with the character # '''


def print_square(size):
    ''' function that prints a square with the character # '''

    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size == 0:
        None
    else:
        for i in range(size):
            for e in range(size):
                print('#', end='')
            print()
