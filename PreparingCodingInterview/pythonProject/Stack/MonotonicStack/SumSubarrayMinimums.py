from typing import List, Deque as Stack
from collections import deque as stack

modk = 10**9 + 7
def gcd_extended(a: int, b: int) -> int:

    if b >= a:
        b = b % a

    a1, a2, a3 = 1, 0, a
    b1, b2, b3 = 0, 1, b

    while b3 != 0 and b3 != 1:
        q = a3 // b3
        r1 = a1 - q * b1
        r2 = a2 - q * b2
        r3 = a3 - q * b3

        a1, a2, a3 = b1, b2, b3
        b1, b2, b3 = r1, r2, r3

    if b3 == 0:
        return a3
    return b2


def factorial_modk(num: int) -> int:
    result: int = 1

    for i in range(1, num + 1):
        result = (result * i) % modk
    return result

class SumSubarrayMinsSolution:
    def __init__(self, arr: List[int]):
        self.arr: List[int] = arr

    def solve(self) -> int:
        n = len(self.arr)


        fac_modk: List[int] = [1] * (n + 1)
        for i in range(1, n+1):
            fac_modk[i] = (fac_modk[i-1] * i) % modk
        inverse_modk = lambda x: gcd_extended(modk, x)
        def c2_normal(k: int):
            if 0 <= k <= 2:
                return 1
            return (fac_modk[k] * inverse_modk(2) * inverse_modk(fac_modk[k-2])) % modk

        def c2_include_mid(k: int, mid: int):
            if k <= 1 or mid > k:
                return 1

            exclude_left = c2_normal(mid-1) if mid > 2 else 0
            exclude_right = c2_normal(k - mid) if k-mid >= 2 else 0
            return (c2_normal(k) - exclude_left - exclude_right + 1) % modk

        st: Stack[int] = stack()

        def calc(k_idx: int, upper_idx: int) -> int:
            lower_idx = st[-1] if st else -1
            return (c2_include_mid(upper_idx-lower_idx-1, k_idx - lower_idx) * self.arr[k_idx]) % modk

        sums = 0
        st.append(0)

        for i in range(1, len(self.arr)):
            while st and self.arr[st[-1]] >= self.arr[i]:
                idx = st.pop()
                sums = (sums + calc(idx, i)) % modk
            st.append(i)

        while st:
            sums = (sums + calc(st.pop(), n)) % modk

        return sums
    def simple_solve(self) -> int:
        n = len(self.arr)

        st: Stack[int] = stack()


        sums = 0
        st.append(0)

        for i in range(1, len(self.arr)):
            while st and self.arr[st[-1]] >= self.arr[i]:
                idx = st.pop()
                lo = st[-1] if st else -1
                hi = i
                sums = (sums + ((idx - lo) * (hi - idx) * self.arr[idx]) % modk) % modk
            st.append(i)

        while st:
            idx = st.pop()
            lo = st[-1] if st else -1
            hi = n
            sums = (sums + ((idx - lo) * (hi - idx) *self.arr[lo]) % modk) % modk

        return sums


arr1 = [3,1,2,4]
print(SumSubarrayMinsSolution(arr1).simple_solve())

