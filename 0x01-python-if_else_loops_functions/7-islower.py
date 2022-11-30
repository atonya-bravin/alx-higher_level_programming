#!/usr/bin/python3

def islower(c):
    for number in range(97, 123):
        if chr(number) == c:
            return True
        else:
            continue
    for number in range(65, 91):
        if chr(number) == c:
            return False
        else:
            continue
    return False
