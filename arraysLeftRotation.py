#!/bin/python

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    l = len(a)
    if (l < d): 
        rem = l % d
        return a[l-rem:l] + (a[:l-rem])        
    else: 
        rem = d
        return a[rem:l] + (a[:rem])
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

    result = rotLeft(a, d)

    print result
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()