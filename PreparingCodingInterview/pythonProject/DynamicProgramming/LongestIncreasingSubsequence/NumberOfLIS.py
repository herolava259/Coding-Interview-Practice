from typing import List


class FenwickTree:
    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums
        self.bits: List[int] = [0] * (len(nums) + 1)

    def build(self):

        n = len(self.nums)

        for i in range(1, n + 1):
            last_bit_num = i & (-i)
            for j in range(last_bit_num):
                self.bits[i] += self.nums[i - j]

    def sum_prefix(self, idx: int) -> int:
        ans = 0
        while idx > 0:
            ans += self.bits[idx]
            idx -= idx & (-idx)

        return ans

    def sum_range(self, first_idx: int, last_idx: int) -> int:
        return self.sum_prefix(last_idx) - self.sum_prefix(first_idx - 1)

    def update(self, idx: int, val: int):
        n = len(self.nums)

        while idx <= n:
            self.bits[idx] += val
            idx += idx & (-idx)


class SegmentTree:
    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums
        self.st: List[int] = [0] * (4* len(nums))

    def build(self, id: int, l: int, r: int):
        if l == r:
            self.st[id] = self.nums[l]
            return

        mid = (l + r) >> 1
        self.build(2 * id, l, mid)
        self.build(2 * id + 1, mid + 1, r)

        self.st[id] = min(self.st[2 * id], self.st[2 * id + 1])

    def update(self, id: int, l: int, r: int, i, val: int):

        if l > i or r < i:
            return

        if l == r:
            self.st[id] = val
            return

        mid = (l + r) >> 1

        self.update(2 * id, l, mid, i, val)
        self.update(2 * id + 1, mid + 1, r, i, val)

        self.st[id] = min(self.st[2 * id], self.st[2 * id + 1])

    def get(self, id: int, l: int, r: int, u: int, v: int) -> int:

        if l > v or r < u:
            return int('inf')

        if l >= u and r <= v:
            return self.st[id]

        mid: int = (l + r) >> 1

        left_val = self.get(2 * id, l, mid, u, v)
        right_val = self.get(2 * id + 1, mid + 1, r, u, v)

        return min(left_val, right_val)


class NumberOfLISSolution:
    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums

    def naive_solve(self) -> int:
        n = len(self.nums)
        dp_len: List[int] = [0] * n
        dp_amount: List[int] = [0] * n
        max_len = 1

        for idx, num in enumerate(self.nums):
            if num == 3:
                pass
            len_lis = 1
            amount = 1
            for i in range(idx - 1, -1, -1):
                if num > self.nums[i]:
                    if dp_len[i] + 1 > len_lis:
                        amount = dp_amount[i]
                        len_lis = dp_len[i] + 1
                    elif dp_len[i] + 1 == len_lis:
                        amount += dp_amount[i]
            max_len = max(max_len, len_lis)
            dp_amount[idx] = amount
            dp_len[idx] = len_lis

        return sum(dp_amount[idx] for idx in range(n) if dp_len[idx] == max_len)


nums1 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

sln = NumberOfLISSolution(nums1)

print(sln.naive_solve())
