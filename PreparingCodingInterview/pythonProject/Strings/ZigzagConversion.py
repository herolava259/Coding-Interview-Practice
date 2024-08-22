from typing import List

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        cols: List[List[str]] = []
        p_mod = 0
        cur_col = []
        num_zigzag = 0
        is_append = False
        for c in s:
            if is_append:
                cols.append(cur_col)
                is_append = False
                cur_col = []
            if num_zigzag <= 0:
                cur_col.append(c)
                p_mod += 1
                if p_mod == numRows:
                    is_append = True
                    num_zigzag = numRows - 2
                    p_mod = 0
                continue

            for i in range(numRows):
                if i == num_zigzag:
                    cur_col.append(c)
                else:
                    cur_col.append('')
            is_append = True
            num_zigzag -= 1

        if len(cur_col) < numRows:
            for i in range(numRows - len(cur_col)):
                cur_col.append('')
        cols.append(cur_col)

        zigzag_s = ''

        n_col = len(cols)

        for i in range(numRows):
            for j in range(n_col):
                zigzag_s += cols[j][i]
        return zigzag_s


sln = Solution()

s1 = "PAYPALISHIRING"
numRows1 = 3

print(sln.convert(s1, numRows1))