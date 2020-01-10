#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    
    i = 0
    while (i < len(arr)-1):
        if (arr[i] != i+1):
            temp = arr[i]
            arr[i], arr[temp-1] = arr[temp-1], arr[i]
            swaps += 1
        else:
            i += 1
    print swaps
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)

    #fptr.write(str(res) + '\n')

    #fptr.close()