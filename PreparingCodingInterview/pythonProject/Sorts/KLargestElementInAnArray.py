from typing import List


class MaxHeap:
    def __init__(self, nums: List[int] | None = None):

        self.nums: List[int] = nums if nums else []
        self._heap: List[int] = [-1]
        self.size: int = 0

    def heapify(self):
        for e in self.nums:
            self.push(e)

    def push(self, u: int):
        self.size += 1
        self._heap.append(u)

        cur_p = self.size

        while cur_p > 1:
            par_p = cur_p // 2

            if self._heap[par_p] < self._heap[cur_p]:
                self._heap[par_p], self._heap[cur_p] = self._heap[cur_p], self._heap[par_p]
                cur_p = par_p
            else:
                break

    def pop(self) -> int | None:
        if self.size == 0:
            return None
        self._heap[1], self._heap[self.size] = self._heap[self.size], self._heap[1]

        max_heap = self._heap.pop()
        self.size -= 1
        cur_p = 1

        while (cur_p << 1) + 1 <= self.size:
            left_p, right_p = cur_p << 1, (cur_p << 1) + 1

            max_e = max(self._heap[cur_p], self._heap[left_p], self._heap[right_p])

            if max_e == self._heap[cur_p]:
                break
            elif max_e == self._heap[left_p]:
                self._heap[cur_p], self._heap[left_p] = self._heap[left_p], self._heap[cur_p]
                cur_p = left_p
            elif max_e == self._heap[right_p]:
                self._heap[cur_p], self._heap[right_p] = self._heap[right_p], self._heap[cur_p]
                cur_p = right_p

        if (cur_p << 1) <= self.size and self._heap[cur_p] < self._heap[cur_p << 1]:
            self._heap[cur_p], self._heap[cur_p << 1] = self._heap[cur_p << 1], self._heap[cur_p]

        return max_heap


class MaxHeapSolution:
    def __init__(self, nums: List[int], k: int):
        self.nums: List[int] = nums
        self.k: int = k

    def solve(self) -> int | None:
        max_heap = MaxHeap(self.nums)
        max_heap.heapify()
        k_largest = 0

        for _ in range(self.k):
            k_largest = max_heap.pop()

        return k_largest


class PartitionSolution:
    def __init__(self, nums: List[int], k: int):
        self.nums: List[int] = nums
        self.k: int = k

    def partition(self, low: int, high: int, k: int) -> int | None:

        if low >= high:
            return low if k == low else None

        pivot = self.nums[low]

        first_p, last_p = low + 1, high

        while first_p <= last_p:

            if self.nums[first_p] <= pivot < self.nums[last_p]:
                self.nums[first_p], self.nums[last_p] = self.nums[last_p], self.nums[first_p]
                first_p += 1
                last_p -= 1
            elif self.nums[first_p] > pivot:
                first_p += 1
            elif self.nums[last_p] <= pivot:
                last_p -= 1
            else:
                break

        self.nums[low], self.nums[first_p - 1] = self.nums[first_p-1], self.nums[low]

        pivot_idx = first_p - 1

        if pivot_idx == k:
            return self.nums[pivot_idx]
        elif pivot_idx < k:
            return self.partition(pivot_idx + 1, high, k)

        return self.partition(low, pivot_idx - 1, k)

    def solve(self) -> int | None:
        return self.partition(0, len(self.nums) - 1, self.k-1)


nums1 = [3,2,1,5,6,4]
k = 2

heap_sln = MaxHeapSolution(nums1, k)
prt_sln = PartitionSolution(nums1, k)
print(prt_sln.solve())
