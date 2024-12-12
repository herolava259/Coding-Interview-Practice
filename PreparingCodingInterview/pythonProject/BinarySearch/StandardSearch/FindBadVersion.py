from typing import List

def isBadVersion(version) -> int:
    return 0

class FirstBadFinder:
    def __init__(self, n: int):
        self.n = n

    def find(self) -> int:

        low, high = 0, self.n

        while low < high:
            mid = (low + high) // 2

            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1

        return low

