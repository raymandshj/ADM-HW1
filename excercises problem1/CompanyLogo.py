#!/bin/python3

import math
import os
import random
import re
import sys


from collections import Counter

if __name__ == '__main__':
    s = sorted(input())
    count_dict = Counter(s)
    for k, v in count_dict.most_common(3):
        print(k,v)
