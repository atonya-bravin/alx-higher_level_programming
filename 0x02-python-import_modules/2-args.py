#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        str = "arguments."
        print("{0} {1}".format((len(sys.argv) - 1), str))
    elif len(sys.argv) == 2:
        str = "argument:"
        print("{0} {1}".format((len(sys.argv) - 1), str))
    elif len(sys.argv) > 2:
        str = "arguments:"
        print("{0} {1}".format((len(sys.argv) - 1), str))
    for index in range(1, len(sys.argv)):
        argument = (sys.argv)[index]
        print("{0}: {1}".format(index, argument))
