from collections import defaultdict


def naive_indian_job(g, arr):

    if max(arr) > g:
        return 'NO'

    sums = sum(arr)

    half_sum = sums // 2 + sums % 2
    if half_sum > g:
        return 'NO'

    # sum of elements of arr, such that this sum is maximum but less or equal than g
    # so that: this sum of elements should be greater or equal than upper bound half the sum of arr but less or equal than g

    limit_g = min(10000, g) + 1
    dp = [0]*limit_g
    for item in arr:
        tmp_dp = dp.copy()
        for i in range(limit_g):
            if i + item < limit_g and dp[i] == 1:
                tmp_dp[i+item] = 1
        dp = tmp_dp
        dp[item] = 1
    print(half_sum)
    for i in range(half_sum, limit_g):
        if dp[i] == 1:
            print(i)
            return 'YES'

    return 'NO'


def naive2_indian_job(g,arr):

    if max(arr) > g:
        return 'NO'

    sums = sum(arr)

    half_sum = sums // 2 + sums % 2
    if half_sum > g:
        return 'NO'

    # sum of elements of arr, such that this sum is maximum but less or equal than g
    # so that: this sum of elements should be greater or equal than upper bound half the sum of arr but less or equal than g

    limit_g = min(10000, g) +1

    dp = defaultdict(int)
    for item in arr:

        keys = list(dp.keys())

        for key in keys:
            if key + item < limit_g:
                dp[key+item] = 1

        dp[item] = 1

    print(half_sum)

    for key in dp.keys():
        if key >= half_sum:
            return 'YES'

    return 'NO'

inp_g = 140
inp_arr = list(map(int, '97 51 92 22'.split(' ')))

print(naive_indian_job(inp_g, inp_arr))
print(naive2_indian_job(inp_g, inp_arr))



