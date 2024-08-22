from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda c: c[0])

        new_points = []

        cur_beg, cur_end = points[0]

        for i_beg, i_end in points[1:]:

            if cur_beg <= i_beg and i_end <= cur_end:
                cur_beg, cur_end = i_beg, i_end
                continue
            elif i_beg == cur_beg and cur_end <= i_end:
                continue

            if i_end > cur_end:
                new_points.append([cur_beg, cur_end])
                cur_beg, cur_end = i_beg, i_end

        new_points.append([cur_beg, cur_end])

        cur_beg, cur_end = new_points[0]
        num_arrow = 1
        for beg_i, end_i in new_points[1:]:

            if beg_i <= cur_end:
                continue
            num_arrow += 1
            cur_end = end_i

        return num_arrow


points1 = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]

sln = Solution()

print(sln.findMinArrowShots(points1))
