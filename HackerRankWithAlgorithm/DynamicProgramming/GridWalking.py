

MODK = 1000000000+7

def copy_arr(arr):
    new_arr = []
    for item in arr:
        new_arr.append(item.copy())
    return new_arr


def sparseArrWalking(x,d,m):

    dp = [[0 for i in range(m+1)] for j in range(d+2)]


    tmp_dp = copy_arr(dp)

    if x > 1:
        dp[x-1][1] = 1

    if x < m:
        dp[x+1][1] = 1

    for i in range(2,m+1):
        for j in range(1,d+1):
            for k in range(1,m+1):
                tmp_dp[j][k] = (dp[j][k] + dp[j-1][k-1] + dp[j+1][k-1])%MODK

        dp = copy_arr(tmp_dp)

    res = [1]

    for i in range(1,m+1):
        sums = 0
        for j in range(1,d+1):
            sums += dp[j][i]

        res.append(sums)

    return res

def arrayWalking(x,d,m):
    dp = [1]
    tmp_dp = [0 for i in range(d+2)]

    if x > 1:
        tmp_dp[x-1] = 1
    if x < d:
        tmp_dp[x+1] = 1

    dp.append(sum(tmp_dp))

    tmps = tmp_dp.copy()
    #print("tmps:",tmps)
    for i in range(m-1):
        for j in range(1,d+1):
            if j == 1:
                tmps[j] = tmp_dp[j+1]
            elif j == d:
                tmps[j] = tmp_dp[j-1]
            else:
                tmps[j] = (tmp_dp[j-1] + tmp_dp[j+1])%MODK

        #print("tmps:",tmps)
        tmp_dp = tmps.copy()
        dp.append(sum(tmp_dp))

    return dp



def extend_gcd(a,b):

    a1 = 1
    a2 = 0

    b1 = 0
    b2 = 1

    a3 = a
    b3 = b

    while b3 != 0 and b3 != 1:
        q = a3 // b3
        r3 = a3 - q*b3
        r1 = a1 - q*b1
        r2 = a2 - q*b2

        a1 = b1
        a2 = b2
        a3 = b3

        b1 = r1
        b2 = r2
        b3 = r3

    if b3 == 0:
        return -1
    return b2


def multiply_bit_modk(a, b):

    a = a % MODK
    b = b % MODK
    res = 0
    factor = b
    tmps = a
    while factor > 0:

        if factor % 2 == 1:
            res = (res+tmps) % MODK

        tmps = (tmps*2) % MODK
        factor = factor // 2

    return res

def gridWalking(m, x, D):
    n = len(x)

    dp = []
    res = [0]

    Pm = [1]

    for i in range(m,0,-1):
        Pm.append(multiply_bit_modk(Pm[m-i],i))

    Pm = Pm[::-1]

    fac_m = Pm[0]

    expose_facm = 1

    for i in range(n-1):
        expose_facm = multiply_bit_modk(expose_facm, fac_m)


    inverse_fac_m = extend_gcd(MODK, expose_facm)

    for i in range(n):
        dp.append(arrayWalking(x[i],D[i],m))

        for id in range(m+1):
            dp[i][id] = multiply_bit_modk(dp[i][id],Pm[id])


    res = dp[0].copy()
    tmp_res = [0 for i in range(m+1)]

    for i in range(1,n):
        tmp_res = [0 for j in range(m+1)]

        for j in range(m+1):
            for k in range(j+1):
                tmp_res[j] = (tmp_res[j] + multiply_bit_modk(res[k],dp[i][j-k])) % MODK

        res = [tmp_res[j] for j in range(m+1)]

    ult_res = multiply_bit_modk(res[m], inverse_fac_m)




    return ult_res




n = 1
m = 5
x = [int(i) for i in "4".split(' ')]
D = [int(i) for i in "4".split(' ')]

print(gridWalking(m,x,D))
print(multiply_bit_modk(10000,MODK))
#x, d, m
#print(arrayWalking(2,6,20))


