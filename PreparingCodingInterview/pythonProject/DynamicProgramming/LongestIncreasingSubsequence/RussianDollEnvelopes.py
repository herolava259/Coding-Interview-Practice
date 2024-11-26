from typing import List, Tuple

class InvertedIndexSegmentTree:
    def __init__(self, max_size: int):
        self.max_size: int = max_size
        self.st: List[int] = [0] * (4 * max_size + 1)

    def easy_update(self, k_idx: int, val: int):
        self.update(1, 0, self.max_size-1, k_idx, val)

    def update(self, idx: int, l: int, r: int, k_idx: int, val: int):

        if l > k_idx or r < k_idx:
            return

        if l == r:
            self.st[idx] = max(self.st[idx], val)
            return

        mid = (l + r) >> 1

        self.update(idx << 1, l, mid, k_idx, val)
        self.update((idx << 1) + 1, mid + 1, r, k_idx, val)

        self.st[idx] = max(self.st[idx << 1], self.st[(idx << 1) + 1])

    def initialize(self, nums: List[int]):

        def build(idx: int, l: int, r: int):
            if l == r:
                self.st[idx] = nums[l]
                return
            mid = (l+r) >> 1

            build(idx << 1, l, mid)
            build((idx << 1) + 1, mid + 1, r)

            self.st[idx] = max(self.st[idx << 1], self.st[(idx << 1) + 1])

        build(1, 0, self.max_size-1)

    def easier_get(self, supreme: int):
        return self.get(1, 0, self.max_size-1, 0, supreme-1)

    def get(self, idx: int, l: int, r: int, u: int, v: int) -> int:

        if l > v or r < u:
            return -1

        if u <= l <= r <= v:
            return self.st[idx]

        mid = (l + r) >> 1

        left_val = self.get(idx << 1, l, mid, u, v)
        right_val = self.get((idx << 1) + 1, mid+1, r, u, v)

        return max(left_val, right_val)



class MaxEnvelopesSolution:
    def __init__(self, envelopes: List[List[int]]):
        self.envelopes: List[List[int]] = envelopes

    def get_max_size(self) -> int:
        return max(map(lambda c: c[1], self.envelopes))

    def solve(self) -> int:

        sorted_envelopes: List[List[int]] = sorted(self.envelopes, key=lambda c: c[0])
        n = len(sorted_envelopes)

        max_size = self.get_max_size()
        segment_tree: InvertedIndexSegmentTree = InvertedIndexSegmentTree(max_size)


        dp: List[int] = [1] * n

        max_dp = 1

        prev_val , search_idx = sorted_envelopes[0]

        cache: List[Tuple[int, int]] = [(search_idx, 1)]
        for i in range(1, n):

            cur_val, search_idx = sorted_envelopes[i]

            if cur_val > prev_val:
                for idx, val in cache:
                    segment_tree.easy_update(idx, val)
                cache.clear()
                prev_val = cur_val

            dp[i] = segment_tree.easier_get(search_idx) + 1

            cache.append((search_idx, dp[i]))
            max_dp = max(dp[i], max_dp)

        return max_dp


class SegmentTree:
    def __init__(self, n: int):

        self.st: List[Tuple[int, int] | None] = [None] * (4 * n + 1)

    def initialize(self, pairs: List[List[int]], n: int):

        def build(idx: int, l: int, r: int):
            if l == r:
                self.st[idx] = (l, pairs[l][1])
                return

            mid = (l+r) >> 1

            build(2 * idx, l, mid)
            build(2 * idx + 1, mid+1, r)

            if self.st[2 * idx][1] > self.st[2 * idx + 1][1]:
                self.st[idx] = self.st[2 * idx]
            else:
                self.st[idx] = self.st[2 * idx + 1]

        build(1, 0, n-1)

    def get(self, idx: int, l: int, r: int, u: int, v: int, val: int) -> Tuple[int, int]:

        if l > v or r < u:
            return -1, -1

        if u <= l <= r <= v:
            if val <= self.st[idx][1]:
                return self.find_lower_bound(idx, l, r, val)
            return self.st[idx]

        mid = (l + r) >> 1

        left_id, left_val = self.get(2 * idx, l, mid, u, v, val)
        right_id, right_val = self.get(2 * idx + 1, mid+1, r, u, v, val)


        if right_val >= left_val:
            return right_id, right_val
        return left_id, left_val

    def find_lower_bound(self, idx: int, l: int, r: int, val: int) -> Tuple[int, int]:

        if l == r:
            if self.st[idx][1] >= val:
                return -1, -1
            return self.st[idx]

        mid = (l + r) >> 1

        left_idx, left_val = self.find_lower_bound(2 * idx, l, mid, val)
        right_idx, right_val = self.find_lower_bound(2 * idx + 1, mid+1, r, val)

        if right_val >= left_val:
            return right_idx, right_val
        return left_idx, left_val

envelopes_r = [[15,8],[2,20],[2,14],[4,17],[8,19],[8,9],[5,7],[11,19],[8,11],[13,11],[2,13],[11,19],[8,11],[13,11],[2,13],[11,19],[16,1],[18,13],[14,17],[18,19]]

sln = MaxEnvelopesSolution(envelopes_r)

print(sln.solve())
