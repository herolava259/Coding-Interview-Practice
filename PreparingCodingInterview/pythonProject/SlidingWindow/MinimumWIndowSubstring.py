from typing import DefaultDict
from collections import defaultdict, Counter


class MinimumWindowSubstringSolution:
    def __init__(self, s: str, t: str):
        self.s: str = s
        self.t: str = t

    def solve(self) -> str:

        freq_char = Counter(self.t)
        map_freq: DefaultDict[str, int] = defaultdict(int)
        len_t = len(self.t)
        len_s = len(self.s)

        num_force = 0

        f, cur_p = 0, 0

        min_ss = ''
        len_ss = 1000000000

        while f < len_s:
            cur_c = self.s[f]
            if freq_char.get(cur_c, 0) == 0:
                f += 1
                continue
            if cur_p < f:
                cur_p = f

            while cur_p < len_s and num_force < len_t:
                cur_p_c = self.s[cur_p]

                if freq_char.get(cur_p_c, 0) == 0:
                    cur_p += 1
                    continue

                map_freq[cur_p_c] += 1

                if map_freq[cur_p_c] <= freq_char[cur_p_c]:
                    num_force += 1

                cur_p += 1

            if num_force < len_t:
                break

            cur_ss = self.s[f: cur_p]

            len_cur_ss = len(cur_ss)

            if len_cur_ss < len_ss:
                len_ss = len_cur_ss
                min_ss = cur_ss

            map_freq[self.s[f]] -= 1

            if map_freq[self.s[f]] < freq_char[self.s[f]]:
                num_force -= 1
            f += 1
        return min_ss


s1 = "ADOBECODEBANC"
t1 = "ABC"

sln = MinimumWindowSubstringSolution(s1, t1)

print(sln.solve())
