#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    num_threads = 100
    rows = len(queries)
    
    for i in range(rows):
        if queries[i][1] - queries[i][0] > num_threads:
            pass


def arrayParallelize(narr, val, start, end):
    for j in range(start, end):
        narr[j] += val


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
