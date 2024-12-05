from collections import defaultdict
from typing import List, DefaultDict, Dict


class NonDecreasingSubseqSolution:
    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums

    def solve(self) -> List[List[int]]:

        results: List[List[int]] = []
        n: int = len(self.nums)
        inverted_indexes: DefaultDict[int, List[int]] = defaultdict(list)
        for i in range(n):
            inverted_indexes[self.nums[i]].append(i)
        keys = sorted(inverted_indexes.keys())
        n_unique = len(keys)
        def backtrack(seq: List[int], k: int, last_idx):

            if k >= n_unique:
                return
            val = keys[k]

            indexes = inverted_indexes[val]
            cum_num = 0
            for l, idx in enumerate(indexes):
                if idx < last_idx:
                    continue
                cum_num += 1
                cd_seq = seq + [val] * cum_num

                if len(cd_seq) > 1:
                    results.append(cd_seq)

                for b in range(k+1, n_unique):
                    backtrack(cd_seq, b, idx)

        for m in range(n_unique):

            backtrack([], m, -1)

        return results

    def dfs_solve(self) -> List[List[int]]:

        n = len(self.nums)

        def generate_graph() -> List[List[int]]:
            graph: List[List[int]] = [[] for _ in range(n)]
            for i in range(n):
                for j in range(i + 1, n):
                    if self.nums[j] >= self.nums[i]:
                        graph[i].append(j)
            return graph

        g: List[List[int]] = generate_graph()

        results: List[List[int]] = []
        visited: DefaultDict[int, bool] = defaultdict(lambda: False)

        def dfs(path: List[int], u: int):
            internal_visited: DefaultDict[int, bool] = defaultdict(lambda: False)
            for v in g[u]:
                if internal_visited[self.nums[v]]:
                    continue
                internal_visited[self.nums[v]] = True
                new_path = path + [self.nums[v]]
                results.append(new_path)
                dfs(new_path, v)

        for i in range(n):
            if visited[self.nums[i]]:
                continue
            visited[self.nums[i]] = True

            dfs([self.nums[i]], i)

        return results

nums1 = [100,90,80,70,60,50,60,70,80,90,100]

sln = NonDecreasingSubseqSolution(nums1)

print(sln.solve())