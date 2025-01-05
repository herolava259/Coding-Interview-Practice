import math
import os
import random
import re
import sys
from typing import List


class DecibinaryNumber:
    def __init__(self, n_character: int, value: int, arr: List[int] = None):
        self.n = n_character
        self.value = value
        if arr is None:
            self.digits = [0 for _ in range(self.n)]
        else:
            self.digits = arr


def decibinaryNumbers(x):
    factorials = factorials_arr(100)


def list_all_decibinary(n: int) -> List[DecibinaryNumber]:
    dp = {0: [DecibinaryNumber(12, 0, [0 for _ in range(12)])]}
    factorials = factorials_arr(20)
    max_decs = max_decibinary_by_digit(factorials)

    for i in range(1, n + 1):
        micro_dp: List[DecibinaryNumber] = []
        min_idx = 0
        while min_idx < 12 and i > max_decs[min_idx]:
            min_idx += 1
        if i == n:
            print(min_idx)
        for ids in range(min_idx, 12):
            if i == 2:
                pass
            if factorials[ids] > i:
                break
            if ids == 0:
                tmp = DecibinaryNumber(12, i, [0 for _ in range(12)])
                tmp.digits[0] = i
                micro_dp.append(tmp)
                continue
            if i == 4:
                pass
            for j in range(1, 10):
                if j * factorials[ids] > i:
                    break
                micro_dp.extend(micro_list_decibinary(i, j, ids, dp[i - factorials[ids] * j]))
        dp[i] = micro_dp

    return dp[4]


def max_decibinary_by_digit(factorials) -> List[int]:
    res: List[int] = [9 * factorials[0]]
    for fac in factorials[1:]:
        res.append(res[-1] + 9 * fac)
    return res


def micro_list_decibinary(value: int, first_digit: int, order: int, decs: List[DecibinaryNumber]):
    res = []
    if value == 2:
        pass
    for dec in decs:
        res.append(create_new_decibinary_from(value, first_digit, order, dec))
    return res




def create_new_decibinary_from(value: int, largest_digit: int, order_digit: int, lower: DecibinaryNumber):

    if value == 2:
        pass
    res = DecibinaryNumber(12, value, list(lower.digits))

    res.digits[order_digit] = largest_digit

    return res


def factorials_arr(n: int) -> List:
    res = [1]
    for i in range(1, n + 1):
        res.append(res[-1] * 2)

    return res


inp = 4

out = list_all_decibinary(4)

for idx, o in enumerate(out):
    print('idx = ', idx)
    print('value = ', o.value)
    print(o.digits)
