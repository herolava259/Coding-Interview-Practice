from typing import List, Deque
from collections import deque as queue


class CanReachSolution:
    def __init__(self, arr: List[int], start: int):
        self.arr: List[int] = arr
        self.start: int = start

    def solve(self) -> bool:

        can_reach = [False] * len(self.arr)

        q: Deque[int] = queue()

        q.append(self.start)
        can_reach[self.start] = False

        n = len(self.arr)

        while q:
            position = q.popleft()
            if self.arr[position] == 0:
                return True
            prev_pos = position - self.arr[position]
            nxt_pos = position + self.arr[position]

            if prev_pos >= 0 and not can_reach[prev_pos]:
                if self.arr[prev_pos] == 0:
                    return True
                can_reach[prev_pos] = True
                q.append(prev_pos)

            if nxt_pos < n and not can_reach[nxt_pos]:
                can_reach[nxt_pos] = True
                q.append(nxt_pos)

        return False


arr1 = [3,0,2,1,2]
start1 = 2

sln = CanReachSolution(arr1, start1)

print(sln.solve())
