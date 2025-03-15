from typing import List, Deque as Stack
from collections import deque as stack


class MaxChunksToSortedSolution:
    def __init__(self, arr: List[int]):
        self.arr: List[int] = arr

    def solve(self) -> int:
        st: Stack[int] = stack()

        st.append(self.arr[0])

        num_chunks = len(self.arr)

        for i in range(1, len(self.arr)):
            max_val = self.arr[i]
            if st and st[-1] > self.arr[i]:
                num_chunks -= 1
                max_val = st.pop()
            while st and st[-1] > self.arr[i]:
                num_chunks -= 1
                st.pop()

            st.append(max_val)

        return num_chunks

print(MaxChunksToSortedSolution([4,3,2,1,0]).solve())

