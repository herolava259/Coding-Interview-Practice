from typing import List

'''
D. CGCDSSQ
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Given a sequence of integers a1,...,an and q queries x1,...,xq on it. For each query xi you have to count the number of pairs (l,r) 
such that 1≤ l ≤ r ≤n and gcd(al,al +1,...,ar)=xi.

 is a greatest common divisor of v1, v2, ..., vn, that is equal to a largest positive integer that divides all vi.

Input
The first line of the input contains integer n, (1 ≤ n ≤ 10^5), denoting the length of the sequence. The next
 line contains n space separated integers a1, ..., an, (1 ≤ ai ≤ 109).

The third line of the input contains integer q, (1 ≤ q ≤ 3 × 10^5), denoting the number of queries.
Then follows q lines, each contain an integer xi, (1 ≤ xi ≤ 109).

Output
For each query print the result in a separate line.
'''


def gcd(a: int, b: int) -> int:
    if a < b:
        a, b = b, a

    while b != 0:
        r = a % b
        a = b
        b = r

    return a


def lcm(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)


class SegmentTreeRMQSolution:
    def __init__(self, arr: List[int]):
        self.arr: List[int] = arr
        self.n = len(arr)
        self.st: List[int] | None = None

    def initialize(self):
        if self.st is not None:
            return
        self.st = [0 for _ in range(2 * self.n + 1)]
        self.build(1, 0, self.n - 1)

    def build(self, nid: int, first: int, last: int) -> int:
        if first == last:
            self.st[nid] = self.arr[first]
            return self.st[nid]
        mid = (first + last) // 2

        gcd_first = self.build(2 * nid, first, mid)
        gcd_last = self.build(2 * nid + 1, mid + 1, last)

        self.st[nid] = gcd(gcd_first, gcd_last)

        return self.st[nid]

    def gcd_query(self, i: int, j: int) -> int:
        return self.query(1, 0, self.n - 1, i, j)

    def query(self, nid: int, first: int, last: int, i: int, j: int) -> int:
        if first > j or last < i:
            return -1
        if i <= first <= last <= j:
            return self.st[nid]

        mid = (first + last) // 2

        gcd_first, gcd_last = self.query(2 * nid, first, mid, i, j), self.query(2 * nid + 1, mid + 1, last, i, j)

        if gcd_first == -1:
            return gcd_last
        if gcd_last == -1:
            return gcd_last

        return gcd(gcd_first, gcd_last)


class BayanSolution:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.n = len(arr)
        self.gcd_resolver = SegmentTreeRMQSolution(arr)

    def resolve_query_naive(self, x: int):
        dp = list(self.arr)
        counter = 0
        for e in self.arr:
            if e == x:
                counter += 1

        for i in range(2, self.n + 1):
            for j in range(self.n - 1, i - 2, -1):
                dp[j] = gcd(dp[j - 1], self.arr[j])
                if dp[j] == x:
                    counter += 1
        return counter

    def resolve_query_using_gcd_segment_tree(self, x: int):
        counter = 0

        for i in range(0, self.n + 1):
            for j in range(i, self.n):
                gcd_i_j = self.gcd_resolver.gcd_query(i, j)
                if gcd_i_j == x:
                    counter += 1
                elif gcd_i_j % x != 0:
                    break
        return counter
