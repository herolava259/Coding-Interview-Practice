from typing import List, Deque as Stack
from collections import deque as stack, Counter


class RemoveDuplicateLettersSolution:
    def __init__(self, s: str):
        self.s: str = s

    def solve(self) -> str:

        nums: List[int] = [ord(c) - ord('a') for c in self.s]

        freq: List[int] = [0] * 26
        for c, fr in Counter(nums).items():
            freq[c] = fr
        st: Stack[int] = stack()

        result = ''
        mark: List[bool] = [False] * 26
        for idx, c in enumerate(nums):
            freq[c] -= 1
            if mark[c]:
                continue
            while st and nums[st[-1]] > c and freq[nums[st[-1]]] > 0:
                ix = st.pop()
                mark[nums[ix]] = False
            st.append(idx)
            mark[c] = True

        for idx in st:
            result += self.s[idx]

        return result


s1 = "cbacdcbc"

print(RemoveDuplicateLettersSolution(s1).solve())
