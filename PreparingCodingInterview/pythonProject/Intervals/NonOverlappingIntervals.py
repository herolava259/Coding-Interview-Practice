from typing import List


class EraseOverlappingIntervalsSolution:

    def __init__(self, intervals: List[List[int]]):

        self.intervals: List[List[int]] = intervals

    def solve(self) -> int:

        sorted_intervals = sorted(self.intervals, key=lambda c: c[0])
        num_erase = 0
        prev_end_i = sorted_intervals[0][1]
        for start_i, end_i in sorted_intervals[1:]:
            if start_i < prev_end_i:
                num_erase += 1
                prev_end_i = min(prev_end_i, end_i)
            else:
                prev_end_i = end_i
        return num_erase


intervals1 = [[0,2],[1,3],[2,4],[3,5],[4,6]]

sln = EraseOverlappingIntervalsSolution(intervals1)

print(sln.solve())
