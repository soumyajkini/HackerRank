#!/bin/python

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices = sorted(filter(lambda x: x <= k, prices))
    
    print prices
    
    sum = 0
    count = 0
    for item in prices:
        if (sum + item) <= k: 
            count += 1
            sum += item
    
    print count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = map(int, raw_input().rstrip().split())

    result = maximumToys(prices, k)

    #fptr.write(str(result) + '\n')

    #fptr.close()
