#!/usr/bin/python3
for number in range(97, 123):
    str = '{0}'
    if chr(number) == 'q' or chr(number) == 'e':
        print("", end="")
    else:
        print(str.format(chr(number)), end="")
