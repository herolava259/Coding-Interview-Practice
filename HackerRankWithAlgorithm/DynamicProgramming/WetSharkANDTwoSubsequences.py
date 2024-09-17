
def twoConsecutivesequences(x ,r ,s):
    MODK = 10 ** 9 + 7
    n = len(x)
    sums = [[0 for _ in range(n + 1)] for i in range(n)]

    for i in range(n):
        for j in range(i, n):
            sums[i][j - i + 1] = (sums[i][j - i] + x[j])
    print(sums)
    num_seq = 0
    for i in range(1 , n +1):
        for j in range(n + 1 - i):
            for k in range(j, n + 1 - i):
                a = sums[j][i] + sums[k][i]
                st = sums[j][i] - sums[k][i]
                if a == r and st == s:
                    num_seq += 1
                if a == r and st == -s:
                    num_seq += 1

    return num_seq

def twoSubsequences(x ,r ,s):

    MODK = 10**9 + 7
    if r <= s or (r + s) % 2 == 1:
        return 0
    a = (r + s) // 2
    b = a - s
    n = len(x)

    dp = [[0 for j in range(n + 1)] for i in range(2001)]

    if x[0] <= a:
        dp[x[0]][1] = 1
    for i in range(1, n):
        for j in range(2000, 0, -1):
            if j - x[i] >= 0:
                for k in range(1, n + 1):
                    dp[j][k] = (dp[j - x[i]][k - 1] + dp[j][k]) % MODK
        dp[x[i]][1] += 1
    sums = 0
    for i in range(1, n + 1):
        sums = (sums + (dp[a][i] * dp[b][i]) % MODK) % MODK

    return sums


x = [1, 1, 1, 4]
r = 5
s = 3

print(twoSubsequences(x, r, s))
