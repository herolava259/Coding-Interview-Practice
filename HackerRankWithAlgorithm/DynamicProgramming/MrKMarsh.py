
def perimerter(a,b):
    return 2*(b[0]+b[1]-a[0]-a[1])

def isGoodChoice(grid,a,b):
    return grid[a[0]][a[1]] == '.' and \
           grid[b[0]][b[1]] == '.' and \
           grid[a[0]][b[1]] == '.' and \
           grid[b[0]][a[1]] == '.'

def kMarsh(grid):
    print("impossible")
    print(isGoodChoice(grid, (0, 0), (3, 4)))


inp = """
.....
.x.x.
.....
.....
"""
grid = inp.split()


def naive_kMarsh(grid):
    m = len(grid[0])
    n = len(grid)
    maxC = 0
    for i in range(n-1):
        for j in range(m-1):
            for k in range(i+1,n):
                for l in range(j+1,m):
                    if isGoodChoice(grid,(i,j),(k,l)):
                        maxC = max(maxC,perimerter((i,j),(k,l)))

    if maxC == 0:
        return "impossible"

    return maxC
"""
.....
..xx.
..x..
x....
"""
def improved_kMarsh(grid):
    m = len(grid[0])
    n = len(grid)
    maxC = 0
    row = [0]*m
    dp = [list(row) for i in range(n)]
    possible_rows = [[] for i in range(m)]
    possible_cols = [[] for i in range(n)]



    if maxC == 0:
        return "impossible"

    return maxC


print(naive_kMarsh(grid))



def kMarsh(grid):

    rows = len(grid)
    cols = len(grid[0])

    up = [[0] * cols for _ in range(rows)]
    left = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if j > 0:
                left[i][j] = left[i][j-1] + 1 if grid[i][j-1] != 'x' else 0

            if i > 0:
                up[i][j] = up[i-1][j] + 1 if grid[i-1][j] != 'x' else 0

    max_premeiter = 0

    for i in range(1,rows):
        for j in range(1,cols):
            if grid[i][j] != 'x':
                a = i - up[i][j]
                b = 0
                while a < i and 2*(i-a) + 2*(i-b) > max_premeiter:
                    b = max(j-left[a][j], j-left[i][j])
                    while up[i][b] < i-a and b < j and 2*(i-a) + 2(j-b) > max_premeiter:
                        b += 1

                    if b < j and left[i][j] >= j-b and grid[a][b] != 'x':
                        max_premeiter = max(2*(i-a)+2*(j-b), max_premeiter)

                    a+= 1
                    b =0

    print(max_premeiter if max_premeiter > 0 else "impossible")
