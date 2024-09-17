class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        end = len(ratings) - 1
        res = 0
        old_val = 0
        for i in range(n - 2, -1, -1):
            if ratings[i] >= ratings[i + 1]:
                val = 1
                if i + 1 == end and ratings[i] != ratings[end]:
                    old_val += 1
                else:
                    old_val = 1
                val = old_val
                res += val
                for k in range(i + 2, end + 1):
                    if ratings[k - 1] < ratings[k]:
                        val += 1
                    res += val
                end = i
        val = 1
        if end == 0:
            val = old_val + 1
        res += val
        for i in range(1, end + 1):
            if ratings[i - 1] < ratings[i]:
                val += 1
            res += val

        return res
