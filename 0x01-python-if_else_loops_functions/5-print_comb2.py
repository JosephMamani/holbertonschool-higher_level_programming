#!/usr/bin/python3
a = list(range(0, 99))
for num in a:
    print(str(num).rjust(2, '0'), end=',')
print(99)
