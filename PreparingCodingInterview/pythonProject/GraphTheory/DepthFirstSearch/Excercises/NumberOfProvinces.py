from typing import List, Deque, Tuple
from collections import deque


class NumOfProvinces:
    def __init__(self, isConnected: List[List[int]]):
        self.is_connected: List[List[int]] = isConnected

    def dfs_solve(self) -> int:

        n = len(self.is_connected)
        visited: List[int] = [False] * n

        st: Deque[List[int]] = deque()
        num_province = 0
        for u in range(n):
            if visited[u]:
                continue
            num_province += 1
            visited[u] = True
            st.append([u, -1, 0])
            while st:
                u_n, p, v = st[-1]
                if v == n:
                    st.pop()
                    continue
                if u_n == v or v == p:
                    st[-1][-1] += 1
                    continue
                if visited[v] or not self.is_connected[u_n][v]:
                    st[-1][-1] += 1
                    continue

                visited[v] = True
                st.append([v, u_n, 0])

        return num_province


isConnected1 = [[1,0,0],[0,1,0],[0,0,1]]

sln = NumOfProvinces(isConnected1)

print(sln.dfs_solve())

