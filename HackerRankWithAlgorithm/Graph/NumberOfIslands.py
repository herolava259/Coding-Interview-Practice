from typing import List

class NoISolution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m: int = len(grid)
        n: int = len(grid[0])
        g: List[List[int]] = [[] for _ in range(m * n)]
        isLands: List[bool] = [False for _ in range(m * n)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    isLands[i * n + j] = False
                    continue
                isLands[i * n + j] = True
                if i - 1 >= 0 and grid[i - 1][j] == '1':
                    g[i * n + j].append((i-1) * n + j)
                if i + 1 < m and grid[i + 1][j] == '1':
                    g[i * n + j].append((i+1) * n + j)

                if j - 1 >= 0 and grid[i][j - 1] == '1':
                    g[i * n + j].append(i * n + j - 1)
                if j + 1 < n and grid[i][j + 1] == '1':
                    g[i * n + j].append(i * n + j + 1)

        visited = [False for _ in range(m * n)]

        numIslands = 0

        for u in range(m * n):
            if visited[u] or not isLands[u]:
                continue
            numIslands += 1
            self.dfs(u, -1, g, visited)

        return numIslands

    def dfs(self, u: int, p: int, g: List[List[int]], visited: List[int]):
        visited[u] = True
        for v in g[u]:
            if v == p or visited[v]:
                continue
            self.dfs(v, u, g, visited)


inp = [["1","1","1"],["0","1","0"],["1","1","1"]]

print(NoISolution().numIslands(inp))
