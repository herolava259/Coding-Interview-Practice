from typing import List, DefaultDict
from collections import defaultdict


class LongestSubsequenceSolution:
    def __init__(self, arr: List[int], difference: int):
        self.arr: List[int] = arr
        self.difference: int = difference

    def solve(self) -> int:
        dp: DefaultDict[int, int] = defaultdict(lambda: 0)

        max_len = 0

        for elem in self.arr:
            dp[elem] = max(dp[elem], dp[elem - self.difference] + 1)
            max_len = max(dp[elem], max_len)

        return max_len


arr1 = [1,5,7,8,5,3,4,2,1]
difference1 = -2

sln = LongestSubsequenceSolution(arr1, difference1)

print(sln.solve())
