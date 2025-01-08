from typing import List, Set,DefaultDict
from collections import defaultdict
import sys

maxk: int = 10**9 + 7

class QTree5Solution:
    def __init__(self, g: List[List[int]], n: int):

        self.g: List[List[int]] = g
        self.n: int = n

        self.multiset: List[DefaultDict[int, List[int]]] = [defaultdict(list) for _ in range(n+1)]

        self.colors: List[bool] = [True] * (n+1)

        self.deleted: List[bool] = [False] * (n+1)
        self.par: List[int] = [-1] * (n+1)
        self.child: List[int] = [1] * (n+1)
        self.dist: List[DefaultDict[int, int]] = [defaultdict(int) for _ in range(n+1)]

    def count_child(self, uid: int, pid: int) -> int:
        self.child[uid] = 1

        for vid in self.g[uid]:
            if vid == pid or self.deleted[vid]:
                continue
            self.child[uid] += self.count_child(vid, uid)

        return self.child[uid]

    def find_centroid(self, uid: int, pid: int, n_force:int):

        half_n = n_force >> 1

        for vid in self.g[uid]:
            if vid == pid or self.deleted[vid]:
                continue
            if self.child[vid] > half_n:
                return self.find_centroid(vid, uid, n_force)

        return uid

    def calc_dist(self, uid: int, pid: int, rid: int):

        for vid in self.g[uid]:
            if vid == pid or self.deleted[vid]:
                continue
            self.dist[vid][rid] = self.dist[uid][rid] + 1
            self.calc_dist(vid, uid, rid)

    def construct_centroid_tree(self, uid: int = 1) -> int:

        n_force: int = self.count_child(uid, 0)

        centroid_id = self.find_centroid(uid,0, n_force)

        self.calc_dist(centroid_id, 0, centroid_id)

        self.deleted[centroid_id] = True

        for vid in self.g[centroid_id]:
            if self.deleted[vid]:
                continue

            child_centroid_id = self.construct_centroid_tree(vid)

            self.par[child_centroid_id] = centroid_id

        return centroid_id

    def initialize(self):
        self.construct_centroid_tree()
        for u in range(1, self.n+1):
            self.change_color(u)


    def find_min_white_dist_to(self, uid: int) -> int:

        def min_dist_of(xid: int) -> int:

            inverse_map: DefaultDict[int, List[int]] = self.multiset[xid]

            sorted_cd_dist = sorted(inverse_map.keys())

            for dist in sorted_cd_dist:
                if inverse_map[dist]:
                    return dist
            return maxk

        ans = maxk
        pid = uid

        while pid:
            if self.multiset[pid]:
                ans = min(ans, self.dist[uid][pid] + min_dist_of(pid))
            pid = self.par[pid]
        if ans >= maxk:
            return -1
        return ans

    def change_color(self, uid: int):

        self.colors[uid] = not self.colors[uid]

        if self.colors[uid]:
            pid = uid
            while pid:
                self.multiset[pid][self.dist[uid][pid]].remove(uid)
                pid = self.par[pid]
        else:
            pid = uid

            while pid:
                self.multiset[pid][self.dist[uid][pid]].append(uid)
                pid = self.par[pid]

    def query(self, cmd: int, uid: int) -> int | None:

        if cmd == 0:
            return self.change_color(uid)

        return self.find_min_white_dist_to(uid)

n: int | None = None
g: List[List[int]] | None = None
def initialize():
    global n
    n = int(input("n: "))
    m = int(input('m: '))
    g: List[List[int]] = [[] for _ in range(n+12)]

    for _ in range(m):
        u, v = [int(item) for item in input("edge: ").split()]
        g[u].append(v)
        g[v].append(u)

def interact():

    num_testcase = int(input('num of test: '))

    for i in range(num_testcase):
        cmd, uid = [int(item) for item in input('query: ').strip().split()]
        result: int | None = sln.query(cmd, uid)

        print(f'Test case:\n cmd: {cmd}. \n uid: {uid}')
        print(f'Result: {result}') if result else None

initialize()
sln = QTree5Solution(g, n)
sln.initialize()
interact()