"""
Author: Armao Thao

Description:
    This file implements the quicksort algorithm.
    Complexity Analysis: O(n^2)
"""

from test_utilities import compare_arr_sorted_equal
from time import clock

GLOBAL_PRINT_DEBUG = False


def insertionsort(arr, print_debug=GLOBAL_PRINT_DEBUG):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                temp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = temp
            else:
                break

if __name__ == "__main__":
    print("Insertion Sort")