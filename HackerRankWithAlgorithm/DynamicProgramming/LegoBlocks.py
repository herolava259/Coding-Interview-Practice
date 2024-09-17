MODK = 10**9+7
def pow2(n):

    tmp = 1
    for i in range(n):
        tmp = (tmp*2)%MODK

    return tmp

def mulModK(a,b):
    return (a*b)%MODK

def powOfN(a,n):
    res = 1
    for i in range(n):
        res =mulModK(res,a)
    return res

def showDP1Row(m):
    init = 1
    res = [1]

    for i in range(1,m+1):
        tmp = 0
        for j in range(1,5):
            if j <= i:
                tmp= (tmp+res[i])%MODK
            else:
                break

        res.append(tmp)
    return res

def legoBlocks(n, m):

    dp = showDP1Row(m)
    dp.pop(0)
    rawTb = [powOfN(item,n) for item in dp]
    s = [1]

    for i in range(1,len(rawTb)):
        sums = sum([(x*y)%MODK for x,y in zip(rawTb[:i],s[::-1])])



