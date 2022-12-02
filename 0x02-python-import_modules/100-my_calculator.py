#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = argv[2]
    a = argv[1]
    b = argv[3]
    if operator != '+' and operator != '-' and
    operator != '*' and operator != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if operator == '+':
        print("{0} {1} {2} = {3}".format(a, operator, b, add(int(a), int(b))))
        exit(0)
    elif operator == '-':
        print("{0} {1} {2} = {3}".format(a, operator, b, sub(int(a), int(b))))
        exit(0)
    elif operator == '*':
        print("{0} {1} {2} = {3}".format(a, operator, b, mul(int(a), int(b))))
        exit(0)
    elif operator == '/':
        print("{0} {1} {2} = {3}".format(a, operator, b, div(int(a), int(b))))
        exit(0)
