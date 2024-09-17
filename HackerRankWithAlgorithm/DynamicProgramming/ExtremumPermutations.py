import math
import os
import random
import re

UP = 1
DOWN = -1
ANY = 0
MODK = 1000000007
def solve(states, curr_idx, prev_val,max_val, dp, isChooses):
    if curr_idx < 0 :
        return 0
    if states[curr_idx] == ANY:
        return dp[curr_idx]
    total = 0
    first = 1
    last = max_val
    if states[curr_idx] == DOWN:
        first = prev_val+1
    else:
        last = prev_val-1

    for i in range(first, last+1):
        if not isChooses[i]:
            isChooses[i] = True
            total = (total + solve(states, curr_idx-1,i,max_val,dp,isChooses))%MODK
            isChooses[i] = False

    return total

def optimize_solve(prev_state, curr_idx,dp):
    curr_val = curr_idx + 1
    if curr_idx <= 0:
        return [0,1,0]



    curr_dp = [0 for i in range(curr_val+2)]

    if prev_state == UP:

        for i in range(1,curr_val+1):
            prev_val = i

            if i == 1:
                prev_val = 0
            else:
                prev_val = i-1

            prev_dp = dp[curr_idx-1][prev_val]

            curr_dp[i] = (prev_dp + curr_dp[i-1]) % MODK

    elif prev_state == DOWN:
        for i in range(curr_val,0,-1):
            prev_val = i
            prev_dp = 0

            if i == curr_val:
                prev_val = 0
            else:
                prev_val = i

            prev_dp = dp[curr_idx-1][prev_val]

            curr_dp[i] = (prev_dp + curr_dp[i+1]) % MODK
    else:
        total = 0

        for item in dp[curr_idx-1]:
            total = (total + item) % MODK
        for i in range(1,curr_val+1):
            curr_dp[i] = total

    return curr_dp

def countConstraintInterval(states, curr_idx, dp):

    if states[curr_idx] == ANY or curr_idx <= 0 :
        return (dp[curr_idx-1]*(curr_idx+1))%MODK if curr_idx > 0 else 1
    max_val = curr_idx + 1
    isChooses = [False for i in range(max_val+1)]


    curr_dp = 0

    for i in range(max_val,0,-1):
        isChooses[i] = True
        curr_dp += solve(states, curr_idx - 1, i,max_val, dp, isChooses)
        isChooses[i] = False

    return curr_dp


def extremumPermutations(n, a, b):

    states = [ANY for i in range(n+1)]

    for item in a:
        idx = item-1
        if states[idx-1] != UP and states[idx] != DOWN:
            states[idx-1] = DOWN
            states[idx] = UP
        else:
            return 0

    for item in b:
        idx = item - 1
        if states[idx-1] != DOWN and states[idx] != UP:
            states[idx-1] = UP
            states[idx] = DOWN
        else:
            return 0

    dp = []
    for i in range(n):
        dp.append(optimize_solve(ANY if i <= 0 else states[i-1], i, dp))

    res = 0

    for item in dp[n-1]:
        res = (res + item) % MODK

    return res

n = 4
a = [2]
b = [3]

print(extremumPermutations(n,a,b))