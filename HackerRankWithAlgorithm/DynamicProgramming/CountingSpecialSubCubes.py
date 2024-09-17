import math
import random
import os
import re
import sys


def specialSubCubes(cube):
    return 3, 6


def access_cube_unit(cube, k_size, x, y, z):
    return cube[(x - 1) * k_size ** 2 + (y - 1) * k_size + z]


def convert_to_3d_tensor(cube_flat_arr, cube_size=None):
    if cube_size is None:
        k_pow_3 = len(cube_flat_arr)
        cube_size = math.ceil(math.pow(k_pow_3, 1 / 3))

    cube_tensor = []
    square_k = cube_size ** 2
    for x in range(cube_size):
        slice_x = []
        for y in range(cube_size):
            slice_xy = []
            begin_xy = x * square_k + y * cube_size
            slice_xy.extend(cube_flat_arr[begin_xy: begin_xy + cube_size])
            slice_x.append(slice_xy)

        cube_tensor.append(slice_x)

    return cube_tensor, cube_size


def check_has_special_cube_tensor(parent_cub, x_beg, y_beg, z_beg, k_size, cube_size=None):
    if cube_size is None:
        cube_size = len(parent_cub)

    x_end = min(cube_size, x_beg + k_size)
    y_end = min(cube_size, y_beg + k_size)
    z_end = min(cube_size, z_beg + k_size)

    for x in range(x_beg, x_end):
        for y in range(y_beg, y_end):
            for z in range(z_beg, z_end):
                if parent_cub[x][y][z] == k_size:
                    return True
    return False


def check_is_special_cube_tensor(parent_cub, x_beg, y_beg, z_beg, k_size, cube_size=None):
    if cube_size is None:
        cube_size = len(parent_cub)

    x_end = x_beg + k_size
    y_end = y_beg + k_size
    z_end = z_beg + k_size
    if x_end > cube_size or y_end > cube_size or z_end > cube_size:
        return False

    for x in range(x_beg, x_end):
        for y in range(y_beg, y_end):
            for z in range(z_beg, z_end):
                if parent_cub[x][y][z] == k_size:
                    return True
    return False


def naive_specialSubCubes(cube):
    cube_3d, cube_size = convert_to_3d_tensor(cube)
    results = []
    for win_size in range(1, cube_size + 1):
        k_special_num = 0
        for x_beg in range(cube_size):
            for y_beg in range(cube_size):
                for z_beg in range(cube_size):
                    if check_is_special_cube_tensor(cube_3d, x_beg, y_beg, z_beg, win_size, cube_size):
                        k_special_num += 1

        results.append(k_special_num)

    return results


def create_cube(k_size, default_value=0):
    new_cube = []

    for x in range(k_size):
        yz_plan = []
        for y in range(k_size):
            z_array = [default_value for i in range(k_size)]
            yz_plan.append(z_array)

        new_cube.append(yz_plan)

    return new_cube


def sum_cube(cube, k_size=None):
    if k_size is None:
        k_size = len(cube)

    sum_cub = 0

    for x in range(k_size):
        for y in range(k_size):
            sum_cub += sum(cube[x][y])
    # cub is cube not cub car
    return sum_cub


def update_exist(ex_cub, x_coord, y_coord, z_coord, k_size, cub_size=None, update_val=1):
    if cub_size is None:
        cub_size = len(ex_cub)
    x_beg = max(0, x_coord + 1 - k_size)
    y_beg = max(0, y_coord + 1 - k_size)
    z_beg = max(0, z_coord + 1 - k_size)

    x_end = min(x_coord, cub_size - 1)
    y_end = min(y_coord, cub_size - 1)
    z_end = min(z_coord, cub_size - 1)

    # print("-----")
    # print("cub_size = ", cub_size)
    # print(f"x belong [{x_beg};{x_end}]")
    # print(f"y belong [{y_beg};{y_end}]")
    # print(f"z belong [{z_beg};{z_end}]")

    for x in range(x_beg, x_end + 1):
        for y in range(y_beg, y_end + 1):
            for z in range(z_beg, z_end + 1):
                ex_cub[x][y][z] = update_val
    # print("end ----------------")


