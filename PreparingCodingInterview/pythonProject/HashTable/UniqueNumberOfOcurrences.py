from typing import List
from collections import defaultdict, Counter


class UniqueOccurrencesSolution:
    def __init__(self, arr: List[int]):
        self.arr: List[int] = arr

    def solve(self) -> bool:

        freq: Counter = Counter(self.arr)
        existed: defaultdict = defaultdict(bool)
        for k in freq.keys():
            if existed[freq[k]]:
                return False
            existed[freq[k]] = True

        return True
