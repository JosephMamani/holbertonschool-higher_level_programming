#!/usr/bin/python3
#fr num in range(0, 99):
#prnt("{}, ".format(str(num).zfill(2)), end='')
for num in range(0, 99):
    print(str(num).rjust(2, '0'), end=', ')
print('99\n')
