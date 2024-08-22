from typing import List, Tuple


class MinHeap:
    def __init__(self):

        self._heap: List[Tuple[int, int, int, int, int, int]] = [(-1, -1, -1, -1, -1, -1)]
        self.size = 0

    def push(self, x: int, y: int, x_idx: int, y_idx: int, freq: int):

        self._heap.append((x + y, x, y, x_idx, y_idx, freq))
        self.size += 1

        cur_p = self.size

        while cur_p > 1:

            par_p = cur_p // 2

            if self._heap[cur_p][0] >= self._heap[par_p][0]:
                break
            self._heap[cur_p], self._heap[par_p] = self._heap[par_p], self._heap[cur_p]
            cur_p = par_p

    def push_freq(self, freq_x: Tuple[int, int], freq_y: Tuple[int, int], x_idx: int, y_idx: int):
        x, num_x = freq_x
        y, num_y = freq_y

        self.push(x, y, x_idx, y_idx, num_x * num_y)

    def peek(self) -> int | None:
        if self.empty():
            return None
        return self._heap[1][0]

    def empty(self) -> bool:
        return self.size <= 0

    def pop(self) -> Tuple[int, int, int, int, int, int] | None:

        if self.empty():
            return None
        self._heap[1], self._heap[self.size] = self._heap[self.size], self._heap[1]
        res = self._heap.pop()
        self.size -= 1
        cur_p = 1

        while (cur_p << 1) + 1 <= self.size:
            left_p, right_p = cur_p << 1, (cur_p << 1) + 1

            min_val = min(self._heap[left_p][0], self._heap[right_p][0], self._heap[cur_p][0])

            if min_val == self._heap[cur_p][0]:
                break
            elif min_val == self._heap[left_p][0]:
                self._heap[left_p], self._heap[cur_p] = self._heap[cur_p], self._heap[left_p]
                cur_p = left_p
            elif min_val == self._heap[right_p][0]:
                self._heap[right_p], self._heap[cur_p] = self._heap[cur_p], self._heap[right_p]
                cur_p = right_p

        if cur_p << 1 <= self.size and self._heap[cur_p][0] > self._heap[cur_p << 1][0]:
            self._heap[cur_p], self._heap[cur_p << 1] = self._heap[cur_p << 1], self._heap[cur_p]

        return res


class KSmallestSolution:
    def __init__(self, nums1: List[int], nums2: List[int], k: int):

        self.nums1: List[int] = nums1
        self.nums2: List[int] = nums2
        self.k: int = k

    def solve(self) -> List[List[int]]:
        freq1, freq2 = freq_arr(self.nums1), freq_arr(self.nums2)
        counter = 0
        pq: MinHeap = MinHeap()
        res: List[List[int]] = []
        n1, n2 = len(freq1), len(freq2)
        for i in range(n2):
            pq.push_freq(freq1[0], freq2[i], 0, i)

        while not pq.empty() and counter < self.k:

            if counter == 3:
                pass

            _, x, y, x_idx, y_idx, num_e = pq.pop()

            if x == 4 and y == 3:
                pass
            for i in range(num_e):
                res.append([x, y])
                counter += 1
                if counter == self.k:
                    break

            if x_idx < n1 - 1:
                pq.push_freq(freq1[x_idx + 1], freq2[y_idx], x_idx + 1, y_idx)

        return res


def freq_arr(arr: List[int]) -> List[tuple]:
    cur_idx = 0
    n = len(arr)
    freq: List[tuple] = []
    for i in range(1, n):
        if arr[i] != arr[cur_idx]:
            freq.append((arr[cur_idx], i - cur_idx))
            cur_idx = i

    freq.append((arr[cur_idx], n - cur_idx))
    return freq


def get_next_p(freq1: List[Tuple[int, int]], freq2: List[Tuple[int, int]], p1: int, p2: int, n1: int, n2: int) -> tuple:
    nxt_p1, nxt_p2 = p1 + 1, p2 + 1

    if nxt_p1 >= n1:
        return False, True
    elif nxt_p2 >= n2:
        return True, False
    min1, max1 = freq2[0][0] + freq1[nxt_p1][0], freq1[nxt_p1][0] + freq2[p2][0]
    min2, max2 = freq1[0][0] + freq2[nxt_p2][0], freq1[p1][0] + freq2[nxt_p1][0]

    if min1 > max2:
        return False, True
    elif min2 > max1:
        return True, False

    return True, True


nums11, nums21 = [1, 2, 4, 5, 6], [3, 5, 7, 9]
k1 = 20

sln = KSmallestSolution(nums11, nums21, k1)

print(sln.solve())
