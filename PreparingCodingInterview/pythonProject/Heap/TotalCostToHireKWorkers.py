from typing import List, Tuple


class MinHeap:
    def __init__(self):
        self._heap: List[Tuple[int, int]] = [(-1, -1)]
        self.size: int = 0

    def push(self, c: int, idx: int):
        self._heap.append((c, idx))
        self.size += 1

        cur_p = self.size

        while cur_p > 1:
            par_p = cur_p >> 1

            if self._heap[par_p][0] <= self._heap[cur_p][0]:
                break
            self._swap(par_p, cur_p)
            cur_p = par_p

    def pop(self) -> Tuple[int, int] | None:

        if self.size <= 0:
            return None
        min_elem = self._heap[1]

        self._swap(1, self.size)
        self._heap.pop()
        self.size -= 1

        cur_p = 1

        while (cur_p << 1) + 1 <= self.size:

            left_p, right_p = cur_p << 1, (cur_p << 1) + 1

            min_val = min(self._heap[left_p][0], self._heap[right_p][0], self._heap[cur_p][0])

            if self._heap[cur_p][0] == min_val:
                break
            elif self._heap[left_p][0] == min_val:
                self._swap(left_p, cur_p)
                cur_p = left_p
            elif self._heap[right_p][0] == min_val:
                self._swap(right_p, cur_p)
                cur_p = right_p

        if (cur_p << 1) <= self.size and self._heap[cur_p] > self._heap[cur_p << 1]:
            self._swap(cur_p, cur_p << 1)

        return min_elem

    def _swap(self, idx1: int, idx2: int):
        self._heap[idx1], self._heap[idx2] = self._heap[idx2], self._heap[idx1]


class TotalCostSolution:

    def __init__(self, costs: List[int], k: int, candidates: int):
        self.costs: List[int] = costs
        self.k: int = k
        self.candidates: int = candidates

    def solve(self) -> int:

        min_heap: MinHeap = MinHeap()
        total_cost = 0

        first_p, last_p = 0, len(self.costs) - 1
        num_first, num_last = 0, 0
        for i in range(self.k):
            while num_first < self.candidates and first_p <= last_p:
                min_heap.push(self.costs[first_p], first_p)
                first_p += 1
                num_first += 1
            while num_last < self.candidates and first_p <= last_p:
                min_heap.push(self.costs[last_p], last_p)
                last_p -= 1
                num_last += 1

            min_cost, cur_idx = min_heap.pop()

            total_cost += min_cost

            if cur_idx < first_p:
                num_first -= 1
            elif cur_idx > last_p:
                num_last -= 1

        return total_cost


costs1 = [17,12,10,2,7,2,11,20,8]
k1 = 3
candidates1 = 4

sln = TotalCostSolution(costs1, k1, candidates1)

print(sln.solve())
