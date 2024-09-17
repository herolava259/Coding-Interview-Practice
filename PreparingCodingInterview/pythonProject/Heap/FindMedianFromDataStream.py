from typing import List


class MedianFilter:

    def __init__(self):
        self._heap: List[int] = [-1]
        self.size: int = 0

    def addNum(self, num: int) -> None:
        self._heap.append(num)
        self.size += 1

        cur_p = self.size

    def findMedian(self) -> float:
        if self.size % 2 == 0:
            return (self._heap[0] + self._heap[1]) / 2

        return float(self._heap[1])
