from typing import List
import math

'''
Alexandra has a paper strip with n numbers on it. Let's call them ai from left to right.

Now Alexandra wants to split it into some pieces (possibly 1). For each piece of strip, it must satisfy:

Each piece should contain at least l numbers.
The difference between the maximal and the minimal number on the piece should be at most s.
Please help Alexandra to find the minimal number of pieces meeting the condition above.

Input
The first line contains three space-separated integers n,s,l (1≤n≤10^5,0≤ s ≤ 10^9, 1 ≤ l ≤ 10^5).

The second line contains n integers ai separated by spaces (-10^9 ≤ ai ≤ 10^9).

Output
Output the minimal number of strip pieces.

If there are no ways to split the strip, output -1.

'''
'''
Input1:
7 2 2
1 3 1 2 4 1 2

Output1:
3

Input2:
7 2 2
1 100 1 100 1 100 1

Output2:
-1
'''

'''Solution: dp[k+1] = max({dp[k-i] with condition: l <= i <= k - 1 and max(arr[k+1-i:k+1]) - min(arr[k+1-i:k+1]) <= 
s and dp[k-i] != -1}) + 1 

s1: building data structure for querying min and max in elements has idx from i to j:
+ Using sparse table
+ Using segment tree

s2: building a data structure for querying in arr[i:j] has max(arr[i:j]) - min(arr[i:j] <= s has name  
diff[0:N][0:N]
diff[j][i] =  max(arr[i:j]) - min(arr[i:j])

building way:
for j -> 0...n-1
for i -> n-1...0
diff[j][i] = max(diff[j][i+1], arr[i]) - min(diff[j][i+1], arr[i])
'''


class SparseTableRMQSolution:
    def __init__(self, arr: List[int], ):
        self.arr: List[int] = arr
        self.n: int = len(arr)
        self.dp_min: List[List[int]] | None = None
        self.dp_max: List[List[int]] | None = None

    def build(self):
        log_n = math.ceil(math.log(self.n, 2))
        self.dp_min = [[0 for _ in range(log_n)] for _ in range(self.n)]
        self.dp_max = [[0 for _ in range(log_n)] for _ in range(self.n)]

        for i in range(self.n):
            self.dp_min[i][0] = i
            self.dp_max[i][0] = i

        for j in range(1, log_n):
            for i in range(self.n):
                self.dp_min[i][j] = self.dp_min[i][j - 1]
                self.dp_max[i][j] = self.dp_max[i][j - 1]
                if i + (1 << j) - 1 >= self.n:
                    continue

                self.dp_min[i][j] = self.dp_min[i][j - 1]
                self.dp_max[i][j] = self.dp_max[i][j - 1]
                if i + (1 << (j - 1)) <= self.n and \
                        self.arr[self.dp_min[i][j]] \
                        > self.arr[self.dp_min[i + (1 << (j - 1)) - 1][j - 1]]:
                    self.dp_min[i][j] = self.dp_min[i + (1 << (j - 1) - 1)][j - 1]

                if i + (1 << (j - 1)) <= self.n and \
                        self.arr[self.dp_max[i][j]] \
                        > self.arr[self.dp_max[i + (1 << (j - 1)) - 1][j - 1]]:
                    self.dp_max[i][j] = self.dp_max[i + (1 << (j - 1)) - 1][j - 1]

    def query_max(self, i: int, j: int) -> tuple:

        log_range = int(math.log((j - i + 1)))
        id_max = self.dp_max[i][log_range]
        val_max = self.arr[id_max]
        if val_max > self.arr[self.dp_max[j - 1 << log_range + 1][log_range]]:
            id_max = self.dp_max[self.dp_max[j - 1 << log_range + 1][log_range]]
            val_max = self.arr[id_max]

        return id_max, val_max

    def query_min(self, i: int, j: int) -> tuple:

        log_range = int(math.log((j - i + 1)))
        id_min = self.dp_min[i][log_range]
        val_min = self.arr[id_min]
        if val_min > self.arr[self.dp_min[j - 1 << log_range + 1][log_range]]:
            id_min = self.dp_min[self.dp_min[j - 1 << log_range + 1][log_range]]
            val_min = self.arr[id_min]

        return id_min, val_min

    def query_diff(self, i: int, j: int) -> int:

        _, val_min = self.query_min(i, j)
        _, val_max = self.query_max(i, j)

        return val_max - val_min


class StripSolution:
    def __init__(self, arr: List[int], l: int, s: int):
        self.arr = arr
        self.least_num = l
        self.most_diff = s
        self.rmq_diff = SparseTableRMQSolution(arr)
        self.dp: List[int] | None = None
        self.n: int = len(arr)

    def solve(self):
        self.rmq_diff.build()
        n = len(self.arr)
        dp: List[int] = [n+1 for _ in range(n+1)]
        dp[0] = 0
        self.dp = dp
        for i in range(1, self.least_num):
            dp[i] = -1

        if self.rmq_diff.query_diff(0, self.least_num - 1) > self.most_diff:
            return -1

        for i in range(self.least_num + 1, self.n+1):
            max_beg = i - self.least_num + 1
            tmp_dp = n+1
            for beg in range(max_beg, -1, -1):
                if dp[beg] == n+1 or self.rmq_diff.query_diff(beg, i) > self.most_diff:
                    continue
                if tmp_dp > dp[beg] + 1:
                    tmp_dp = dp[beg] + 1
            dp[i] = tmp_dp

        return dp[n] if dp[n] < n+1 else -1

    def binary_search(self, first: int, last: int):

        mid = (first + last) // 2
        if first >= last:
            return last
        res = self.binary_search(mid+1, last)
        if self.dp[mid + 1] != self.n+1:
            return res
        res_low = self.binary_search(first, mid)
        if self.dp[res] == self.n+1:
            return res_low
        return res



