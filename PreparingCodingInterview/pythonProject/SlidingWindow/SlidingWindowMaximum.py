from typing import List, Tuple


class MaxHeap:
    def __init__(self, n: int):
        self._heap: List[Tuple[int, int]] = [(0, 0) for _ in range(n + 4)]
        self.size: int = 0

    def push(self, x: int, idx: int):

        self.size += 1
        self._heap[self.size] = (x, idx)
        cur_p = self.size

        while cur_p > 1:

            par_p = cur_p // 2

            if self._heap[par_p][0] >= self._heap[cur_p][0]:
                break

            self._heap[par_p], self._heap[cur_p] = self._heap[cur_p], self._heap[par_p]
            cur_p = par_p

    def pop(self) -> Tuple[int, int] | None:

        if self.size == 0:
            return None

        self._heap[1], self._heap[self.size] = self._heap[self.size], self._heap[1]
        res = self._heap[self.size]
        self.size -= 1

        cur_p = 1

        while (cur_p << 1) + 1 <= self.size:
            left_p, right_p = cur_p << 1, (cur_p << 1) + 1

            cur_max = max(self._heap[cur_p][0], self._heap[left_p][0], self._heap[right_p][0])

            if cur_max == self._heap[cur_p][0]:
                break
            elif cur_max == self._heap[left_p][0]:
                self._heap[cur_p], self._heap[left_p] = self._heap[left_p], self._heap[cur_p]
                cur_p = left_p
            elif cur_max == self._heap[right_p][0]:
                self._heap[cur_p], self._heap[right_p] = self._heap[right_p], self._heap[cur_p]
                cur_p = right_p

        if (cur_p << 1) <= self.size and self._heap[cur_p << 1][0] > self._heap[cur_p][0]:
            self._heap[cur_p], self._heap[cur_p << 1] = self._heap[cur_p << 1], self._heap[cur_p]

        return res

    def peek(self) -> Tuple[int, int] | None:
        if self.size == 0:
            return -1, -1

        return self._heap[1]

    def empty(self) -> bool:
        return self.size <= 0


class SlidingWindowMaximumSolution:
    def __init__(self, nums: List[int], k: int):
        self.nums: List[int] = nums
        self.k: int = k

    def solve(self) -> List[int]:

        if self.k == 1:
            return self.nums
        n = len(self.nums)

        max_heap = MaxHeap(n)

        for i in range(self.k):
            max_heap.push(self.nums[i], i)

        max_windows: List[int] = [0] * (n - self.k + 1)
        max_windows[0] = max_heap.peek()[0]

        for i in range(self.k, n):

            beg_w, end_w = i - self.k + 1, i
            max_heap.push(self.nums[i], i)
            while max_heap.peek()[1] < beg_w:
                max_heap.pop()

            max_windows[beg_w] = max_heap.peek()[0]

        return max_windows


nums1 = [1]
k1 = 1

sln = SlidingWindowMaximumSolution(nums1, k1)

print(sln.solve())
