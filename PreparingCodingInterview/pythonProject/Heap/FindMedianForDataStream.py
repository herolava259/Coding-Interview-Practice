from typing import List


class MinHeap:
    def __init__(self):
        self._heap: List[int] = [0 for _ in range(25001)]
        self.size: int = 0

    def push(self, x: int):

        self.size += 1
        self._heap[self.size] = x
        cur_p = self.size

        while cur_p > 1:

            par_p = cur_p // 2

            if self._heap[par_p] <= self._heap[cur_p]:
                break

            self._heap[par_p], self._heap[cur_p] = self._heap[cur_p], self._heap[par_p]
            cur_p = par_p

    def pop(self) -> int | None:

        if self.size == 0:
            return None

        self._heap[1], self._heap[self.size] = self._heap[self.size], self._heap[1]
        res = self._heap[self.size]
        self.size -= 1

        cur_p = 1

        while (cur_p << 1) + 1 <= self.size:
            left_p, right_p = cur_p << 1, (cur_p << 1) + 1

            cur_min = min(self._heap[cur_p], self._heap[left_p], self._heap[right_p])

            if cur_min == self._heap[cur_p]:
                break
            elif cur_min == self._heap[left_p]:
                self._heap[cur_p], self._heap[left_p] = self._heap[left_p], self._heap[cur_p]
                cur_p = left_p
            elif cur_min == self._heap[right_p]:
                self._heap[cur_p], self._heap[right_p] = self._heap[right_p], self._heap[cur_p]
                cur_p = right_p

        if (cur_p << 1) <= self.size and self._heap[cur_p << 1] < self._heap[cur_p]:
            self._heap[cur_p], self._heap[cur_p << 1] = self._heap[cur_p << 1], self._heap[cur_p]

        return res

    def peek(self) -> int | None:
        if self.size == 0:
            return 0

        return self._heap[1]

    def empty(self) -> bool:
        return self.size <= 0


class MaxHeap:
    def __init__(self):
        self._heap: List[int] = [0 for _ in range(25001)]
        self.size: int = 0

    def push(self, x: int):

        self.size += 1
        self._heap[self.size] = x
        cur_p = self.size

        while cur_p > 1:

            par_p = cur_p // 2

            if self._heap[par_p] >= self._heap[cur_p]:
                break

            self._heap[par_p], self._heap[cur_p] = self._heap[cur_p], self._heap[par_p]
            cur_p = par_p

    def pop(self) -> int | None:

        if self.size == 0:
            return None

        self._heap[1], self._heap[self.size] = self._heap[self.size], self._heap[1]
        res = self._heap[self.size]
        self.size -= 1

        cur_p = 1

        while (cur_p << 1) + 1 <= self.size:
            left_p, right_p = cur_p << 1, (cur_p << 1) + 1

            cur_min = max(self._heap[cur_p], self._heap[left_p], self._heap[right_p])

            if cur_min == self._heap[cur_p]:
                break
            elif cur_min == self._heap[left_p]:
                self._heap[cur_p], self._heap[left_p] = self._heap[left_p], self._heap[cur_p]
                cur_p = left_p
            elif cur_min == self._heap[right_p]:
                self._heap[cur_p], self._heap[right_p] = self._heap[right_p], self._heap[cur_p]
                cur_p = right_p

        if (cur_p << 1) <= self.size and self._heap[cur_p << 1] > self._heap[cur_p]:
            self._heap[cur_p], self._heap[cur_p << 1] = self._heap[cur_p << 1], self._heap[cur_p]

        return res

    def peek(self) -> int | None:
        if self.size == 0:
            return 0

        return self._heap[1]

    def empty(self) -> bool:
        return self.size <= 0


class MedianFinder:

    def __init__(self):
        self.lower_heap: MaxHeap = MaxHeap()
        self.upper_heap: MinHeap = MinHeap()
        self.size: int = 0

    def addNum(self, num: int) -> None:

        if self.size % 2 == 0:
            self.lower_heap.push(num)
            self.upper_heap.push(self.lower_heap.pop())
            self.size += 1
        else:
            self.upper_heap.push(num)
            self.lower_heap.push(self.upper_heap.pop())
            self.size += 1

    def findMedian(self) -> float:
        if self.size == 0:
            return 0.0

        if self.size % 2 == 1:
            return float(self.upper_heap.peek())

        return (self.lower_heap.peek() + self.upper_heap.peek()) / 2


med_finder = MedianFinder()
med_finder.addNum(1)
print(med_finder.findMedian())
med_finder.addNum(2)
print(med_finder.findMedian())
med_finder.addNum(3)
print(med_finder.findMedian())
