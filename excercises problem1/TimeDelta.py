#!/bin/python3

import math
import os
import random
import re
import sys
import datetime
import dateutil.parser

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1 = dateutil.parser.parse(t1,fuzzy=True)
    t2 = dateutil.parser.parse(t2,fuzzy=True)
    return str(int(abs(t1-t2).total_seconds()))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
