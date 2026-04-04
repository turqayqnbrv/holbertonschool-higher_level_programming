#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_count = len(sys.argv) - 1
    
    # Print the header line
    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(arg_count))
    
    # Print each argument with its position
    for i in range(1, arg_count + 1):
        print("{:d}: {}".format(i, sys.argv[i]))
