#!/bin/python3

import math
import os
import random
import re
import sys

def repeatedString(s, n):
    c1 = s.count("a")
    c2 = c1*(n//len(s))

    c2 += s[:n % len(s)].count("a")
    return c2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
