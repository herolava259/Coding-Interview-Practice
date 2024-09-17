import math
import os
import random
import re
import sys

def bricksGame(arr):

    n = len(arr)

    dp = [[0,0] for i in range(n)]

    if n <= 3:
        return sum(arr)

    arr = arr[::-1]

    dp[0][0] = arr[0]
    dp[0][1] = 0

    dp[1][0] = arr[0] + arr[1]
    dp[1][1] = 0

    dp[2][0] = arr[0] + arr[1] + arr[2]
    dp[2][1] = 0

    for i in range(3,n):
        maxs = [arr[i]+dp[i-1][1], arr[i]+arr[i-1]+dp[i-2][1], arr[i]+arr[i-1]+arr[i-2]+ dp[i-3][1]]
        max_idx = max(range(3), key = lambda x: maxs[x])
        dp[i][0] = maxs[max_idx]
        dp[i][1] = dp[i-max_idx-1][0]

    return dp[n-1][0]


arr =  [999, 1, 1, 1, 0]#[0,1,1,1,999], [1,2,3,4,5] [999, 1, 1, 1, 0]

print(bricksGame(arr))