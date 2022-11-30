#!/usr/bin/python3
for number in range(0, 100):
    if number != 99:
        if number < 10:
            str = '0{0}, '
        else:
            str = '{0}, '
    elif number == 99:
        str = '{0}\n'
    print(str.format(number), end="")
