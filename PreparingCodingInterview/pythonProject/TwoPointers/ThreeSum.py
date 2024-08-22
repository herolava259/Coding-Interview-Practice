from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        res: List[List[int]] = []
        for i in range(n - 2):
            k = -nums[i]
            first = i + 1
            last = n - 1

            while first < last:

                if nums[first] + nums[last] < k:
                    first += 1
                elif nums[first] + nums[last] == k:
                    tmp_last = last
                    while first < tmp_last and nums[first] + nums[tmp_last] == k:
                        res.append([nums[i], nums[first], nums[tmp_last]])
                        tmp_last -= 1
                    tmp_first = first
                    while tmp_first < last and nums[tmp_first] + nums[last] == k:
                        res.append([nums[i], nums[first], nums[tmp_last]])
                        tmp_first += 1

                    first += 1
                    last -= 1
                else:
                    last -= 1

        return res

sln = Solution()

nums1 = [-1,0,1,2,-1,-4]

print(sln.threeSum(nums1))
