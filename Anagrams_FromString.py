#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def sherlockAndAnagrams(s):
    substrings = [''.join(sorted(s[i:j+1])) for i in range(len(s)) for j in range(i, len(s))]
    return sum([(v*(v-1))//2 for _, v in Counter(substrings).most_common()])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
