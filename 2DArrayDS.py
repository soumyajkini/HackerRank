#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):

    row = 0 # To get each 3 rows
    
    result = []
    while (row+2 < len(arr)):
        col = 0 # For each 3 columns
        result.append([])
        while (col+2 < len(arr[row])):
            sum = 0 # Sum of each hourglass
            i = 0 # To count current row being added
            for r in arr[row:row+3]:            
                j = 0 # To count current column
                for c in r[col:col+3]:                    
                    if (i != 1 or (j != 0 and j != 2)):
                        sum += c                        
                    j += 1
                i += 1
            result[row].append(sum)
            col += 1
        row += 1
    print result
    return max([max(num) for num in result])
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    #fptr.write(str(result) + '\n')

    #fptr.close()