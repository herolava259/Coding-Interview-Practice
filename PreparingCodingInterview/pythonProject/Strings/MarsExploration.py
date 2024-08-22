import math
import os
import random
import os
import re
import sys

def marsExploration(s):
    default_str = 'SOS'
    num_diff = 0
    for i in range(0, len(s)-2, 3):
        for j in range(3):
            if default_str[j] != s[i + j]:
                num_diff += 1

    return num_diff


input = 'SOSSPSSQSSOR'


print(marsExploration(input))

