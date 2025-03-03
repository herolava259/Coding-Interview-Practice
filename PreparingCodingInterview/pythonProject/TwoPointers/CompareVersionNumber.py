

class CompareVersionSolution:
    def __init__(self, version1: str, version2: str):
        self.version1: str = version1
        self.version2: str = version2

    def solve(self) -> int:

        p1, p2 = 0, 0
        prev_p1, prev_p2 = 0, 0
        def convert_to_number(ver: str) -> int:
            p=0
            while p < len(ver) and ver[p] == '0':
                p+=1
            r_p = len(ver) -1
            level = 0
            result = 0
            while r_p >= p:
                result += (ord(ver[r_p]) - ord('0')) * 10 ** level
                level += 1
                r_p -= 1
            return result

        def compare_two_revision(ver1: str, ver2: str):
            ver1 = convert_to_number(ver1)
            ver2 = convert_to_number(ver2)

            if ver1 > ver2:
                return 1
            elif ver1 == ver2:
                return 0
            else:
                return -1

        def check_later_revision(ver: str) -> bool:

            for c in ver:
                if c != '0' and c!= '.':
                    return True
            return False


        while p1 < len(self.version1) and p2 < len(self.version2):

            if self.version1[p1] == '.' and self.version2[p2] == '.':

                compare_val = compare_two_revision(self.version1[prev_p1: p1], self.version2[prev_p2: p2])

                if compare_val != 0:
                    return compare_val

                p1 += 1
                p2 += 1
                prev_p1, prev_p2 = p1, p2
            elif self.version1[p1] == '.':
                p2 += 1
            elif self.version2[p2] == '.':
                p1 += 1
            else:
                p1 += 1
                p2 += 1

        while p1 < len(self.version1) and self.version1[p1] != '.':
            p1 +=1
        while p2 < len(self.version2) and self.version2[p2] != '.':
            p2 +=1
        compare_val = compare_two_revision(self.version1[prev_p1: p1], self.version2[prev_p2: p2])

        if compare_val != 0:
            return compare_val


        if p1 < len(self.version1):
            if check_later_revision(self.version1[p1+1:]):
                return 1
            return 0
        if p2 < len(self.version2):
            if check_later_revision(self.version2[p2+1:]):
                return -1
            return 0

        return 0

version1 = "1.2"
version2 = "1.10"

sln = CompareVersionSolution(version1, version2)

print(sln.solve())