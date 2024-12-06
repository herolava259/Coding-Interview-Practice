from typing import List, Dict

class MaxNonDecreasingLengthSolution:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1: List[int] = nums1
        self.nums2: List[int] = nums2

    def solve(self) -> int:

        assert len(self.nums1) == len(self.nums2)

        n = len(self.nums1)
        dp_dict: Dict[str, List[List[int]]] = {'max': [[1,-1] for _ in range(n)] , 'min': [[1, -1] for _ in range(n)]}

        max_dp = 1

        dp_dict['max'][0][1], dp_dict['min'][0][1] = max(self.nums1[0], self.nums2[0]), min(self.nums1[0], self.nums2[0])

        for i in range(1, n):
            cur_max = max(self.nums1[i], self.nums2[i])

            cur_min = self.nums1[i] + self.nums2[i] - cur_max

            prev_len_min, prev_min = dp_dict['min'][i-1]
            prev_len_max, prev_max = dp_dict['max'][i-1]

            if cur_max < prev_min:
                dp_dict['min'][i][1] = cur_min
                dp_dict['max'][i][1] = cur_max
                continue

            if cur_max >= prev_max:
                dp_dict['max'][i][0], dp_dict['max'][i][1] = prev_len_max+1, cur_max
            else:
                dp_dict['max'][i][0], dp_dict['max'][i][1] = prev_len_min+1, cur_max

            if cur_min >= prev_max:
                dp_dict['min'][i][0], dp_dict['min'][i][1] = prev_len_max+1, cur_min
            elif cur_min >= prev_min:
                dp_dict['min'][i][0], dp_dict['min'][i][1] = prev_len_min+1, cur_min
            else:
                dp_dict['min'][i][0], dp_dict['min'][i][1] = 1, cur_min

            max_dp = max(max_dp, dp_dict['max'][i][0])

        return max_dp

nums11 = [1,3,2,1]
nums21 = [2,2,3,4]

sln = MaxNonDecreasingLengthSolution(nums11, nums21)

print(sln.solve())

