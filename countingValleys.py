#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valley_count = 0
    valley = 0 # at sea level
    for i in s:
        if (i == 'D'): valley += 1 #every step down
        elif (i == 'U'): valley -= 1 #every step up
        if (valley == 0 and i == 'U'): # reaching back sea level (with a step up)
            valley_count += 1
    return valley_count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    print(str(result) + '\n')

   # fptr.close()
