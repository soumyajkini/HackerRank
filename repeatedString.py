#!/bin/python

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    l = len(s)

    div = n / l #To find len of repeated string
    rem = n % l #To get remaining part of string
    sub = s[0:rem] #To get substring of remaining part
    
    count = s.count('a') + sub.count('a')
    print count
    
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    #fptr.write(str(result) + '\n')

    #fptr.close()
