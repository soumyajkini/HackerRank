#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    i = 0
    l = len(c)
    
    while (i < l):
        if (i+2 < l):
            if (c[i+2] == 0): 
                #First check for 2 pos jump
                jumps += 1
                i += 2
            else: 
                #If 2 pos jump is not possible, then do a 1 pos jump
                jumps += 1
                i += 1
        elif (i+1 < l):
            jumps += 1
            i += 1
        else:
            break
    return jumps

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)

    #fptr.write(str(result) + '\n')

    #fptr.close()
