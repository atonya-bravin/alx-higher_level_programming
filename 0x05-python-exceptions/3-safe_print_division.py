#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        a *= 1.0
        result = (a / b)
    except ZeroDivisionError:
        result = None
    finally:
        print('Inside result: {}'.format(result))
        return result
