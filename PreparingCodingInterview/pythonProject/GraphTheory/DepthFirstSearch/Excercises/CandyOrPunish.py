from typing import List, Deque
from collections import deque as stack


class CandyOrPunishSolution:

    def __init__(self, nexts: List[int], n: int):

        self.nexts: List[int] = nexts
        self.n: int = n

    def solve(self) -> List[int]:

        st: Deque = stack()
        visited: List[int] = [False for _ in range(self.n+1)]
        num_candy: List[int] = [0 for _ in range(self.n+1)]
        for u in range(1, self.n+1):
            if visited[u]:
                continue
            st.clear()

            cur_node = u
            while not visited[cur_node]:
                st.append(cur_node)
                visited[cur_node] = True
                nxt_node = self.nexts[cur_node]

                if visited[nxt_node]:
                    num_candy[cur_node] = num_candy[nxt_node]
                cur_node = nxt_node

            num_scc = num_candy[cur_node]
            prev_node = st.pop()

            while prev_node != cur_node:
                num_scc += 1
                prev_node = st.pop()

            num_scc += 1
            nxt_node = cur_node
            while self.nexts[nxt_node] != cur_node:
                num_candy[nxt_node] = num_scc
                nxt_node = num_candy[nxt_node]

            while st:
                cur_node = st.pop()
                num_scc += 1
                num_candy[cur_node] = num_scc

        return num_candy

