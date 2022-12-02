#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    print(len(sys.argv))
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = sys.argv[2]
    a = sys.argv[1]
    b = sys.argv[3]
    if operator != '+' and operator != '-' and operator != '*' and operator != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if operator == '+':
        print("{0} {1} {2} = {3}".format(a, operator, b, add(int(sys.argv[1]), int(sys.argv[3]))))
        exit(0)
    elif operator == '-':
        print("{0} {1} {2} = {3}".format(a, operator, b, sub(int(sys.argv[1]), int(sys.argv[3]))))
        exit(0)
    elif operator == '*':
        print("{0} {1} {2} = {3}".format(a, operator, b, mul(int(sys.argv[1]), int(sys.argv[3]))))
        exit(0)
    elif operator == '/':
        print("{0} {1} {2} = {3}".format(a, operator, b, div(int(sys.argv[1]), int(sys.argv[3]))))
        exit(0)
