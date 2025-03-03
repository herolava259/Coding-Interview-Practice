from typing import List, Dict, Tuple


class FourSumSolution:
    def __init__(self, nums: List[int], target: int):

        self.nums: List[int] = nums
        self.target: int = target

    def solve(self) -> List[List[int]]:

        self.nums.sort()

        results: Dict[str, List[int]] = dict()
        n = len(self.nums)

        for p_lc in range(1,n):
            for p_rc in range(p_lc+1, n):
                p_l, p_r = 0, n-1



                while p_l < p_lc and p_rc < p_r:
                    cd_sum = self.nums[p_l] + self.nums[p_lc] + self.nums[p_rc] + self.nums[p_r]
                    if cd_sum == self.target:
                        arr = [self.nums[p_l], self.nums[p_lc], self.nums[p_rc], self.nums[p_r]]
                        results[f'{arr[0]}_{arr[1]}_{arr[2]}_{arr[3]}'] = arr
                        p_l += 1
                        p_r -= 1
                        continue
                    if p_l == p_lc - 1:
                        p_r -= 1
                        continue
                    if p_r == p_rc + 1:
                        p_l += 1
                        continue

                    if cd_sum > self.target:
                        p_r -= 1
                    elif cd_sum < self.target:
                        p_l += 1

        return list(results.values())

    def opt_solve(self) -> List[List[int]]:

        pairs: List[Tuple[int, int, int]] = []
        n = len(self.nums)
        self.nums.sort()
        for i in range(n):
            for j in range(i+1, n):
                pairs.append((self.nums[i] + self.nums[j], i, j))

        pairs.sort(key=lambda c: c[0])
        p_left, p_right = 1, len(pairs)-1

        result_dict: Dict[str, List[int]] = dict()

        while p_left < p_right:

            val_l, idx_l1, idx_l2 = pairs[p_left]

            val_r, idx_r1, idx_r2 = pairs[p_right]


            cd_sum = val_l + val_r
            if cd_sum == self.target:
                indexes = [idx_l1, idx_l2, idx_r1, idx_r2]
                indexes.sort()
                cd_arr: List[int] = [self.nums[idx] for idx in indexes]
                result_dict[f'{cd_arr[0]}_{cd_arr[1]}_{cd_arr[2]}_{cd_arr[3]}'] = cd_arr
                p_left += 1
                p_right -= 1
            elif cd_sum < self.target:
                p_left += 1
            else:
                p_right -= 1

        return list(result_dict.values())

    def double_two_pointer_solve(self) -> List[List[int]]:

        self.nums.sort()
        n = len(self.nums)
        p_ll, p_cl, p_cr, p_rr = 0, 1, n-2, n-1
        result_dict: Dict[str, List[int]] = dict()
        while p_cl < p_cr:
            inner_partial_sum = self.nums[p_cl] + self.nums[p_cr]
            remain_target = self.target - inner_partial_sum

            while p_ll < p_cl and p_rr > p_cr:

                cd_sum = self.nums[p_ll] + self.nums[p_rr]

                if cd_sum == remain_target:

                    cd_arr: List[int] = [self.nums[p_ll], self.nums[p_cl], self.nums[p_cr], self.nums[p_rr]]
                    result_dict[f'{cd_arr[0]}_{cd_arr[1]}_{cd_arr[2]}_{cd_arr[3]}'] = cd_arr
                    p_ll += 1
                    p_rr -= 1
                elif cd_sum < remain_target:
                    p_ll += 1
                else:
                    p_rr -= 1

            bounding_sum = self.nums[p_ll] + self.nums[p_cl] + self.nums[p_cr] + self.nums[p_rr]

            if bounding_sum < self.target:
                p_cl += 1
            elif bounding_sum == self.target:
                p_cl += 1
                p_cr -= 1
            else:
                p_cr -= 1

        return list(result_dict.values())


class KSumSolution:
    def __init__(self, nums: List[int], target:int, k: int):

        self.nums = nums
        self.target = target
        self.k = k

    def solve(self) -> List[List[int]]:
        n = len(self.nums)
        self.nums.sort()

        def two_sum(start: int, target: int) -> List[List[int]]:

            p_left, p_right = start, n-1

            results = []

            while p_left < p_right:

                val = self.nums[p_left] + self.nums[p_right]

                if val == target:
                    results.append([self.nums[p_left], self.nums[p_right]])
                    p_left +=1
                    p_right -= 1
                elif val > target:
                    p_right -= 1
                else:
                    p_left += 1
            return results

        def k_sum_recur(start: int, k: int, target)-> List[List[int]]:

            if start+k > n or k * self.nums[start] > target or k * self.nums[-1] < target:
                return []

            if k == 2:
                return two_sum(start, target)
            results: List[List[int]] = []

            for st in range(start, n-k-1):

                for sub_sln in k_sum_recur(st+1, k-1, target - self.nums[st]):
                    results.append([self.nums[st]] + sub_sln)

            return results

        return k_sum_recur(0, self.k, self.target)








