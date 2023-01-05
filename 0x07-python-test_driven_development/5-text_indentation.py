#!/usr/bin/python3

"""
    prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
        text_indentation - takes in a text and prints 2 new lines
        after each of the characters ., ? and :

        args:
            text: the text to act on

    """

    if type(text) != str:
        raise TypeError("text must be a string")

    for character in text:
        print(character, end="")
        if character in ('.', '?', ':'):
            print("\n")
