#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:  # ASCII values for lowercase letters
            char = chr(ord(char) - 32)  # Convert to uppercase
        print("{}".format(char), end="")


print(uppercase("best"))
print(uppercase("Best School 98 Battery street"))
