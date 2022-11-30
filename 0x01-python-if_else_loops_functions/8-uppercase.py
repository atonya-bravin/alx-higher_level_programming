#!/usr/bin/python3
def uppercase(str):
    new_string = ""
    for index in range(len(str)):
        if ord(str[index]) >= 97 and ord(str[index]) <= 122:
            new_string += chr(65 + (ord(str[index]) - 97))
        else:
            new_string += str[index]
    print('{0}'.format(new_string))
