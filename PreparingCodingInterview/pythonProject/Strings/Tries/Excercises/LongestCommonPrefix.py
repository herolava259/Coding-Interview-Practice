from typing import List


class PrefixNode:
    def __init__(self):
        self.child: List[PrefixNode | None] = [None for _ in range(26)]
        self.cnt: int = 0
        self.exist: int = 0


class PrefixTrie:
    def __init__(self):

        self.root: PrefixNode = PrefixNode()

        self.cur: int = 0

    def new_node(self):
        self.cur += 1
        return PrefixNode()

    def add_chain(self, s: str):

        cur_node = self.root

        for c in s:

            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                nxt_node = cur_node.child[offset] = self.new_node()

            nxt_node.cnt += 1

            cur_node = nxt_node

        cur_node.exist += 1

    def find_chain(self, s: str) -> bool:

        cur_node = self.root

        for c in s:
            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]
            if nxt_node is None:
                return False
            cur_node = nxt_node

        return cur_node.exist > 0

    def delete_chain(self, s: str) -> bool:

        if not self.find_chain(s):
            return False

        cur_node = self.root

        for c in s:
            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                return True

            nxt_node.cnt -= 1

            if nxt_node.cnt <= 0:
                cur_node.child[offset] = None
            cur_node = nxt_node

        cur_node.exist -= 1
        return True


class LCPSolution(PrefixTrie):

    def __init__(self, chains: List[str], k: int):
        super(LCPSolution, self).__init__()

        self.chains: List[str] = chains
        self.k: int = k

    def build(self):

        for s in self.chains:
            self.add_chain(s)

    def solve(self) -> int:
        return self.dfs_solve(self.root, 0)[self.k]
    
    def dfs_solve(self, node: PrefixNode, depth: int = 0) -> List[int]:
        dp = [0 for _ in range(self.k + 1)]

        if node is None:
            return dp

        dp_prime: List[List[int]] = []
        for i in range(26):
            tmp_dp = self.dfs_solve(node.child[i], depth + 1)

            dp_prime.append(tmp_dp)

        limit_size = min(self.k, node.cnt)
        for i in range(1, limit_size):

            dp[i] = self.calc_value(dp_prime, 0, node, i, depth+1)

        return dp

    def calc_value(self, mtx: List[List[int]], st: int, par_node: PrefixNode, total_k: int, d: int) -> int:

        if total_k < 0:
            return 0
        cur_node = par_node.child[st]
        if st == 25:
            return mtx[st][total_k]
        if cur_node is None:
            return self.calc_value(mtx, st+1, par_node, total_k, d)

        max_dp = 0

        for num in range(1, total_k):
            cur_val = mtx[st][num]
            tmp_dp = self.calc_value(mtx, st + 1, par_node, total_k - num, d)

            if cur_val + d * num * (total_k - num) + tmp_dp > max_dp:
                max_dp = cur_val + d * num * (total_k - num) + tmp_dp

        return max_dp
