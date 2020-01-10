#!/bin/python

import math
import os
import random
import re
import sys

def getMedian(expenditures, d):
    expenditures.sort()
    print d
    print expenditures
    if (d % 2 == 0):
        return (expenditures[d/2 - 1] + expenditures[d/2]) / 2
    else:
        return (expenditures[d/2])
        
# Complete the activityNotifications function below.
def activityNotifications(expenditures, d):
    
    for i in range(d, len(expenditures)):
        trailing = expenditures[i-d:i]
        print "Trailing", trailing
        print "Median", getMedian(trailing, d)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = map(int, raw_input().rstrip().split())

    result = activityNotifications(expenditure, d)

    #fptr.write(str(result) + '\n')

    #fptr.close()
