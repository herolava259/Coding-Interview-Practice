
def overlappedGetWays(n, c):
    # Write your code here
    c.sort()
    minCoin = c[0]
    dp = [0] *(max(n,c[-1])+1)

    dp[0] = 1



    for i in range(minCoin , n +1):
        for k, coin in enumerate(c):
            if i-coin < 0:
                break
            total = dp[i-coin]
            for j in range(k):
                if coin <= i - c[j] and dp[i-coin-c[j]] > 0:
                    total -= dp[i-c[j]-coin]
                    break
            dp[i] +=total
    return dp[n]

def getWays(n,c):

    c.sort()
    minCoin = c[0]
    p = [0]*(c[-1]+1)
    m = max(c[-1], n)
    dp = [list(p) for i in range(m+1)]
    for i in c:
        dp[i][i] = 1

    for i in range(minCoin,n+1):
        for coin in c:
            if i-coin <= 0:
                break
            if i-coin < coin:
                break
            for t in dp[i-coin][coin:]:
                dp[i][coin] += t

    sums = sum(dp[n])

    return sums



n = 3
str_inp = "8 3 1 2".split(' ')
c = [int(i) for i in str_inp]



print(getWays(n,c))


