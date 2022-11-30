#!/usr/bin/python3
for outer_number in range(0, 9):
    for inner_number in range((outer_number + 1), 10):
        if outer_number == 8:
            str = '{0}{1}'
        else:
            str = '{0}{1}, '
        print(str.format(outer_number, inner_number), end="")
print()
