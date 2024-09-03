from typing import List


class DecodeStringSolution:

    def __init__(self, s: str):
        self.s: str = s

    def solve(self) -> str:

        st: List[str] = []
        for c in self.s:
            if c == '[':
                st.append(c)
            elif c.isalpha():
                if st and st[-1].isalpha():
                    st[-1] += c
                else:
                    st.append(c)
            elif c.isdigit():
                if st and st[-1].isdigit():
                    st[-1] += c
                else:
                    st.append(c)
            elif c == ']':
                new_str = st.pop()
                st.pop()
                num_str = st.pop()
                aggr_str = new_str * int(num_str)
                if st and st[-1].isalpha():
                    st[-1] += aggr_str
                else:
                    st.append(aggr_str)

        return st[-1]


s1 = "2[abc]3[cd]ef"

sln = DecodeStringSolution(s1)

print(sln.solve())
