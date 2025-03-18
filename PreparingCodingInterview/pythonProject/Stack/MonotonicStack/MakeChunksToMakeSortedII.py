from typing import List, Deque as Stack, Tuple
from collections import deque as stack

class MaxChunksToSortedSolution:
    def __init__(self, arr: List[int]):

        self.arr: List[int] = arr

    def solve(self) -> int:

        max_chunk = len(self.arr)

        st: Stack[Tuple[int, int]] = stack()

        for idx, num in enumerate(self.arr):
            max_s = num

            if st and st[-1][0] == num:
                st.append((num, st.pop()[1] + 1))
                continue
            elif st and st[-1][0] > num:
                max_s, mult = st.pop()
                max_chunk -= mult

            while st and st[-1][0] > num:
                max_chunk -= st.pop()[1]

            st.append((max_s, 1))

        return max_chunk

print(MaxChunksToSortedSolution([5,4,3,2,1]).solve())
