#!/bin/python3

import math
import os
import random
import re
import sys

def hourglassSum(arr):

    smax = 0
    for row in range((len(arr) - 2)):
     for col in range((len(arr[row]) - 2)):
          sum = 0;
          
          sum += arr[row][col];
          sum += arr[row][col + 1];
          sum += arr[row][col + 2];
          sum += arr[row + 1][col + 1];
          sum += arr[row + 2][col]; 
          sum += arr[row + 2][col + 1];
          sum += arr[row + 2][col + 2];
          
          smax = max(sum,smax)
    return smax
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
