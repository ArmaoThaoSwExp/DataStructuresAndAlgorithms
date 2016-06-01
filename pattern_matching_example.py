__author__ = 'Armao'

"""
Give a sorted array.  The array has been rotated by a certain index.  Find the minimum element.
"""


def min_val_rotated_arr(arr):
    start = 0
    end = len(arr) - 1
    result = False

    if len(arr) == 0:
        return False
    if len(arr) == 1:
        return arr[0]

    while True:
        if start > end:
            result = False
            break
        mid = (start + end) / 2
        if end == start + 1:
            if arr[start] < arr[end]:
                result = arr[start]
            else:
                result = arr[end]
            break

        if arr[start] > arr[mid]:
            end = mid
        else:
            start = mid

    return result


# def binary_search(arr, target):
#     start = 0
#     end = len(arr) - 1
#     result = False
#     while True:
#         if start > end:
#             break
#
#         mid = (start + end) / 2
#         if target == arr[mid]:
#             result = True
#             break
#         elif target > arr[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return result


# def binary_search(arr, val):
#     start = 0
#     end = len(arr) - 1
#     while True:
#         if start > end:
#             return False
#         mid = int((start + end) / 2)
#         if val == arr[mid]:
#             return True
#         elif val > arr[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1


if __name__ == '__main__':
    print("Pattern Matching Example")

    my_arr_sorted = [i for i in range(8, 100) if not i % 8]
    print('\nmy_arr_sorted: {0}'.format(my_arr_sorted))

    my_arr_rotated = my_arr_sorted[9:] + my_arr_sorted[0:9]
    print('\nmy_arr_rotated: {my_arr_rotated}'.format(my_arr_rotated=my_arr_rotated))

    print('\nminimum element value: {0}'.format(min_val_rotated_arr(my_arr_rotated)))
    print('Expected minimum element value: {0}'.format(min(my_arr_rotated)))

    print('\nminimum element value: {0}'.format(min_val_rotated_arr([])))
    print('Expected minimum element value: {0}'.format(False))

    print('\nminimum element value: {0}'.format(min_val_rotated_arr([109, ])))
    print('Expected minimum element value: {0}'.format(109))

    # for i in range(0, 17):
    #     print('i = {0}, binary_search results: {1}'.format(i, binary_search(my_arr_sorted, i)))
