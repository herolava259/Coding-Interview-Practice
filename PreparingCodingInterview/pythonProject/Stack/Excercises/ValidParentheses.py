from typing import Deque
from collections import deque


def isValid(s: str) -> bool:
    st: Deque[str] = deque()

    for c in s:
        if c in '[{(':
            st.append(c)
        elif c == ']':
            if not st or s[-1] != '[':
                return False

            st.pop()
        elif c == '}':
            if not s or s[-1] != '{':
                return False

            st.pop()
        elif c == ')':
            if not st or s[-1] != '(':
                return False

            st.pop()

    if st:
        return False

    return True


s1 = '(}'

print(isValid(s1))
