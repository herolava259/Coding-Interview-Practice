

def naive_solve(i, prices, shares, bal):
    if i == len(prices):
        return 0 if bal < 0 else bal

    selling = naive_solve(i + 1, prices, 0, bal + prices[i] * shares)
    buying = naive_solve(i + 1, prices, shares + 1, bal - prices[i])
    donothing = naive_solve(i + 1, prices, shares, bal)

    return max(selling, buying, donothing)

inp = [2,1]
def naive_stockmax(prices):

    return naive_solve(0, prices, 0, 0)

def optimize_stockmax(prices):
    dp = []

    maxPrice = prices[-1]
    dp.append(len(prices)-1)
    for id in range(len(prices)-1,-1,-1):
        if prices[id] > maxPrice:
            dp.append(id)
            maxPrice = prices[id]


    dp = dp[::-1]
    print(dp)
    id = 0
    sell_id = dp[0]
    profit = 0
    for i, price in enumerate(prices):
        if i > sell_id:
            id += 1
            sell_id = dp[id]
        profit += (prices[sell_id] - prices[i])

    return profit

print(naive_stockmax(inp))
print(optimize_stockmax(inp))