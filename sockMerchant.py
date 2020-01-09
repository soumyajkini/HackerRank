#!/bin/python

import math
import os
import random
import re
import sys

from itertools import groupby

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    res = 0
    for val in [len(list(group)) for key, group in groupby(sorted(ar))]:
        print val
        res += int(val / 2)
    return res


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    print(str(result) + '\n')
    #fptr.write(str(result) + '\n')

    #fptr.close()