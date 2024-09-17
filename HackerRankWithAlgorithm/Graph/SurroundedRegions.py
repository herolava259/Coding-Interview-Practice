from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])

        visited: List[List[bool]] = [[False for _ in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 3 and j == 1:
                    pass
                if 0 < i < m - 1 and 0 < j < n - 1:
                    continue

                if not visited[i][j] and board[i][j] == "O":
                    self.dfs(i, j, m, n, visited, board)

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    board[i][j] = "X"
        return

    def dfs(self, i_row: int, j_col: int, m: int, n: int, visited: List[List[bool]], board: List[List[str]]):

        visited[i_row][j_col] = True

        if i_row + 1 < m and not visited[i_row + 1][j_col] and board[i_row + 1][j_col] == 'O':
            self.dfs(i_row + 1, j_col, m, n, visited, board)
        if i_row - 1 >= 0 and not visited[i_row - 1][j_col] and board[i_row - 1][j_col] == 'O':
            self.dfs(i_row - 1, j_col, m, n, visited, board)
        if j_col + 1 < n and not visited[i_row][j_col + 1] and board[i_row][j_col + 1] == 'O':
            self.dfs(i_row, j_col + 1, m, n, visited, board)
        if j_col - 1 >= 0 and not visited[i_row][j_col - 1] and board[i_row][j_col - 1] == 'O':
            self.dfs(i_row, j_col - 1, m, n, visited, board)


board_inp = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(Solution().solve(board_inp))