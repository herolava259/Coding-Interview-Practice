from typing import List


class Project:
    def __init__(self, profit: int, capital: int):
        self.profit: int = profit
        self.capital: int = capital


class MaxHeap:
    def __init__(self):
        self.heap: List[Project] = [Project(-1, -1)]
        self.size = 0

    def push(self, prj: Project):

        self.heap.append(prj)
        self.size += 1

        cur_p = self.size

        while cur_p > 1:
            par_p = cur_p >> 1

            if self.heap[par_p].profit > self.heap[cur_p].profit:
                break
            if self.heap[par_p].profit == self.heap[cur_p].profit \
                    and self.heap[cur_p].capital >= self.heap[par_p].capital:
                break

            self.heap[par_p], self.heap[cur_p] = self.heap[cur_p], self.heap[par_p]
            cur_p = par_p

    def empty(self) -> bool:
        return self.size <= 0

    def peek(self) -> Project | None:
        if self.size == 0:
            return None
        return self.heap[1]

    def pop(self) -> Project | None:

        if self.size <= 0:
            return None

        self.heap[1], self.heap[self.size] = self.heap[self.size], self.heap[1]
        res = self.heap.pop()
        self.size -= 1

        cur_p = 1

        while (cur_p << 1) + 1 <= self.size:
            left_p, right_p = cur_p << 1, (cur_p << 1) + 1

            max_profit = max(self.heap[cur_p].profit, self.heap[left_p].profit, self.heap[right_p].profit)

            if max_profit == self.heap[cur_p].profit:
                break
            elif max_profit == self.heap[left_p].profit:
                self.heap[cur_p], self.heap[left_p] = self.heap[left_p], self.heap[cur_p]
                cur_p = left_p
            elif max_profit == self.heap[right_p].profit:
                self.heap[cur_p], self.heap[right_p] = self.heap[right_p], self.heap[cur_p]
                cur_p = right_p

        if cur_p << 1 <= self.size and self.heap[cur_p << 1].profit > self.heap[cur_p].profit:
            self.heap[cur_p], self.heap[cur_p << 1] = self.heap[cur_p << 1], self.heap[cur_p]

        return res


class IPOSolution:
    def __init__(self, k: int, w: int, profits: List[int], capital: List[int]):
        self.k: int = k
        self.w: int = w
        self.profits: List[int] = profits
        self.capital: List[int] = capital

    def solve(self) -> int:

        projects: List[Project] = [Project(p, c) for p, c in zip(self.profits, self.capital)]

        projects.sort(key=lambda c: c.capital, reverse=True)
        max_heap = MaxHeap()

        cur_c = self.w
        for _ in range(self.k):
            while projects and projects[-1].capital <= cur_c:
                max_heap.push(projects.pop())
            if max_heap.empty():
                return -1
            cur_c += max_heap.pop().profit

        return cur_c


k1, w1 = 2, 0
profits1 = [1, 2, 3]
capital1 = [0, 1, 2]

sln = IPOSolution(k1, w1, profits1, capital1)

print(sln.solve())
