from typing import List


class Solution:
    def isValid(self, s: str) -> bool:

        st: List[str] = []

        close_sign = [')', ']', '}']
        open_sign_map = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in close_sign:
                if not st or st[-1] != open_sign_map[c]:
                    return False
                _ = st.pop()
            else:
                st.append(c)

        if len(st) > 0:
            return False
        return True