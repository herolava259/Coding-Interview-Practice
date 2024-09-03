from typing import List


class RemoveStarsSolution:
    def __init__(self, s: str):
        self.s = s

    def solve(self) -> str:

        st: List[str] = []

        for c in self.s:
            if c != '*':
                st.append(c)
                continue

            if st:
                st.pop()

        return ''.join(st)

s1 = 'erase*****'

sln = RemoveStarsSolution(s1)

print(sln.solve())

