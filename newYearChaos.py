#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):

    bribes = 0
    for p in q:
        ind = q.index(p)
        if (p - ind > 3):
            print "Too chaotic"
            return
        bribes += sum(i < p for i in q[ind:])
    print bribes
    
if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)