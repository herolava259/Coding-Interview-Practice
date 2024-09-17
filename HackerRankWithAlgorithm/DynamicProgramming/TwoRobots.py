

def twoRobots(m, queries):

    n = len(queries)

    dp = [100000 for i in range(n)]

    dp[0] = abs(queries[0][0]-queries[0][1])
    dp[1] = dp[0] + abs(queries[1][0]-queries[1][1])
    total_dist = abs(queries[0][1]-queries[1][0])+ dp[1]

    dp[0] = dp[1]
    for i in range(2, n):
        inc = abs(queries[i][0]-queries[i][1])
        curr_dp = total_dist + abs(queries[i][0]-queries[i][1])
        prev_dist = curr_dp
        total_dist += inc + abs(queries[i][0]-queries[i-1][1])
        for j in range(i):
            ass_dp = dp[j]+inc+abs(queries[j][1]-queries[i][0])
            if j < i-1:
                prev_dist = min(ass_dp, prev_dist)
            curr_dp = min(curr_dp, ass_dp)
            dp[j] += inc + abs(queries[i][0]-queries[i-1][1])
        dp[i-1] = prev_dist
        dp[i] = curr_dp

    return dp[-1]

def greedy_twoRobots(m, queries):

    total_dist = 1000000000

    n = len(queries)
    for i in range(n-1):
        tmp_total = abs(queries[0][0]-queries[0][1])
        pos_robot2 = queries[i+1][1]
        pos_robot1 = queries[0][1]
        for idx, query in enumerate(queries[1:]):
            flag = True
            if i > idx:
                if abs(queries[i][0]-pos_robot1) > abs(queries[i][0]-pos_robot2):
                    flag = False

            if flag:
                tmp_total += abs(queries[i][0] - queries[i][1]) + abs(queries[i][0]-pos_robot1)
                pos_robot1 = queries[i][1]
            else:
                tmp_total += abs(queries[i][0] - queries[i][1]) + abs(queries[i][0]-pos_robot2)
                pos_robot2 = queries[i][1]

        total_dist = min(total_dist,tmp_total)

    return total_dist

inps = [(1,5), (3,2), (4,1), (2,4)]
m = 5


def opt_twoRobots(m, queries):
    n = len(queries)
    posr1 = 0
    posr2 = 0

    for query in queries:
        pass

minS = 10000000
def solve(n, queries, k, r1, r2, sum):
    global minS
    if k == n:
        minS = min(minS, sum)
        return

    solve(n, queries, k + 1, queries[k][1], r2, sum+abs(r1-queries[k][0])+abs(queries[k][0]-queries[k][1]))
    r2 = queries[k][0] if r2 == 0 else r2
    solve(n, queries, k + 1, r1, queries[k][1], sum + abs(r2 - queries[k][0]) + abs(queries[k][0] - queries[k][1]))

def other_twoRobots(m, queries):
    return "HA HA"

print(greedy_twoRobots(m,inps))
solve(len(inps),inps,1,inps[0][1],0,abs(inps[0][1]-inps[0][0]))
print(minS)

print(twoRobots(m,inps))
