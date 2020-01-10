#!/bin/python

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n+1)
    for q in queries:
        arr[q[0]] = arr[q[0]] + q[2]
        if (q[1] < n) : arr[q[1]+1] = arr[q[1]+1] - q[2] 
        print arr
    
    print sum([x for x in arr if x > 0])
    #return [sum(x) for x in arr if x > 0]
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))

    result = arrayManipulation(n, queries)

    #fptr.write(str(result) + '\n')

    #fptr.close()
