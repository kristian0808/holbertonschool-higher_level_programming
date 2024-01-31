#!/usr/bin/python3


def safe_print_integer(value):
    try:
        if isinstance(value, set):
            for val in value:
                print("{:d}".format(val), end="")
            print()
        else:
            print("{:d}".format(value))
        return True
    except ValueError:
        return False
