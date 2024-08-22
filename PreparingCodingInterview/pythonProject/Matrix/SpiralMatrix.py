from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.spiral_build(matrix, len(matrix), len(matrix[0]), 0, 0, 'lt')

    def spiral_build(self, board: List[List[int]], m_row: int, n_col: int, beg_i, beg_j, corner_st: str = 'lt') \
            -> List[int]:

        if m_row == beg_i or n_col == beg_j:
            return []

        nxt_corner_st = 'lt'

        res = []
        if corner_st == 'lt':
            res = board[beg_i][beg_j: n_col]
            beg_i += 1
            nxt_corner_st = 'rt'
        elif corner_st == 'rt':
            res = [board[i][n_col - 1] for i in range(beg_i, m_row)]
            nxt_corner_st = 'rb'
            n_col -= 1
        elif corner_st == 'rb':
            res = board[m_row - 1][beg_j:n_col][::-1]
            nxt_corner_st = 'lb'
            m_row -= 1
        elif corner_st == 'lb':
            res = [board[i][beg_j] for i in range(m_row - 1, beg_i - 1, -1)]
            nxt_corner_st = 'lt'
            beg_j += 1

        res += self.spiral_build(board, m_row, n_col, beg_i, beg_j, nxt_corner_st)
        return res


matrix_inp = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sln = Solution()

print(sln.spiralOrder(matrix_inp))
