from typing import List, Deque as Stack, DefaultDict as Table
from collections import deque as stack, Counter, defaultdict

class RemoveDuplicateLettersSolution:
    def __init__(self, s: str):
        self.s: str = s

    def greedy_solve(self) -> str:

        map_tb: Table[str, List[int]] = defaultdict(list)

        for idx, c in enumerate(self.s):
            map_tb[c].append(idx)

        result = ''
        threshold_idx = -1
        choose_idx: List[int] = []
        for i in range(26):

            c = chr(i + ord('a'))

            if not map_tb[c]:
                continue
            c_idx: int = map_tb[c][0]

            for idx in map_tb[c]:
                c_idx = idx
                if idx > threshold_idx:
                    break
            choose_idx.append(c_idx)
            threshold_idx = max(c_idx, threshold_idx)

        result= ''

        for idx in sorted(choose_idx):
            result += self.s[idx]
        return result




    def solve(self) -> str:

        nums: List[int] = [ord(c) - ord('a') for c in self.s]

        freq: List[int] = [0] * 26
        for c, fr in Counter(nums).items():
            freq[c] = fr
        st: Stack[int] = stack()

        result = ''
        mark: List[bool] = [False] * 26

        for idx, c in enumerate(nums):
            if mark[c]:
                continue
            while st and nums[st[-1]] >= c:
                ix = st.pop()
                freq[nums[ix]] -= 1
            st.append(idx)

            if freq[nums[idx]] > 1:
                continue

            while st:
                ix = st.popleft()
                result += self.s[ix]
                mark[nums[ix]] = True

        return result


s1 = "cbacdcbc"

print(RemoveDuplicateLettersSolution(s1).greedy_solve())
