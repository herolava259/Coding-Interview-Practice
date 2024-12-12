from typing import List

class FindRightIntervalSolution:
    def __init__(self, intervals: List[List[int]]):
        self.intervals: List[List[int]] = intervals

    def solve(self) -> List[int]:

        index_pairs = [(c[0], i) for i, c in enumerate(self.intervals)]

        sorted_starts = sorted(index_pairs, key=lambda c: (c[0], c[1]))
        results = [-1] * len(self.intervals)
        for idx, cnt in enumerate(self.intervals):
            _, end = cnt
            low, high = 0, len(sorted_starts)-1

            while low < high:
                mid = (low + high) // 2

                val = sorted_starts[mid][0]

                if val < end:
                    low = mid+1
                else:
                    high = mid

            if sorted_starts[low][0] >= end:
                results[idx] = sorted_starts[low][1]

        return results

intervals1 = [[1,2]]
sln = FindRightIntervalSolution(intervals1)

print(sln.solve())

