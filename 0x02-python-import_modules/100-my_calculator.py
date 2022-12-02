#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    print(len(argv) - 1)
    if len(argv) != 4:
        if (argv[3]):
            mult = True
        else:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            exit(1)
    op = argv[2]
    a = argv[1]
    b = argv[3]
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if op == '+':
        print("{0} {1} {2} = {3}".format(a, op, b, add(int(a), int(b))))
        exit(0)
    elif op == '-':
        print("{0} {1} {2} = {3}".format(a, op, b, sub(int(a), int(b))))
        exit(0)
    elif op == '*':
        print("{0} {1} {2} = {3}".format(a, op, b, mul(int(a), int(b))))
        exit(0)
    elif op == '/':
        print("{0} {1} {2} = {3}".format(a, op, b, div(int(a), int(b))))
        exit(0)
