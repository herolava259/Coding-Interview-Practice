from typing import List, Tuple


class SegmentTree:
    def __init__(self, n_size: int):

        self.n_size : int = n_size

        self.st: List[int] = [0] * (4 * n_size + 1)

    def update(self, k_idx: int, val: int):

        def st_update(idx: int, l: int, r: int)->int:
            if k_idx < l or k_idx > r:
                return self.st[idx]

            if l == r:
                self.st[idx] = max(val, self.st[idx])
                return val

            mid = (l + r) >> 1

            left_val = st_update(idx << 1, l, mid)
            right_val = st_update((idx << 1) + 1, mid + 1, r)

            self.st[idx] = max(left_val, right_val)

            return self.st[idx]

        st_update(1, 0, self.n_size - 1)

    def get(self, u: int, v: int) -> int:


        def st_get(idx: int, l: int, r: int)-> int:

            if l > v or r < u:
                return -1

            if u <= l <= r <= v:
                return self.st[idx]

            mid = (l + r) >> 1

            return max(st_get(idx << 1, l, mid), st_get((idx << 1)+1, mid+1, r))

        return st_get(1, 0, self.n_size-1)


class LongestValidObstacleSolution:
    def __init__(self, obstacles: List[int]):
        self.obstacles: List[int] = obstacles

    def naive_solve(self) -> List[int]:

        n = len(self.obstacles)

        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if self.obstacles[j] <= self.obstacles[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return dp

    def lu_solve(self) -> List[int]:

        n = len(self.obstacles)

        result: List[int] = [1] * n
        lowers: List[int] = [-1] * n
        uppers: List[int] = [-1] * n

        for i in range(1,n):

            l_idx, h_idx = i-1, i-1

            while l_idx != -1 and self.obstacles[l_idx] > self.obstacles[i]:
                l_idx = lowers[l_idx]

            while h_idx != -1 and self.obstacles[h_idx] <= self.obstacles[i]:
                h_idx = uppers[h_idx]



            lowers[i], uppers[i] = l_idx, h_idx

            idx = l_idx

            lower_bound = self.obstacles[l_idx]
            cur_val = self.obstacles[i]

            while idx > -1 and self.obstacles[idx] >= lower_bound:
                result[i] = max(result[i], result[idx] + 1)

                lower_bound = self.obstacles[idx]

                idx = uppers[idx]

                while idx > -1 and not (lower_bound <= self.obstacles[idx] <= cur_val):
                    if self.obstacles[idx] < lower_bound:
                        idx = uppers[idx]
                    elif self.obstacles[idx] > cur_val:
                        idx = lowers[idx]

        return result

    def st_solve(self) -> List[int]:

        st: SegmentTree = SegmentTree(max(self.obstacles) + 1)

        n = len(self.obstacles)
        result: List[int] = [1] * n

        st.update(self.obstacles[0], 1)

        for i in range(1, n):
            result[i] = st.get(0, self.obstacles[i]) + 1
            st.update(self.obstacles[i], result[i])
        return result

    def bs_solve(self) -> List[int]:

        order_dp: List[int] = []
        def binary_search(key: int) -> int:
            low, high = 0, len(order_dp)-1

            if key > order_dp[-1]:
                return high + 1
            if key < order_dp[0]:
                return -1

            while low < high:
                mid = ((low + high) >> 1) + 1
                mid_key = order_dp[mid]

                if mid_key > key:
                    high = mid - 1
                else:
                    low = mid

            return low
        n = len(self.obstacles)
        result: List[int] = [1] * n

        order_dp.append(self.obstacles[0])

        for i in range(1, n):

            k = self.obstacles[i]
            search_idx = binary_search(k)
            if i == 8:
                pass

            if search_idx == -1:
                result[i] = 1
                order_dp[0] = k
            elif search_idx >= len(order_dp)-1:
                order_dp.append(k)
                result[i] = len(order_dp)
            else:
                result[i] = search_idx + 2
                order_dp[search_idx+1] = min(k, order_dp[search_idx+1])
        return result





obstacles1 = [5,3,4,4,4,2,1,1,4,1]
sln = LongestValidObstacleSolution(obstacles1)

print(sln.bs_solve())