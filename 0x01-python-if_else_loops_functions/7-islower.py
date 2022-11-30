#!/usr/bin/env python3

def islower(c):
    for number in range(97, 123):
        if chr(number) == c:
            return True
        elif number == 122 and chr(number) != c:
            return False
        else:
            continue
