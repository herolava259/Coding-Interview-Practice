MODK = 1000000007


def swap_permutation(n, k):
    if k == 0:
        return 1, 1

    if n <= 1:
        return 1, 2

    adj_dp = [1 for _ in range(k + 1)]
    most_dp = [2 for _ in range(k + 1)]

    cul_dp = [i for i in range(k + 2)]

    most_dp[0] = 1
    # print('n = ', 2)
    # print('dp= ', dp)
    # print('cul_dp= ', cul_dp)
    for i in range(3, n + 1):
        adj_tmp_dp = [0 for _ in range(k + 1)]
        tmp_cul_dp = [0 for _ in range(k + 2)]
        adj_tmp_dp[0] = 1
        adj_tmp_dp[1] = (1 + adj_dp[1]) % MODK

        most_tmp_dp = [0 for _ in range(k + 1)]
        most_tmp_dp[0] = 1
        most_tmp_dp[1] = (most_dp[1] + ((i - 1) * most_dp[0]) % MODK) % MODK

        tmp_cul_dp[1] = 1
        tmp_cul_dp[2] = (tmp_cul_dp[1] + adj_tmp_dp[1]) % MODK

        for j in range(2, k + 1):
            # minimum of swapping between inner array that one are considering and new element at last position of array
            # i-1 : maximum num of swap two adjanct element sequentially from left to rigth or
            # right to left of array has i element
            limit_swap_out = min(j, i - 1)
            adj_tmp_dp[j] = (cul_dp[j + 1] - cul_dp[j - limit_swap_out]) % MODK
            tmp_cul_dp[j + 1] = (adj_tmp_dp[j] + tmp_cul_dp[j]) % MODK

            most_tmp_dp[j] = (most_dp[j] + ((i - 1) * most_dp[j - 1]) % MODK) % MODK

        adj_dp = adj_tmp_dp
        cul_dp = tmp_cul_dp
        most_dp = most_tmp_dp
        # print('n= ',i)
        # print('dp= ',dp)
        # print('cul_dp= ', cul_dp)

    return adj_dp[-1], most_dp[-1]


def most_swap_permutation(n, k):
    if k == 0:
        return 1

    if n <= 1:
        return 1

    dp = [2 for i in range(k + 1)]

    dp[0] = 1

    for i in range(3, n + 1):

        tmp_dp = [0 for _ in range(k + 1)]

        tmp_dp[0] = 1
        tmp_dp[1] = (dp[1] + ((i - 1) * dp[0]) % MODK) % MODK

        for j in range(2, k + 1):
            tmp_dp[j] = (dp[j] + ((i - 1) * dp[j - 1]) % MODK) % MODK

        dp = tmp_dp

    return dp[-1]


def adjancent_swap_permutation(n, k):
    if k == 0:
        return 1

    if n <= 1:
        return 1

    adj_dp = [1 for i in range(k + 1)]

    adj_dp[0] = 1
    cul_dp = [i for i in range(k + 2)]
    # print('n = ', 2)
    # print('dp= ', dp)
    # print('cul_dp= ', cul_dp)
    for i in range(3, n + 1):
        tmp_dp = [0 for _ in range(k + 1)]
        tmp_cul_dp = [0 for _ in range(k + 2)]
        tmp_dp[0] = 1
        tmp_dp[1] = (1 + adj_dp[1]) % MODK

        tmp_cul_dp[1] = 1
        tmp_cul_dp[2] = (tmp_cul_dp[1] + tmp_dp[1]) % MODK

        for j in range(2, k + 1):
            # minimum of swapping between inner array that one are considering and new element at last position of array
            # i-1 : maximum num of swap two adjanct element sequentially from
            # left to rigth or right to left of array has i element
            limit_swap_out = min(j, i - 1)

            tmp_dp[j] = (cul_dp[j + 1] - cul_dp[j - limit_swap_out]) % MODK
            tmp_cul_dp[j + 1] = (tmp_dp[j] + tmp_cul_dp[j]) % MODK

        adj_dp = tmp_dp
        cul_dp = tmp_cul_dp

        # print('n= ',i)
        # print('dp= ',dp)
        # print('cul_dp= ', cul_dp)

    return adj_dp[-1]


# print(swapPermutation(10,8))

n, k = 1000, 94
print(swap_permutation(n, k))
