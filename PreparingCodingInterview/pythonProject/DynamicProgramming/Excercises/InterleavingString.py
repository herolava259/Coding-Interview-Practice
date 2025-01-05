from typing import List


class InterleavingStringSolution:
    def __init__(self, s1: str, s2: str, s3: str):
        self.s1: str = s1
        self.s2: str = s2
        self.s3: str = s3

    def dp_solve(self) -> bool:

        if (len(self.s1) + len(self.s2)) != len(self.s3):
            return False

        dp = [[False for _ in range(len(self.s2) + 1)] for _ in range(len(self.s1) + 1)]

        dp[0][0] = True
        for i in range(1, len(self.s2) + 1):
            dp[0][i] = dp[0][i-1] and (self.s2[i-1] == self.s3[i-1])

        for i in range(1, len(self.s1) + 1):
            dp[i][0] = dp[i-1][0] and (self.s1[i-1] == self.s3[i-1])

        for i in range(1, len(self.s1) + 1):
            for j in range(1, len(self.s2) + 1):
                dp[i][j] = (dp[i-1][j] and self.s1[i-1] == self.s3[i+j-1]) or (dp[i][j-1] and self.s2[j-1] == self.s3[i+j-1])

        return dp[len(self.s1)][len(self.s2)]

    def solve(self):
        map_idx = [[] for _ in range(26)]

        for idx, c in enumerate(self.s3):
            map_idx[ord(c) - ord('a')].append(idx)

        return self.isInterleave(0, 0, [False for _ in range(len(self.s3))], map_idx)

    def isInterleave(self, p2: int, p3: int, flags: List[bool], map_idx: List[List[int]]) -> bool:
        if p2 == len(self.s2):
            p1 = 0
            for i in range(len(self.s3)):
                if flags[i]:
                    continue
                if self.s1[p1] != self.s3[i]:
                    return False
                p1 += 1
            return p1 == len(self.s1)

        for idx in map_idx[ord(self.s2[p2]) - ord('a')]:
            if idx < p3:
                continue
            flags[idx] = True
            if self.isInterleave(p2 + 1, idx + 1, flags, map_idx):
                return True
            flags[idx] = False
        return False


def isInterleave(s1: str, s2: str, s3: str, p1: int, p2: int, p3: int):
    if p1 == len(s1) - 1 and p2 == len(s2) - 1 and p3 == len(s3) - 1:
        return True

    check1, check2 = False, False

    if p1 < len(s1) - 1 and s1[p1 + 1] == s3[p3 + 1]:
        check1 = isInterleave(s1, s2, s3, p1 + 1, p2, p3 + 1)
    if p2 < len(s2) - 1 and s2[p2 + 1] == s3[p3 + 1]:
        check2 = isInterleave(s1, s2, s3, p1, p2 + 1, p3 + 1)

    return check1 or check2


s11, s12, s13 = "acaccabaabcbbacaacaaaacabbac", "accbccbccccabaaabcacabbaba", "acaccabccbcccaccababaaaababcaccbcbacababacbaaaaacabbac"
sln = InterleavingStringSolution(s11, s12, s13)

#print(sln.solve())
print(sln.dp_solve())
#print(isInterleave('aabcc', 'dbbca', 'aadbbbaccc', -1, -1, -1))
