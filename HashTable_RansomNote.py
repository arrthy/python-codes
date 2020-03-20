
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def checkMagazine(magazine, note):
    result = (Counter(note) - Counter(magazine)) == {}
    if(result):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
