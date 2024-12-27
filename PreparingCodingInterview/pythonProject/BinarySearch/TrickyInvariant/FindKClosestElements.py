from typing import List


class FindClosestElementsSolution:
    def __init__(self, arr: List[int], k: int, x: int):

        self.arr: List[int] = arr

        self.k: int = k

        self.x: int = x

    def sort_solve(self) -> List[int]:

        relative_sorted_arr: List[int] = sorted(map(lambda c: (abs(c - self.x), c), self.arr),
                                                key=lambda c: (c[0], c[1]))

        return list(sorted(map(lambda c: c[1], relative_sorted_arr[: self.k])))

    def two_pointer_solve(self) -> List[int]:

        n = len(self.arr)

        left, right = 0, n - 1
        counter = n
        while counter > self.k and left < right:
            abs_left = self.norm_one_x(left)
            abs_right = self.norm_one_x(right)

            if abs_left <= abs_right:
                right -= 1
            else:
                left += 1
            counter -= 1

        return self.arr[left: right + 1]

    def norm_one_x(self, idx: int) -> int:

        return abs(self.x - self.arr[idx])

    def find_closest_elem(self, n: int) -> int:
        low, high = 0, n - 1

        while low < high-1:
            mid = (low + high) >> 1

            abs_low = self.norm_one_x(low)
            abs_high = self.norm_one_x(high)

            if abs_low <= abs_high:
                if self.arr[mid] >= self.x:
                    high = mid
                else:
                    low = mid
            else:
                # mid += (low + high) & 1
                if self.arr[mid] < self.x:
                    low = mid
                else:
                    high = mid

        if self.norm_one_x(low) <= self.norm_one_x(high):
            return low
        return high

    def bs_solve(self) -> List[int]:

        n = len(self.arr)

        if self.k >= n:
            return self.arr

        pivot = self.find_closest_elem(n)

        left, right = pivot, pivot

        result: List[int] = [self.arr[pivot]]

        while right - left + 1 < self.k:

            if right == n - 1:
                left -= 1
                result.insert(0, self.arr[left])
                continue

            if left == 0:
                right += 1
                result.append(self.arr[right])
                continue
            # case: left > 0 and right < n-1
            cd_left, cd_right = left - 1, right + 1

            if self.norm_one_x(cd_left) <= self.norm_one_x(cd_right):
                result.insert(0, self.arr[cd_left])
                left = cd_left
            else:
                result.append(self.arr[cd_right])
                right = cd_right

        return result

    def sliding_frame_solve(self) -> List[int]:

        n = len(self.arr)

        min_win_idx = 0
        min_eval_window = sum(map(self.norm_one_x, range(self.k)))

        prev_eval_window = min_eval_window

        # max(sup_window) = n
        # max(x_beg_window) + k - 1 =  max(x_end_window) = n-1
        # => max(x_beg_window) = n - k
        # sup(last_window) = n - k + 1

        for win_idx in range(1, n - self.k + 1):
            cur_eval_window: int = prev_eval_window + self.norm_one_x(win_idx + self.k - 1) - self.norm_one_x(
                win_idx - 1)

            if cur_eval_window < min_eval_window:
                min_eval_window = cur_eval_window
                min_win_idx = win_idx

            prev_eval_window = cur_eval_window

        return self.arr[min_win_idx: min_win_idx + self.k]


arr1: List[int] = [0,0,1,2,3,3,4,7,7,8]
k1: int = 3
x1: int = 5

sln = FindClosestElementsSolution(arr1, k1, x1)

print('sliding window solve: ', sln.sliding_frame_solve())
print('sort solve: ', sln.sort_solve())
print('two pointer solve: ', sln.two_pointer_solve())
print('binary search solve: ', sln.bs_solve())