def opt1_specialSubCubes(cube):
    cube_3d, cube_size = convert_to_3d_tensor(cube)
    exist_cube_arr = [create_cube(cube_size - i) for i in range(cube_size)]
    for x in range(cube_size):
        for y in range(cube_size):
            for z in range(cube_size):
                kk = cube_3d[x][y][z]
                belong_cube = exist_cube_arr[kk - 1]
                update_exist(belong_cube, x, y, z, kk, update_val=1)

    results = [sum_cube(item) for item in exist_cube_arr]
    return results


def update_max_k_subcube(mark_cube, x_coord, y_coord, z_coord, k_size, cub_size=None):
    if cub_size is None:
        cub_size = len(mark_cube)
    x_beg = max(0, x_coord + 1 - k_size)
    y_beg = max(0, y_coord + 1 - k_size)
    z_beg = max(0, z_coord + 1 - k_size)

    x_end = min(x_coord, cub_size - 1)
    y_end = min(y_coord, cub_size - 1)
    z_end = min(z_coord, cub_size - 1)

    # print("-----")
    # print("cub_size = ", cub_size)
    # print(f"x belong [{x_beg};{x_end}]")
    # print(f"y belong [{y_beg};{y_end}]")
    # print(f"z belong [{z_beg};{z_end}]")

    for x in range(x_beg, x_end + 1):
        for y in range(y_beg, y_end + 1):
            for z in range(z_beg, z_end + 1):
                mark_cube[x][y][z] = max(mark_cube[x][y][z], k_size)
    # print("end ----------------")


def counting_special_subcube(mark_cube, cube_size=None):
    if cube_size is None:
        cube_size = len(mark_cube)
    results = [0 for i in range(cube_size + 1)]

    for x in range(cube_size):
        for y in range(cube_size):
            for z in range(cube_size):
                results[mark_cube[x][y][z]] += 1

    results.pop(0)

    return results


def real_opt1_specialSubCubes(cube):
    cube_3d, cube_size = convert_to_3d_tensor(cube)

    mark_cube = create_cube(cube_size, 0)

    for x in range(cube_size):
        for y in range(cube_size):
            for z in range(cube_size):
                kk = cube_3d[x][y][z]
                update_max_k_subcube(mark_cube, x, y, z, kk, cube_size)

    return counting_special_subcube(mark_cube, cube_size)


def check_is_max_special_cube(cube_3d, x_beg, y_beg, z_beg, win_size, cube_size=None):
    if cube_size is None:
        cube_size = len(cube_3d)

    x_end = x_beg + win_size - 1
    y_end = y_beg + win_size - 1
    z_end = z_beg + win_size - 1

    if x_end > cube_size - 1 or y_end > cube_size - 1 or z_end > cube_size - 1:
        return False

    is_special = False
    for x in range(x_beg, x_end + 1):
        for y in range(y_beg, y_end + 1):
            for z in range(z_beg, z_end + 1):
                if cube_3d[x][y][z] > win_size:
                    return False
                elif cube_3d[x][y][z] == win_size:
                    is_special = True

    return is_special


def naive_max_subspecial_cube(cube_flattened):
    cube_3d, cube_size = convert_to_3d_tensor(cube_flattened)

    results = []

    for win_size in range(1, cube_size + 1):
        count_special_k = 0
        for x in range(cube_size):
            for y in range(cube_size):
                for z in range(cube_size):
                    if check_is_max_special_cube(cube_3d, x, y, z, win_size, cube_size):
                        count_special_k += 1
        results.append(count_special_k)

    return results


def classify_point_to_bucket(cube_3d, cube_size=None):
    if cube_size is None:
        cube_size = len(cube_3d)
    bucket_dozen = [[] for _ in range(cube_size + 1)]
    for x in range(cube_size):
        for y in range(cube_size):
            for z in range(cube_size):
                bucket_dozen[cube_3d[x][y][z]].append((x, y, z))
    return bucket_dozen


def calc_effect_region_of_point(x_coord, y_coord, z_coord, k_size, cube_size):
    x_beg = max(0, x_coord + 1 - k_size)
    y_beg = max(0, y_coord + 1 - k_size)
    z_beg = max(0, z_coord + 1 - k_size)

    x_end = min(x_coord, cube_size - 1)
    y_end = min(y_coord, cube_size - 1)
    z_end = min(z_coord, cube_size - 1)

    return (x_beg, y_beg, z_beg), (x_end, y_end, z_end)


