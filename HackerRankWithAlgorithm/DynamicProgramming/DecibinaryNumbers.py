from typing import List
import re
import math

class DecibinaryNumbersSolution:
    def __init__(self, x):
        self.x = x

    def calc_value_decimal(self):

        order:int = 0

        dp:List[List[int]] = [[0 for _ in range(17)] for i in range(17)]

        dp[0][0] = 1
        dp[1][0] = 1

