from typing import List
import heapq


class CandySolution:
    def __init__(self, ratings: List[int]):

        self.ratings: List[int] = ratings

    def solve(self) -> int:

        min_heap = [(e, idx) for idx, e in enumerate(self.ratings)]

        take_candy = [0 for _ in self.ratings]
        heapq.heapify(min_heap)

        min_candy = 0
        n = len(self.ratings)

        while min_heap:
            val, idx = heapq.heappop(min_heap)
            candy_child = 1
            if idx > 0 and self.ratings[idx - 1] < val:
                candy_child = max(candy_child, take_candy[idx - 1] + 1)

            if idx < n - 1 and self.ratings[idx + 1] < val:
                candy_child = max(candy_child, take_candy[idx + 1] + 1)
            take_candy[idx] = candy_child
            min_candy += candy_child

        return min_candy


ratings1 = [1,2,2]

sln = CandySolution(ratings1)

print(sln.solve())
