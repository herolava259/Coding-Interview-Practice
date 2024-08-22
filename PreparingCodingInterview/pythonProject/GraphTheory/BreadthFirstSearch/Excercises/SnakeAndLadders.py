from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)
        n2 = n ** 2

        visited = [False for _ in range(0, n2 + 1)]

        q: List[tuple] = []

        cur_s, num_move = 1, 0
        q.append((cur_s, num_move))
        visited[1] = True

        while q:
            cur_s, num_move = q.pop(0)

            if cur_s == n2:
                return num_move

            for nxt_s in range(cur_s + 1, min(cur_s + 6, n2 + 1)):
                nxt_i = (nxt_s - 1) // n
                nxt_j = (nxt_s - 1) % n

                if nxt_i % 2 == 1:
                    nxt_j = n - 1 - nxt_j
                nxt_i = n - 1 - nxt_i
                real_s = nxt_s
                while board[nxt_i][nxt_j] != -1:
                    real_s = board[nxt_i][nxt_j]
                    if real_s == 15:
                        pass
                    nxt_i = (real_s - 1) // n
                    nxt_j = (real_s - 1) % n
                    if nxt_i % 2 == 1:
                        nxt_j = n - 1 - nxt_j
                    nxt_i = n - 1 - nxt_i

                if visited[real_s]:
                    continue

                visited[real_s] = True

                q.append((real_s, num_move + 1))

        return -1


sln = Solution()
board1 = [[-1,-1],[-1,3]]

print(sln.snakesAndLadders(board1))