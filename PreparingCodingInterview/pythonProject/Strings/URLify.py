from typing import List

class URLifySolution:
    def __init__(self, url: List[str]):
        self.url: List[str] = url
        self.n:int = len(url)

    def solve(self) -> str:

        p_curr = self.n - 1

        while p_curr >= 0 and self.url[p_curr] == ' ':
            p_curr -= 1

        p_c = self.n - 1

        while p_curr >= 0:
            while p_curr >= 0 and self.url[p_curr] != ' ':
                self.url[p_c] = self.url[p_curr]
                p_c -= 1
                p_curr -= 1
            if p_curr >= 0:
                self.url[p_c] = '%'
                p_c -= 1
                self.url[p_c] = '0'
                p_c -= 1
                self.url[p_c] = '2'
                p_c -= 1
                p_curr -= 1

        return ''.join(self.url)


url_inp = 'Mr John Smith    '
url_arr = [c for c in url_inp]
sln = URLifySolution(url_arr)
print(sln.solve())