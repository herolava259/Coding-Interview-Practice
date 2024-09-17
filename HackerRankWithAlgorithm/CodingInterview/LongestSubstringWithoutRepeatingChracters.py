from collections import defaultdict
import math

math.pow

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dp = []
        table = defaultdict(list)
        res = 1
        dp.append(1)
        n = len(s)
        table[s[0]].append(0)
        for i in range(1, n):

            idx_arr = table[s[i]]
            last_dp = dp[-1]

            curr_dp = last_dp + 1
            if len(idx_arr) > 0 and curr_dp > i - idx_arr[-1]:
                curr_dp = i - idx_arr[-1]

            dp.append(curr_dp)
            res = max(curr_dp, res)
            table[s[i]].append(i)

        return res


inp = 'bbbbb'

print(Solution().lengthOfLongestSubstring(inp))

