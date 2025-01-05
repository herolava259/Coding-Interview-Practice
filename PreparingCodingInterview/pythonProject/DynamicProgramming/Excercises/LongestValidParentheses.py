from collections import deque
from typing import Deque, Tuple


class LongestValidParentheses:
    def __init__(self, s: str):
        self.s: str = s

    def solve(self) -> int:

        st: Deque[Tuple[int, str]] = deque()

        max_length = 0
        for idx, c in enumerate(self.s):

            if c == '(':
                st.append((0, '('))
                continue

            # case c == ')'

            new_length = 0

            while st and st[-1][1] == '':
                cur_len, _ = st.pop()
                new_length += cur_len
            max_length = max(new_length, max_length)
            if not st:
                continue
            new_length += 2

            max_length = max(new_length, max_length)
            st.pop()
            st.append((new_length, ''))

        while st:
            while st and st[-1][1] == '(':
                st.pop()
            cur_len = 0

            while st and st[-1][1] == '':
                l, _ = st.pop()
                cur_len += l
            max_length = max(max_length, cur_len)

        return max_length


s1 = '(()())(((())))()((()))(('

sln = LongestValidParentheses(s1)

print(sln.solve())
