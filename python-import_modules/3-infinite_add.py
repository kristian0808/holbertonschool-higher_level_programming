#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    if num_args == 0:
        print("0")
    else:
        sum = 0
        for i in range(1, num_args + 1):
            sum = sum + int(argv[i])
        print("{}".format(sum))
