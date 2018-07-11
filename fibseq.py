#!/usr/bin/env python
"""
Password Generator
"""
__author__ = "Glen Coulter"
__version__ = "0.1"
__license__ = "MIT"

def main():
    sequence = input("How long would you like the sequence to be: ")
    n1 = 0
    n2 = 1
    count = 0
    end = ' , '
    while count < sequence:
       print n1
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
if __name__ == "__main__":
        main()
