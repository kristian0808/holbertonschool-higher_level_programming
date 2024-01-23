#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:  # ASCII values for lowercase letters
            c = chr(ord(c) - 32)  # Convert to uppercase
        print("{}".format(c), end="")
    print()