def mark_and_update_state(mark_cube_list, coord, win_size):
    curr_mark_cube = mark_cube_list[win_size - 1]
    curr_cube_size = len(curr_mark_cube)
    (x_beg, y_beg, z_beg), (x_end, y_end, z_end) = \
        calc_effect_region_of_point(coord[0], coord[1], coord[2], win_size, curr_cube_size)

    for x in range(x_beg, x_end + 1):
        for y in range(y_beg, y_end + 1):
            for z in range(z_beg, z_end + 1):
                if curr_mark_cube[x][y][z] == 0:
                    curr_mark_cube[x][y][z] = 1

    for sub_win_size in range(1, win_size):
        sub_mark_cube = mark_cube_list[sub_win_size - 1]
        sub_cube_size = len(sub_mark_cube)
        (x_beg_vir, y_beg_vir, z_beg_vir), (x_end_vir, y_end_vir, z_end_vir) = \
            calc_effect_region_of_point(coord[0], coord[1], coord[2], sub_win_size, sub_cube_size)

        for x in range(x_beg_vir, x_end_vir + 1):
            for y in range(y_beg_vir, y_end_vir + 1):
                for z in range(z_beg_vir, z_end_vir + 1):
                    sub_mark_cube[x][y][z] = -1


def bucket_max_subspecial(cube_flattened):
    cube_3d, cube_size = convert_to_3d_tensor(cube_flattened)

    bucket_dozen = classify_point_to_bucket(cube_3d, cube_size)

    mark_cube_list = [create_cube(cube_size - i, 0) for i in range(cube_size)]

    for win_size in range(cube_size, 0, -1):
        for coord in bucket_dozen[win_size]:
            mark_and_update_state(mark_cube_list, coord, win_size)

    results = [0 for i in range(cube_size)]

    for i in range(cube_size):
        curr_mark_cube = mark_cube_list[i]

        for plan in curr_mark_cube:
            for line in plan:
                for val in line:
                    if val == 1:
                        results[i] += 1

    return results


##### Test #######

cube_flattended = [1, 1, 1, 1, 2, 1, 1, 2]
cube_flattended = list(map(int, "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 3 1 1 1 3 1 2 2".split(" ")))
# 2 1 1 1 1 1 1 1
# cube_flattended = list(map(int, "2 1 1 1 1 1 1 1".split(" ")))
print(type(cube_flattended))
cube_3d_inp, _ = convert_to_3d_tensor(cube_flattended)
print(cube_3d_inp)
# print(naive_specialSubCubes(cube_flattended))
print(opt1_specialSubCubes(cube_flattended))
print(real_opt1_specialSubCubes(cube_flattended))

print("Test max 1: ")
cube_flattended = list(map(int, "1 1 1 1 1 3 1 1 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 2".split(" ")))
print(naive_max_subspecial_cube(cube_flattended))

cube_flattended = list(map(int, "1 1 1 1 1 1 1 1 2 1 1 1 1 3 1 2 2 1 1 1 1 1 1 1 1 1 1".split(" ")))
print(naive_max_subspecial_cube(cube_flattended))

cube_flattended = list(map(int, "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 3 1 1 1 3 1 2 2".split(" ")))
print(naive_max_subspecial_cube(cube_flattended))
print(bucket_max_subspecial(cube_flattended))

