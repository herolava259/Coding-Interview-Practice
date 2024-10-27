from typing import List
from collections import Counter


class TopKFrequentSolution:
    def __init__(self, nums: List[int], k: int):
        self.nums: List[int] = nums
        self.k: int = k

    def solve(self) -> List[int]:
        freqs = Counter(self.nums)

        return list(map(lambda c: c[0], freqs.most_common(self.k)))
