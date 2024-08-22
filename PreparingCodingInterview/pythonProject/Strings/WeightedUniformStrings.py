import math
import os
import re
import random
import re
import sys
from collections import defaultdict

def weightedUniformStrings(s, queries):
    min_val = ord('a') - 1
    dic = defaultdict(int)
    curr = s[0]
    beg = 0
    end = 0
    s += '@'
    for idx, nxt in enumerate(s[1:]):
        if curr == nxt:
            end = idx + 1
        else:
            dic[curr] = max(len(s[beg: end+1]), dic[curr])
            curr = nxt
            beg = idx + 1
            end = idx + 1

    values = dic.values()
    print(dic)
    result = []
    for q in queries:
        check = True
        for k in dic.keys():
            val = ord(k) - min_val
            if q % val == 0 and (q // val) <= dic[k]:
                result.append("Yes")
                check = False
                break
        if check:
            result.append('No')

    return result

input_s = 'aaabbbbcccddd'
input_queries = [1, 3, 12, 5, 9, 10]

print(weightedUniformStrings(input_s, input_queries))



