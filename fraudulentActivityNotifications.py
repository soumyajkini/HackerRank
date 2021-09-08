#!/bin/python

import math
import os
import random
import re
import sys

def getMedian(trailing, d):
    trailing = sorted(trailing)
    print trailing, trailing[(d-1)/2], trailing[d/2], d
    if d % 2 != 0: return float(trailing[d/2])
    else: return float((trailing[(d-1)/2] + trailing[d/2]) / 2.0)
        
# Complete the activityNotifications function below.
def activityNotifications(expenditures, d):
    
    notices = 0
    trailing = expenditures[0:d]
    median = getMedian(trailing, d)
    
    print expenditures, trailing
    for i in range(d, len(expenditures)):
        trailing = (trailing[1:d])
        if (expenditures[i] >= 2*median): notices += 1
    print notices
    return notices

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = map(int, raw_input().rstrip().split())

    result = activityNotifications(expenditure, d)

    #fptr.write(str(result) + '\n')

    #fptr.close()
