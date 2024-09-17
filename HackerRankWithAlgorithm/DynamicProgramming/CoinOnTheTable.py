


def coinOnTheTable(m, k, board):

    des_x = 0
    des_y = 0
    height = len(board)
    width = m


    for i in range(height):
        for j in range(width):
            if board[i][j] == "*":
                des_y = i
                des_x = j

    if des_x + des_y > k:
        return -1

    upper_oper = 2501

    h2 = height**2
    w2 = width**2

    dp = [[[upper_oper, 0, 'D'] for j in range(width)] for i in range(height)]

    dp[0][0][0] = 0
    dp[0][0][1] = 0

    for i in range(height*width):
        for j in range(height):
            for l in range(width):
                if j == 0 and l == 0:
                    continue
                min_oper = upper_oper + 1
                temp = 0

                if j > 0 and board[j-1][l] != "*":
                    temp = dp[j-1][l][0]
                    if board[j-1][l] != "D":
                        temp += 1

                    if temp < dp[j][l][0] and dp[j-1][l][1] < k:
                        dp[j][l][0] = temp
                        dp[j][l][1] = dp[j-1][l][1] +1
                        dp[j][l][2] = "U"

                if j < height -1 and board[j+1][l] != "*":
                    temp = dp[j+1][l][0]
                    if board[j+1][l] != "U":
                        temp += 1

                    if temp < dp[j][l][0] and dp[j+1][l][1] < k:
                        dp[j][l][0] = temp
                        dp[j][l][1] = dp[j+1][l][1] + 1
                        dp[j][l][2] = "D"

                if l > 0 and board[j][l-1] != "*":
                    temp = dp[j][l-1][0]
                    if board[j][l-1] != "R":
                        temp += 1

                    if temp < dp[j][l][0] and dp[j][l-1][1] < k:
                        dp[j][l][0] = temp
                        dp[j][l][1] = dp[j][l-1][1] + 1
                        dp[j][l][2] = "L"

                if l < width - 1 and board[j][l+1] != "*":
                    temp = dp[j][l+1][0]

                    if board[j][l+1] != "L":
                        temp += 1

                    if temp < dp[j][l][0] and dp[j][l+1][1] < k:
                        dp[j][l][0] = temp
                        dp[j][l][1] = dp[j][l+1][1] + 1
                        dp[j][l][2] = "R"

    return dp, des_y, des_x

class MinHeap:
    def __init__(self,m,n):
        self.maxsize = m*n
        self.rowsize = m
        self.colsize = n
        self.queue = []
        self.board = []
        self.flag = []

        for i in range(m):
            row_arr = []
            row_flag = []
            for j in range(n):
                self.queue.append([i,j,2501])
                row_arr.append(2501)
                row_flag.append(False)

            self.flag.append(row_flag)
            self.board.append(row_arr)

    def __getitem__(self, x,y):

        return self.board[x][y]

    def __setitem__(self, key, value):
        x, y = key
        self.board[x][y] = value[0]
        self.heapify(key, value)

    def heapify(self, key, value):
        x,y = key

        for index, item in enumerate(self.queue):
            if item[0] == x and item[1] == y:
                self.queue[index] = [x,y,value]
                #self.queue.sort(reverse=True, key = lambda x: x[2])
                break

    def update(self):
        self.queue.sort(reverse=True, key=lambda x: x[2])

    def isOptimize(self, x, y):

        return self.flag[x][y]

    def pop(self):
        x =0
        y =0
        value = -1
        if self.maxsize > 0:
            self.maxsize -= 1
            x,y,value = self.queue.pop(-1)
            self.flag[x][y] = True

        return [x,y,value]


def coinOnTheTableByDijiktraAlg(m, k, board):
    des_x = 0
    des_y = 0
    height = len(board)
    width = m

    for i in range(height):
        for j in range(width):
            if board[i][j] == "*":
                des_y = i
                des_x = j

    if des_x + des_y > k:
        return -1

    upper_oper = 2501

    h2 = height ** 2
    w2 = width ** 2

    minheap = MinHeap(height,width)
    minheap[0,0] = 0
    minheap.update()

    curr_y = 0
    curr_x = 0
    value = 0
    prev_dir = board[0][0]
    while (curr_y != des_y or curr_x != des_x) and value != -1:
        curr_x, curr_y, value = dp.pop()
        # cap nhat lai cac vi tri ke voi vi tri hien tai

        #cap nhat lai min heap


    if curr_x != des_x or curr_y != des_y:
        return -1

    return value






def tracing_recur(dp, pos_y, pos_x):

    if pos_x == 0 and pos_y == 0:
        print(f"i = 1. Position (y,x) : ({pos_y}, {pos_x})")
        return 1
    next_pos_y = pos_y
    next_pos_x = pos_x

    prev_sig = dp[pos_y][pos_x][2]

    if prev_sig == "D":
        next_pos_y += 1
    elif prev_sig == "U":
        next_pos_y -= 1
    elif prev_sig == "L":
        next_pos_x -= 1
    elif prev_sig == "R":
        next_pos_x += 1
    else:
        print(f"Error at position: {pos_y}, {pos_x}")
        return 2501

    order = tracing_recur(dp, next_pos_y, next_pos_x) + 1

    print(f"i = {order}. Position (y,x): ({pos_y}, {pos_x})")
    return order


def print_tracing_result(dp, des_y, des_x):

    tracing_recur(dp, des_y, des_x)




n,m,k = [int(i) for i in "2 2 3".split(" ")]

board_str = """RD
*L"""

board = [list(row) for row in board_str.split('\n')]
#print(board)
dp, des_y, des_x = coinOnTheTable(m, k, board)

print("Result: ",dp[des_y][des_x][0])

print(print_tracing_result(dp, des_y, des_x))
