import math
import os
import random
import re
import sys


def playWithWords(s):

    n = len(s)
    dp = maxPanlidrome(s)
    print('dp = ', dp)
    maxs = 0
    for i in range(n-1):
        maxLenS1 = dp[0][i]
        maxLenS2 = dp[i+1][n-i-2]

        maxs = max(maxs, maxLenS1 * maxLenS2)

        # print('P1 = ', s[:i+1])
        # print('P2 = ', s[i+1:])
        print('maxLenS1 = ', maxLenS1)
        print('maxLenS2 = ', maxLenS2)
        print('---------------')

    return maxs





def maxPanlidrome(s):

    n = len(s)

    print('n = ', n)
    dp = [[1 for j in range(n-i)] for i in range(n)]


    firstIdxArr = firstIdxOfCharacterAppear(s)

    a_idx = ord('a')

    for i in range(n):
        char_idx = ord(s[i]) - a_idx

        for j in range(i):
            last_max_length = 1
            first_idx = firstIdxArr[char_idx][j]
            if first_idx < i:
                last_max_length = 2 + dp[first_idx + 1][i - first_idx - 2] if i - first_idx >= 2 else 2
            dp[j][i-j] = max(dp[j][i-j-1], last_max_length)
    #print('dp = ', dp)
    return dp





def firstIdxOfCharacterAppear(s):
    n = len(s)
    firstAppearArr = [[-1 for j in range(n)] for i in range(26)]

    last_update = [-1 for i in range(26)]

    a_idx = ord('a')

    for idx, c in enumerate(s):
        i = ord(c) - a_idx
        begin = last_update[i] + 1
        for j in range(begin, idx+1):
            firstAppearArr[i][j] = idx
        last_update[i] = idx

    return firstAppearArr


inp = 'baaabbabbaaaaaaaababbbbababaaabaabbbbbbbbbababbabbaaaabbabbbbbababbbbabaabbbaaabaaabaabaabbbaababbababaaaabaabbaaaabaaabbbabbabbbbababaaaaaabbbababbbabbbbbbaaaaababbabbaabbabbbbbbaabbabababbbaabbababbbbababbbabaaabbaaaaabaaaababbaaababaaaaaaaabbaabaabbbabbaaaaabbaabaaabbbababbbbbaabbabaabbbbbabaababababbbbaabaaabbaaabaaababbbaaabbabbbabaababbbabbabbbbbabbaaabaabaaaababbabaabaaababbabbaaaababbaabbbbabaababbbaababbbabbbaabaabbbbaaaaabababbaabbababaaabaaaababbbbaaaaaabbbababbaababbbabbababbbaaabbaabbbbabbaaaaabbbbbbaaababbaaaababbbabbbabaaababbabaabaabbbbaabababaabbaaabaaabbaabbaaaaaaaabababaaabaabbaabbbbaaabaaaaaaababaababbababbaaabbaaabaaababaabbbabaabaaabababbbabababababaaaaababbaabbbaaaaababbabaaabaaaababaaabbaaaaaaaababababbbbabbabbbbbabaaabbbbaabaaabbbaaabababbbaabbaabbabbababaaaaabbaaabaabaaabbbababbbbababbbbaababaaaabbabbbaabbbbabababaabaabaaaabaabbbaaabbbbbababbbbbaababbbaabbaaabaabaababaabbaababbaaabaaaabaaaabbbaaabaaaababbbbabbbbbabbbbabbaaaabaaaaaababbaaaabaabbbababbbaabbbbaaaabbbabaababaabaabaaabbbbaababaaaabbaaaababbbaaabaaababbbbabbabbaaabbaaaabbaabbaaaaababbbbaababababaaabbaaaaabbbbaaaaababaaaabbbaabbbbbbaabaaaabbabbaaaabbaababbaabaaaaabbbabaabbbaabbaaaabbabaaababbaaaabababbbabbaababbaabbbbbabbaabaaabababaabbabaaaaaabababbabbaabbaaaaababaabababaaaaaaabbaaabbabbbbbbaabbbaaababbaabbbabababaabbaabababbbaabbbbbabbaaabbabbbbbbabbabbaabaaaababbaabbbbbbaababbaabbbbbabaaaabbaaabbabaabababababbbabababbbbbbaababbababaabbabbabbbabbaaaaabbbbbabbabbaaababbbbabbbaabbabbaaabababbbabbabaaabababaaabaabbbababaaaababbbabaaaabbbbaaaaabbbaaaaabaaaaaaaababaabaababababbaaaaaabaababbbabbbaabbbaaaababbabababaabbbaababaaaaaaabbbaaaaabababababbbbaaabbbbabbbbbaabaaabaaaaababbaabbababbbaaabaababbbbabbababaabbbaaabbaabbaababbaaabbbbbbbaabaababaaaaabababbbbbaaababaababbaabaaaaabaaabbbbaabbbababababbbbbbbaaabaabbabaabbaaabaaaaabbbaaabaababaabbabaabbabbbbbaaaabbbbbabbbaaabbaabaaaababbaaaabababaabaaaaaabaabbbaaaaaabbabbaabbbabbbbabababbaabbbbabbabbbabbaaabaabbbababbbbaaabbabbabaaaaaababaaaaababbabbaabbaabaaaaaaaababaabbbbaaabbababbaaababababbababababbaababbabbaaaabaaaaaaaabaaabaabaaaabbbbababbbabaaaaaaaaababaaabaabaabbaabaaaaaabaaaaaabbabbaabababbaabaabaababbbbaabbbaabaaaaabbaaabaababbbaabaaaaaaababbaaaaabaabaaaaaaabbabaaaaaabbbbbbaaaaaabbaaaaabaaabbabaababbababbbbbabbbbabababbabaaaabaaabaaaaaaaababbabbabaaabbbbbabbaaaabaabbbbbbbbababaaabaabaabbbaababbabaaaabbabaaabbaaaabbaabbababaabaabbabaabbbabbbbbababbaaaabbbabaaaaaaaaabaabbabbaabbbaaaabababbaabbabbbbbabaabbabbabbabbbaabbabbaabbabbbababbbaabbaabbbaaabaababbaabaaaabbbababbaaaabbababbbabbabbaaaabaaaabbaaaaaaaabbaabbbbaabbbbaabbbbaabbabaaabaaabbbbbaabaaabbabaabbbababbaabbbbbaaabbbaaaababbbbbaaaabaabbbabaabbbbbbaaabbbbaabbbabbabbbaabbbabbabaabbaabbbabaaabbbabbababaaaaaabbabaabbbbaababbaabbbabaaabbbbbbbbbbabaabbbbaaabaaaabbbbbaaabaaabaaabbabbaaaaaabbabbbaabaaaaaaabbbbaaababbabaabaabaabaabbbabaaabaaabbabaabbbaabaaaaababaaabbaaaabbbaaabaaaabbbababbbbaaaabbbaabbbaabaaababbabaababbaaaabbbabaaaabbababbbaabbbbaaabaabbabbabaa'#'eeegeeksforskeeggeeks'

print(playWithWords(inp))


print(maxPanlidrome('decbaeadcecada'))