"""
Author: Armao Thao

Description:
    This file implements the quicksort algorithm.
    Complexity Analysis: O(nlogn) on average. Worst case: O(n^2)
"""

from test_utilities import compare_arr_sorted_equal
from time import clock

#
# def quicksort(arr, left, right, print_debug=True):
#     pivot = arr[(left + right) / 2]
#     i = left
#     j = right
#     while i <= j:
#         # while arr[i] < arr[pivot]:
#         #     i += 1
#         # while arr[j] > arr[pivot]:
#         #     j -= 1
#
#         while arr[i] < pivot:
#             i += 1
#         while arr[j] > pivot:
#             j -= 1
#         if i <= j:
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
#             i += 1
#             j -= 1
#
#     if left < j:
#         quicksort(arr, left, j)
#     if right > i:
#         quicksort(arr, i, right)



def quicksort(arr, left, right, print_debug=True):
    pivot = arr[(left + right) / 2]
    i = left
    j = right
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
    if j > left:
        quicksort(arr, left=left, right=j, print_debug=print_debug)
    if i < right:
        quicksort(arr, left=i, right=right, print_debug=print_debug)


if __name__ == "__main__":
    print("Quick Sort")
