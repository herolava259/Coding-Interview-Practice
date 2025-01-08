import math
from typing import List, DefaultDict, Tuple
from collections import defaultdict

modk = 10**9 + 7
base = 3157

class LampiceSolution:
    def __init__(self, g: List[List[int]], a: List[str]):


        self.g: List[List[int]] = g
        self.a: List[str] = a
        self.n: int = len(self.g)

        self.child: List[int] = [0] * (self.n+1)
        self.valid: List[bool] = [True] * (self.n+1)
        self.pw: List[int] = [0] * (self.n+1)
        self.f: List[DefaultDict[int, bool]] = [defaultdict(bool) for _ in range(self.n+1)]
        self.b: List[Tuple[int, int]] = []

        self.max_depth = 0

        self.len: int = math.ceil(math.log2(self.n))

    def count_child(self, u:int, p: int) -> int:
        self.child[u] = 1

        for v in self.g[u]:
            if v!= p and self.valid[u]:
                self.child[u] += self.count_child(v, u)

        return self.child[u]


    def dfs_check_max_len(self, uid: int, pid: int, h: int, hshdown: int, hshup: int) -> bool:
        if h > self.len:
            return False

        if pid != 0:
            hshdown = (hshdown * base + ord(self.a[uid])) % modk
        hshup = (hshup + ord(self.a[uid]) * self.pw[h-1]) % modk

        x = (hshup * self.pw[self.len-h] - hshdown + modk) % modk

        if not pid:
            self.f[h][x] = True
        if self.f[self.len - h +1][x]:
            return True

        for vid in self.g[uid]:
            if vid == pid or not self.valid[vid]:
                continue

            if pid == 0:
                self.b.clear()

            if self.dfs_check_max_len(vid, uid, h + 1, hshdown, hshup):
                return True

            if not pid:
                for height, hsh in self.b:
                    self.f[height][hsh] = True

        self.max_depth = max(self.max_depth, h)

        self.b.append((h, x))

    def check_palindrome(self, uid: int, n_len: int) -> bool:

        self.count_child(uid, 0)

        flag: bool = True
        half_n = n_len // 2

        # find centroid
        while flag:
            flag = False

            for vid in self.g[uid]:
                if self.valid[vid] and half_n < self.child[vid] < self.child[uid]:
                    uid = vid
                    flag = True
                    break

        self.count_child(uid, 0)

        if self.dfs_check_max_len(uid, 0, 1, 0, 0):
            return True

        for i in range(1, self.max_depth+1):
            self.f[i].clear()

        self.max_depth = 0
        self.valid[uid] = False

        for vid in self.g[uid]:
            if self.valid[vid] and self.check_palindrome(vid, self.child[vid]):
                return True

        return False

    def check_valid_len(self, len_l: int):

        # reset temp variables
        self.len = len_l
        for i in range(1, self.n+1):
            self.valid[i] = True
            self.f[i].clear()

        return self.check_palindrome(1, self.n)


    def solve(self) -> int:

        self.pw[0] = 1

        for i in range(1, self.n+1):
            self.pw[i] = self.pw[i-1] * base % modk

        low, high = 0, (self.n-1) >> 1

        while low < high:

            mid = (low+high+1) >> 1

            if self.check_valid_len((mid << 1) + 1):
                low = mid
            else:
                high = mid - 1

        ans = (high << 1) + 1

        low, high = 0, self.n >> 1

        while low < high:

            mid = (low + high + 1) >> 1

            if self.check_valid_len(mid << 1):
                low = mid
            else:
                high = mid + 1

        return max(ans, high << 1)
