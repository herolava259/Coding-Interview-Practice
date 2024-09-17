import os
import sys


def cutTree(n, k, edges):
    tree = [list() for i in range(n + 1)]

    for edge in edges:
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])

    print(tree)
    counter = 0

    def solve(k, prev_node, curr_node):

        m = len(tree[curr_node])
        m = m - 1 if prev_node > 0 else m
        dp = [0 for i in range(k + 1)]

        if m == 0:
            dp[0] = 1
            dp.append(1)
            print("curr node:", curr_node)
            print("dp: ")
            print(dp)
            print("total:", sum(dp[:-1]))
            print("\n")
            return dp

        tmp_dp = [0 for i in range(k + 1)]
        sums = 0
        first_node = tree[curr_node][0] if tree[curr_node][0] != prev_node else tree[curr_node][1]

        res = solve(k, curr_node, first_node)
        sums += res[-1]
        res[1] += 1
        print("res: ", res)
        for i in range(k + 1):
            dp[i] = res[i]

        for v in tree[curr_node]:
            if v != prev_node and v != first_node:

                res = solve(k, curr_node, v)
                sums += res[-1]
                res[1] += 1

                print("res: ", res)
                for i in range(k + 1):
                    for j in range(i + 1):
                        tmp_dp[i] += res[j] * dp[i - j]
                dp = tmp_dp.copy()
                tmp_dp = [0 for i in range(k + 1)]

        print("curr node:", curr_node)
        print("dp: ", dp)
        print("total:", sum(dp[:-1]))
        print("\n")
        sums += sum(dp[:-1])
        dp.append(sums)
        return dp

    ress = solve(k, -1, 1)

    counter += ress[-1] + ress[k] + 1
    return counter


n = 10
k = 3
inps = [(10, 8), (7, 10), (2, 10), (5, 4), (6, 1), (2, 6), (4, 2), (9, 2), (7, 3)]
# [[2,1], [2,3]]

print(cutTree(n, k, inps))
