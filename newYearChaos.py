#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    for ind, p in enumerate(q):
        print ind, p
        if (p - 1 - ind > 2):
            print "Too chaotic"
            return
        print q[max(p-2, 0):ind]
        bribes += sum(i > p for i in q[max(p-2, 0):ind])
    print bribes
    
if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)