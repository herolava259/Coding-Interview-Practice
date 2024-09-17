

def naive_travelAroundTheWorld(a,b,c):
    if len(a) != len(b):
        return 0
    n = len(a)

    count =0

    for beg_pos in range(n):
        current_power = 0
        for idx in range(n):
            current_power = min(current_power+a[(beg_pos + idx) % n], c) - b[(beg_pos+idx) % n]
            if current_power < 0:
                break

            if current_power >= 0 and idx == n-1:
                count += 1
                break


    return count

def naive2_travelAroundTheWorld(a,b,c):

    fusions= []

    for x,y in zip(a,b):
        fusions.append(x)
        fusions.append(-y)

    n = len(a)
    residuals = []

    sums =[]

    tmp_sum = 0

    real_sum = 0

    res_sum = 0
    for item in fusions:
        tmp_sum += item
        sums.append(tmp_sum)

        real_sum = min(c, real_sum+item)

        res_sum = max(0, tmp_sum-real_sum)

        residuals.append(res_sum)

    print(fusions)
    print(sums)
    print(residuals)


def travelAroundTheWorld(a, b, c):

    sum_city_check = len(a)

    n = len(a)
    sum_able_city = 0
    for begin in range(n-1,-1,-1):
        current_fuel = 0
        is_check = True
        for idx in range(sum_city_check):

            city_i = (begin+idx) % n

            current_fuel = min(c, current_fuel + a[city_i])

            next_fuel = current_fuel - b[city_i]

            if next_fuel < 0:
                is_check = False
                break

            current_fuel = next_fuel

        if is_check:
            sum_able_city += 1
            sum_city_check = 1
        elif sum_city_check < n:
            sum_city_check += 1

    return sum_able_city




def line_sum(arr):

    sums = 0
    sum_arr = [0]

    for item in arr:
        sums += item
        sum_arr.append(sums)

    return sum_arr

def sum_circle(sum_arr, begin, end):

    #begin and end in range [1,n]
    #sum_arr[i] is sum of first i elements of arr meaning, sum_arr has n+1 element sum_arr[0] = 0
    mid = end

    if begin > end:
        begin, end = end, begin
    # neccessary sum include begin and end
    exclusive_sum = sum_arr[end-1] - sum_arr[begin]

    return sum_arr - exclusive_sum


c = 3
a = [3,1,2]
b = [2,2,2]

print(travelAroundTheWorld(a, b, c))

# print(naive_travelAroundTheWorld(a,b,c))
#
# print(naive2_travelAroundTheWorld(a,b,c))
#
# a = [1,2,3]
# b = [2,2,2]
# print(naive2_travelAroundTheWorld(a,b,c))
#
#
# a = [2,3,1]
# b = [2,2,2]
# print(naive2_travelAroundTheWorld(a,b,c))
#
# a = [3,0,3]
# b = [2,2,2]
# print(naive2_travelAroundTheWorld(a,b,2))



