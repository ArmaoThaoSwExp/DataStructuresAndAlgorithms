"""
Author: Armao Thao

Description:
    This file implements the quicksort algorithm.
    Complexity Analysis: O(n^2)
"""

from test_utilities import compare_arr_sorted_equal
from time import clock

GLOBAL_PRINT_DEBUG = False


def selectionsort(arr):
    for i in range(len(arr)):
        smallest_ind = i
        for j in range(i, len(arr)):
            if arr[smallest_ind] > arr[j]:
                smallest_ind = j
        if smallest_ind != i:
            temp = arr[i]
            arr[i] = arr[smallest_ind]
            arr[smallest_ind] = temp


if __name__ == "__main__":
    print("Selection Sort")