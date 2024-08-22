import math
import os
import random
import re
import sys

def superReducedString(s):
    changed = True
    while changed:

        cur_idx = 0
        n = len(s)
        while cur_idx < n-1:
            if s[cur_idx] == s[cur_idx+1]:
                break
            cur_idx += 1

        if cur_idx < n-1 and s[cur_idx] == s[cur_idx+1]:
            s = s[:cur_idx] + s[cur_idx + 2:]
            changed = True
        else:
            changed = False

    if s == '':
        return 'Empty String'
    else:
        return s

input = 'baab'

print(superReducedString(input))