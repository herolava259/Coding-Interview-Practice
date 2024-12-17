from typing import List

class FindingKthPositiveSolution:
    def __init__(self, arr: List[int], k: int):
        self.arr: List[int] = arr
        self.k: int = k

    def solve(self) -> int:


        low, high = 0, len(self.arr)-1

        while low < high:
            mid = ((low + high) >> 1) + ((low + high) & 1)

            cur_val = self.arr[mid]

            num_missing = cur_val - mid - 1

            if num_missing > self.k:
                high = mid - 1
            else:
                low = mid

        num_missing = self.arr[low] - low - 1


        if low == 0 and self.arr[low] > self.k:
            return self.k

        if num_missing < self.k:
            return self.arr[low] + self.k - num_missing
        while low > 0 and self.arr[low] == self.arr[low-1]+1:
            low -= 1

        return self.arr[low] - 1

arr1 = [6,7,10,20,28,29,33,37,39,40,49,53,55,72,75,76,85,87,88,94,106,107,119,120,129,142,147,152,157,159,161,173,178,183,187,188,193,199,202,212,215,224,227,230,237,239,246,251,256,260,266,268,273,277,279,281,291,297,298,310,312,314,315,321,324,326,329,341,342,348,355,367,370,374,387,389,394,413,420,424,429,446,447,458,460,464,467,473,477,478,498,500,501,503,514,515,523,525,528,529,531,535,539,555,566,569,572,583,588,591,596,602,604,605,606,610,611,616,619,622,623,631,632,640,642,645,647,661,680,684,685,687,694,696,698,714,717,720,726,734,738,742,745,753,770,775,780,781,783,787,788,798,806,821,835,852,865,873,888,897,926,932,935,939,945,956,966,967,969,973,979,980,986,992,995,997]
k1 = 96

sln = FindingKthPositiveSolution(arr1, k1)

print(sln.solve())
