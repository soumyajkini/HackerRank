#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swaps = 0
    for i in range(0, len(a)):
        for j in range(0, len(a)-1):
            print i, j, j+1, swaps
            if (a[j] > a[j + 1]):
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
            print a
    print "Array is sorted in %d swaps." %(swaps)
    print "First Element: ", a[0]
    print "Last Element: ", a[len(a)-1]

if __name__ == '__main__':
    n = int(raw_input())

    a = map(int, raw_input().rstrip().split())

    countSwaps(a)
