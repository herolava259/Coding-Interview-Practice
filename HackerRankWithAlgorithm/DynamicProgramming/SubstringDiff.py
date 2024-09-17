
from collections import deque

def naive_substringDiff(k, s1, s2):


    if len(s1) > len(s2):
        tmp = s2
        s2 = s1
        s1 = tmp

    len_s1 = len(s1)
    len_s2 = len(s2)
    m = len_s1

    for l in range(m,1,-1):
        for i in range(len_s1-l+1):
            for j in range(len_s2-l+1):
                diff_count = 0

                t = 0
                while diff_count <= k and t < l:
                    if s1[i+t] != s2[j+t]:
                        diff_count +=1
                    t+=1

                if diff_count <= k:
                    return l



    return 0


def dp_substringDiff1(k, s1, s2):
    pattern  = [0]*1501

    dp = [list(pattern) for i in range(1501)]

    lenS1 = len(s1)
    lenS2 = len(s2)

    maxLen = 0

    for i in range(lenS1):
        for j in range(lenS2):
            if s1[i] != s2[j]:
              dp[i][j] += 1
            maxLen = 1

            if dp[i][j] > k:
                dp[i][j] = -1
                maxLen = 0


    n = min(lenS1,lenS2)+1

    for l in range(2,n):
        for i in range(lenS1):
            for j in range(lenS2):
                if dp[i][j] != -1:
                    if i+l <= lenS1 and j+l <= lenS2:
                        if s1[i+l-1] != s2[j+l-1]:
                            dp[i][j] += 1
                        if dp[i][j] > k:
                            dp[i][j] = -1
                        else:
                            maxLen = l
                    else:
                        dp[i][j] = -1



    return maxLen

def create_list(n):
    sample = [1,0]
    return [sample.copy() for i in range(n)]

def optimize_substringDiff(k, s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    size_s = max(len_s1,len_s2)+1
    dp = [[[1,0] for j in range(size_s)] for i in range(size_s)]


    for i in range(len_s2):
        if s1[len_s1-1] != s2[i]:
            dp[len_s1-1][i][1] = 1
            if k == 0:
                dp[len_s1-1][i][0] =0
    for i in range(len_s1):
        if s2[len_s2-1] != s1[i]:
            dp[i][len_s2][1] = 1
            if k == 0:
                dp[i][len_s2-1][0] =0
    maxlen = 0
    print(dp)
    for i in range(len_s1-2, -1,-1):
        for j in range(len_s2-2,-1,-1):

            if s1[i] == s2[j]:
                dp[i][j][0] = dp[i+1][j+1][0]+1
                dp[i][j][1] = dp[i+1][j+1][1]
            else:
                if dp[i+1][j+1][1] < k:
                    dp[i][j][0] = dp[i+1][j+1][0]+1
                    dp[i][j][1] = dp[i+1][j+1][1]+1
                else:

                    offset = dp[i+1][j+1][0]

                    while offset >= 0 and s1[i+offset] == s2[j+offset]:
                        offset -= 1
                    offset = offset if offset > 0 else 1
                    dp[i][j][0] = offset
                    dp[i][j][1] = dp[i+1][j+1][1]

            # print("i: ", i)
            # print("j: ", j)
            # print("dp[i][j]: ", dp[i][j] )
            maxlen = max(maxlen, dp[i][j][0])

    return maxlen

def opt_ver2_substringDiff(k, s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)

    dp = [[1,0] if s1[len_s1-1] == s2[i] else [1,1] if k>0 else [0,0]  for i in range(len_s2)]
    tmp_dp = [[1, 0] if s1[len_s1 - 1] == s2[i] else [1, 1] if k > 0 else [0, 0] for i in range(len_s2)]



    maxlen = 0
    diff12 = [[len_s1-1] if len_s1-1-i > 0 and s1[-1] != s2[len_s1-1-i] else [] for i in range(len_s1)] # when id_ofs1 > id_ofs2
    diff21 = [[len_s2-1 -i ] if len_s2-1-i > 0 and s2[-1] != s1[len_s2-1-i] else [] for i in range(len_s2)] # when id_ofs1 < id_ofs2
    print(dp)
    for i in range(len_s1-2, -1,-1):
        tmp_dp[len_s2-1] = [1,0] if s1[i] == s2[len_s2-1] else [1,1] if k>0 else [0,0]
        print("i: ", i)
        for j in range(len_s2-2,-1,-1):

            if s1[i] == s2[j]:
                tmp_dp[j][0] = dp[j+1][0]+1
                tmp_dp[j][1] = dp[j+1][1]
            else:
                if i > j:
                    diff12[i-j].append(i)
                else:
                    diff21[j-i].append(i)

                if dp[j+1][1] < k:
                    tmp_dp[j][0] = dp[j+1][0]+1
                    tmp_dp[j][1] = dp[j+1][1]+1
                else:
                    last_id =  i
                    if i > j:
                        last_id = diff12[i-j][0]
                        diff12[i-j].pop(0)
                    else:
                        last_id = diff21[j-i][0]
                        diff21[j-i].pop(0)

                    offset = last_id-i


                    tmp_dp[j][0] = offset
                    tmp_dp[j][1] = dp[j+1][1]


            print("j: ", j)
            print("dp[j]: ", dp[j] )
            maxlen = max(maxlen, tmp_dp[j][0])


        tmp = dp
        dp = tmp_dp
        tmp_dp = tmp
        print(tmp_dp)
        print(dp)
        print("\n")


    return maxlen

def solution_substringDiff(k, s1, s2):
    longest = 0

    for d in range(-len(s1)+1, len(s2)):
        i = max(-d,0) + d
        j = max(-d,0)

        q = deque(maxlen=k)
        s = 0

        for p in range(0,min(len(s2)-i, len(s1)-j)):
            if s1[i+p] != s2[j+p]:
                if k > 0:
                    if len(q) == k:
                        s = q[-1] + 1
                    q.appendleft(p)
                else:
                    s = p+1
            if p+1-s > longest:
                longest = p+1-s

    return longest

s1 = "tabriz"
s2 = "torino"
k = 0

[s1,s2] = "abacba abcaba".split(' ')
print(naive_substringDiff(k,s1,s2))

print(dp_substringDiff1(k,s1,s2))

print(opt_ver2_substringDiff(k,s1,s2))