#!/usr/bin/env python
"""
Password Generator
"""
__author__ = "Glen Coulter"
__version__ = "0.1"
__license__ = MIT

import random
import string
def main():
    charset = string.printable
    length = input("Please input password length: ")
    paswd=""
    for n in range(length):
        ni = random.randrange(len(charset))
        paswd = paswd + charset[ni]
    print(paswd)
if __name__ == "__main__":
    main()
