from typing import List
from collections import defaultdict
from queue import Queue


class InversionSortSolution:
    def __init__(self, seq_src: str, seq_dst: str):

        self.seq_src: str = seq_src
        self.seq_dst: str = seq_dst

    def bfs_solve(self) -> List[str] | None:

        visited: defaultdict = defaultdict(bool)
        path: List[str] = []
        prev: defaultdict = defaultdict(str)

        q: Queue = Queue()
        q.put(self.seq_src)
        visited[self.seq_src] = True
        curr_seq = self.seq_src
        while not q.empty():
            curr_seq = q.get()

            if curr_seq == self.seq_dst:
                break

            for len_s in range(2, 11):

                for st in range(0, 11 - len_s):
                    sub_seq = curr_seq[st:st + len_s]
                    new_seq = curr_seq[0: st] + sub_seq[::-1] + curr_seq[st + len_s:]

                    if visited[new_seq]:
                        continue
                    visited[new_seq] = True
                    prev[new_seq] = curr_seq
                    q.put(new_seq)

        if curr_seq != self.seq_dst:
            return None

        while curr_seq != self.seq_dst:
            path.insert(0, curr_seq)
            curr_seq = prev[curr_seq]
        path.insert(0, self.seq_src)

        return path
