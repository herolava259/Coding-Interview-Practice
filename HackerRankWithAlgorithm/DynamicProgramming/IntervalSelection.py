

def calc_overlap_between_2_intervals(interval1, interval2):
    ci1 = tuple(interval1)
    ci2 = tuple(interval2)

    overlap = 0
    if ci1[1] > ci2[1]:
        tmp = ci1
        ci1 = ci2
        ci2 = tmp

    if ci1[1] >= ci2[0]:
        return ci1[1] - max(ci2[0], ci1[0]) + 1
    return 0

print(calc_overlap_between_2_intervals((1,10), (1,3)))


def naive_intervalSelection(intervals):

    n = len(intervals)

    overlaping_matrix = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            overlaping_matrix[i][j] = calc_overlap_between_2_intervals(intervals[i], intervals[j])


def sort_two_element(intervals):
    n = len(intervals)
    intervals.sort(key=lambda x: x[0], reverse=False)

    begin = 0
    for idx in range(1, n):
        if intervals[idx][0] != intervals[idx - 1][0]:
            tmp_list = intervals[begin:idx]
            tmp_list.sort(key=lambda x: x[1], reverse=False)
            for j in range(begin, idx):
                intervals[j] = tmp_list[j-begin]
            begin = idx
    



def naive2_intervalSelection(intervals):

    n = len(intervals)

    #sort_two_element(intervals)
    #print(intervals)

    intervals.sort(key=lambda x: x[1], reverse=False)

    # 1,1 ; 1,2 ; 2,3 ; 2,4

    count_max_intervals = 2

    lower = min(intervals[0][1], intervals[1][1])
    upper = max(intervals[0][1], intervals[1][1])+1
    if n <= 2:
        return count_max_intervals

    for item in intervals[2:]:
        if item[0] > lower:
            count_max_intervals += 1
            if item[0] >= upper:
                lower = item[0]-1
                upper = item[1]+1


            lower = min(item[1], upper-1)
            upper = max(item[1], upper-1)+1

    return count_max_intervals

def greedy_intervalSelection(intervals):
    intervals.sort(key=lambda x: x[1], reverse=False)

    noOfSelections = 0
    busy = [[0,0],[0,0]]

    for interval in intervals:
        if interval[0] > busy[1][1]:
            noOfSelections += 1
            busy[1] = interval
        else:
            if interval[0] > busy[0][1]:
                noOfSelections += 1
                busy[0] = interval
                if interval[1] > busy[1][1]:
                    (busy[0],busy[1]) = (busy[1],busy[0])

    return noOfSelections


inp = [[1,12], [1,3],[3,5],[4,6],[6,8],[7,10],[8,12]]


print(naive2_intervalSelection(inp))

print(greedy_intervalSelection(inp))