print("Test max 2: ")
inp = "1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 3 1 1 1 1 1 1 1 1 2 1 1 1 1 1 2 1 3 1 1 1 2 1 1 1 2 1 1 1 2 1 1 1 1 2 3 1 1 1 1 1 1 1 1 2 1 1 4 1 1 4 1 1 1 1 3 3 1 1 1 1 1 3 3 1 1 1 1 1 1 3 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 1 1 1 7 1 4 1 2 1 1 1 1 1 1 1 1 1 2 1 2 2 1 2 1 1 1 1 3 4 1 4 1 1 1 1 1 1 1 1 1 1 1 1 1 1 3 1 1 1 3 1 6 1 1 1 1 2 1 1 1 1 1 7 1 1 1 1 1 1 1 2 1 1 2 2 1 1 1 1 1 1 1 1 2 1 1 1 1 2 1 2 1 4 1 5 7 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 4 1 1 1 1 1 1 2 3 1 1 2 1 1 1 3 1 1 1 1 1 2 1 1 1 3 1 1 1 1 1 1 1 1 1 1 1 1 3 1 1 1 1 1 1 1 1 1 1 4 1 1 2 2 1 1 2 1 1 1 1 2 2 1 1 1 1 2 1 1 2 1 1 1 1 1 2 1 2 1 1 2 3 1 1 1 1 1 2 1 1 2 5 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 2 2 1 1 1 1 1 1 1 1 1 1 6 1 1 1 2 1 2 1 2 4 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 2 1 1 1 1 4 2 1 1 1 1 1 1 5 1 1 1 1 1 1 1 1 2 3 1 1 1 1 2 1 1 1 4 1 1 1 4 1 1 3 1 1 1 1 1 1 1 2 3 1 3 1 1 1 3 2 1 1 2 1 1 1 1 1 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 2 1 1 1 3 1 2 1 2 1 1 1 1 1 1 1 1 1 1 1 2 1 2 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 3 1 1 2 1 1 1 1 1 2 1 1 1 1 1 1 1 1 2 1 1 1 1 6 1 1 2 1 2 1 1 1 1 1 1 4 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 2 1 1 1 2 3 1 1 1 1 1 11 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 2 1 1 1 2 1 1 1 1 1 1 1 1 2 9 1 2 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 3 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 1 1 1 1 2 1 2 1 2 1 1 1 1 1 1 1 1 1 1 2 1 1 8 2 1 1 1 1 2 1 1 7 4 1 1 4 1 1 1 1 1 1 1 1 1 1 1 6 1 1 1 2 2 1 7 1 1 2 1 1 5 2 1 1 1 2 1 1 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 2 1 1 1 1 1 1 3 1 2 1 1 1 1 1 1 1 1 5 1 1 1 3 1 1 1 1 1 1 3 1 1 4 1 4 1 1 1 1 1 1 1 1 1 4 3 1 1 1 1 3 1 2 1 1 1 2 1 1 1 1 1 1 2 6 1 1 1 1 1 1 1 1 2 1 1 1 1 2 1 1 1 2 1 1 3 2 1 1 1 1 1 1 2 2 1 1 9 1 1 1 1 1 1 1 1 1 1 1 2 1 1 2 1 2 1 4 5 1 1 1 1 1 1 1 1 1 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 5 2 1 2 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 2 3 1 1 1 1 1 2 1 1 1 1 1 1 1 2 1 2 1 6 2 1 1 1 2 1 1 2 7 1 1 1 2 1 1 1 1 1 1 1 1 1 2 1 4 1 1 1 1 1 1 1 1 1 1 2 1 3 3 1 1 2 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 2 3 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 4 1 1 1 1 1 1 1 1 1 1 1 1 3 2 1 1 1 1 1 1 2 1 1 1 2 1 1 1 1 1 1 1 2 1 1 2 4 3 1 1 1 1 2 1 1 1 1 4 1 1 1 1 1 1 1 1 1 2 1 3 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 2 1 3 1 1 1 2 1 1 1 1 1 2 1 1 2 1 2 2 1 3 1 1 1 2 1 1 1 3 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 3 1 1 1 1 3 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 5 2 1 1 1 1 1 1 2 1 1 7 1 1 1 2 2 1 7 2 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 3 1 1 1 1 1 1 2 1 1 1 1 1 1 2 1 1 1 1 1 2 1 1 2 1 1 1 1 2 1 1 1 1 4 1 1 1 1 1 1 1 1 2 1 1 1 1"

cube_flattended = list(map(int, inp.split(" ")))
print(naive_max_subspecial_cube(cube_flattended))
print(bucket_max_subspecial(cube_flattended))
print(math.pow(len(cube_flattended), 1))
cube_3d_inp, cube_size_inp = convert_to_3d_tensor(cube_flattended)

print("cube_size= ", cube_size_inp)
print(cube_3d_inp[0])
