from typing import List, Deque, DefaultDict
from collections import deque, defaultdict


class SortItemsSolution:
    def __init__(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]):
        self.n: int = n
        self.m: int = m
        self.group: List[int] = group
        self.before_items: List[List[int]] = beforeItems

    def solve(self) -> List[int]:
        buckets: List[List[int]] = [[] for _ in range(self.m)]
        in_groups: List[int] = [0] * self.m
        out_g: List[List[int]] = [[] for _ in range(self.n)]

        q: Deque[int] = deque()
        for i in range(self.n):
            if self.group[i] == -1:
                self.group[i] = len(buckets)
                buckets.append([i])
                in_groups.append(len(self.before_items[i]))
                for in_u in self.before_items[i]:
                    out_g[in_u].append(i)
            else:
                buckets[self.group[i]].append(i)
                group_of_i = self.group[i]
                for bf_i in self.before_items[i]:
                    if self.group[bf_i] != group_of_i:
                        in_groups[group_of_i] += 1
                    out_g[bf_i].append(i)

        for i in range(len(buckets)):
            if in_groups[i] == 0:
                q.append(i)
            buckets[i] = self.sort_in_bucket(buckets[i])

        orders: List[int] = []
        counter: int = 0
        while q:

            gr_idx = q.popleft()

            for item in buckets[gr_idx]:
                orders.append(item)
                counter += 1
                for in_v in out_g[item]:
                    gr_in_idx = self.group[in_v]
                    in_groups[gr_in_idx] -= 1
                    if in_groups[gr_in_idx] == 0:
                        q.append(gr_in_idx)

        if counter == self.n:
            return orders

        return []

    def sort_in_bucket(self, bucket: List[int]) -> List[int]:

        if len(bucket) <= 1:
            return bucket
        indeg: DefaultDict[int, int] = defaultdict(int)
        q: Deque[int] = deque()
        after_items: DefaultDict[int, List[int]] = defaultdict(list)

        for item in bucket:
            for bf_item in self.before_items[item]:
                if self.group[item] == self.group[bf_item]:
                    after_items[bf_item].append(item)
                    indeg[item] += 1
            if indeg[item] == 0:
                q.append(item)

        sorted_bucket: List[int] = []

        while q:
            cur_item = q.popleft()
            sorted_bucket.append(cur_item)
            for after_item in after_items[cur_item]:
                indeg[after_item] -= 1
                if indeg[after_item] == 0:
                    q.append(after_item)
        return sorted_bucket


n1 = 8
m1 = 2
group1 = [-1, -1, 1, 0, 0, 1, 0, -1]
beforeItems1 = [[], [6], [5], [6], [3, 6], [], [], []]

sln = SortItemsSolution(n1, m1, group1, beforeItems1)

print(sln.solve())
