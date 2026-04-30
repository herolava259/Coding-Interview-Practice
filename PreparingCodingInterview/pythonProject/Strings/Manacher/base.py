from typing import List


class PalindromeEnumerationWithManacherSolution:
    def __init__(self, max_n: int, s: str):
        self.max_n = max_n
        self.s = s
        self.d_even = [0] * max_n
        self.d_odd = [0] * max_n
        self.n = len(s)

    def _calc_d_odd(self):
        l, r = 1, 0

        for i in range(1, self.n+1):
            if i > r: self.d_odd[i] = 0
            else:
                self.d_odd[i] = min(r-i, self.d_odd[l+r-i])

            while i - self.d_odd[i] -1 > 0 \
                    and i + self.d_odd[i] + 1 <= self.n \
                    and self.s[i-self.d_odd[i] - 1] == self.s[i+self.d_odd[i] + 1]:
                self.d_odd[i] += 1

            if i + self.d_odd[i] > r:
                r, l = i + self.d_odd[i], i - self.d_odd[i]

    def _calc_d_even(self):

        l, r = 1, 0

        for i in range(1, self.n):
            j = i + 1

            if j > r:
                self.d_even[i] = 0
            else:
                self.d_even[i] = min(r-j+1, self.d_even[l+r-j])

            while i - self.d_even[i] > 0 and \
                j + self.d_even[i] <= self.n and \
                self.s[i-self.d_even[i]] == self.s[j+self.d_even[i]]:
                self.d_even[i] += 1

            if i + self.d_even[i] > r:
                r, l = i + self.d_even[i], j - self.d_even[i]

    def solve(self) -> List[int]:

        self._calc_d_odd()
        self._calc_d_even()

        result = []
        for d_o, d_e in zip(self.d_odd[1:self.n], self.d_even[1:self.n]):
            result.extend([d_o*2 + 1, d_e * 2])

        result.append(self.d_odd[self.n] * 2 + 1)
        return result