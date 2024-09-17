

MAX_ELEM = 5
def candlesCounting(k, candles):
    dp = [0 for _ in range(MAX_ELEM+1)]

    for (h, k_item) in candles:
        for less in range(h+1):
            dp[h] += dp[less]
        dp[h] += 1

    return dp

# tinh vi tri thap nhat cua 1 mau ma lon hon 1 so
# tinh vi tri thap nhat ma co chieu cao lon hon h

k = 3
candles = [(4,3), (1,1), (3,2), (2,2), (4,3)]

def sort_follow_color(k, candles):
    color_boxes = [[] for _ in range(k+1)]

    for idx, item in enumerate(candles):
        color_boxes[item[1]].append((idx,item[0]))

    return color_boxes

def deep_copy(arr):

    return [list(item) for item in arr]

def sol1_candlesCounting(k, candles):
    MAX_VALUE = 50000
    MAX_K = 7
    mod_k = 100000007
    pow_2_k = 2**k
    template_dp = [[0 for i in range(pow_2_k)] for _ in range(MAX_VALUE + 1)]

    dp = deep_copy(template_dp)

    for hc in candles:
        #tmp_dp = deep_copy(dp)
        for i in range(1,hc[0]):
            for j in range(pow_2_k):
                access_color = hc[1] | j
                dp[hc[0]][access_color] = (dp[hc[0]][access_color] + dp[i][j]) % mod_k

        dp[hc[0]][2 ** hc[1]] = (dp[hc[0]][2 ** hc[1]] + 1) % mod_k
        #dp = tmp_dp

    sums = 0

    for i in range(MAX_VALUE + 1):
        if dp[i][-1] > 0:
            sums = (sums + dp[i][-1] - 1) % mod_k

    return sums

def count_increase_arr(arr):
    dp = [0 for i in range(50001)]
    for item in arr:
        for i in range(item):
            dp[item] += dp[i]
        dp[item] += 1

    sums = 0
    prev_value = -1
    for item in arr[::-1]:
        if prev_value <= item:
            sums += dp[item]
            prev_value = item

    return sums

def sol2_count_increase_arr(arr):
    n = len(arr)
    greater_or_equal_elems = [i for i in range(n)]
    less_elems = [i for i in range(n)]

    for i in range(1, n):
        if arr[i] > arr[i-1]:
            less_elems[i] = i-1
            idx = greater_or_equal_elems[i-1]
            while idx != greater_or_equal_elems[idx] and arr[idx] < arr[i]:
                idx = greater_or_equal_elems[idx]

            if arr[idx] >= arr[i]:
                greater_or_equal_elems[i] = idx
        else:
            greater_or_equal_elems[i] = i-1
            idx = less_elems[i-1]

            while idx != less_elems[idx] and arr[idx] >= arr[i]:
                idx = less_elems[idx]

            if arr[idx] < arr[i]:
                less_elems[i] = idx
    dp = [0 for _ in range(n)]
    dp[0] = 1
    for i in range(1,n):
        idx = less_elems[i]

        while arr[idx] < arr[i]:
            dp[i] += dp[idx]
            prev_ge = greater_or_equal_elems[idx]
            if prev_ge == idx:
                dp[i] += dp[idx] - 1
                break
            for j in range(prev_ge+1, idx):
                dp[i] += dp[j]
            idx = prev_ge
        dp[i] += 1

    return dp[-1] - 1

# tinh day tang don cua tung mau
# vi tri thap nhat cua day
# vi tri cao nhat cua day
# (1,1); (3,2); (2,2); (4,3)
def sol2_candlesCounting(k, candles):
    min_dp = [[]]
    prev_item = (-1, 50001)
    n = len(candles)
    colored_candle_buckets = sort_follow_color(k, candles)

    for c in range(1, k+1):
        current_dp = []
        for item in colored_candle_buckets[c]:
            if prev_item[1] >= item[1]:
                current_dp.append(item)
                prev_item = item

        min_dp.append(current_dp)
def discussion_candlesCounting(k, candles):
    full_mask = 2 ** k
    bit = [[0]*(full_mask) for _ in range(50001)]
    #explantation:
    ans = 0
    for i in range(len(candles)):
        h, c = candles[i]
        hh = h-1
        res = [0] * (full_mask)

        #explantation:

        while hh > 0:
            res = [res[j] + bit[hh][j] for j in range(full_mask)]
            hh -= (hh & (-hh))

        new_res = [0] * (full_mask)
        new_res[(1 << (c-1))] = 1
        for j in range(full_mask):
            new_res[j | (1 << (c-1))] += (res[j]%1000000007)
        while h < 50001:
            bit[h] = [bit[h][j]+new_res[j] for j in range(full_mask)]

            h += (h & (-h))

    return ans % (1000000007)

# vi tri gan nhat ma nho hon
print(candlesCounting(k, candles))

print(sort_follow_color(k, candles))
