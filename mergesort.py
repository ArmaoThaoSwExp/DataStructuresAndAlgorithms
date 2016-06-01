"""
Author: Armao Thao

Description:
    Merge Sort: a simple merge sort algorithm
    Complexity Analysis: O(nlogn) on average.
"""

from test_utilities import compare_arr_sorted_equal
from time import clock


def mergesort(arr, start, end, print_debug=False):
    if start == end:
        return [arr[start]]

    mid = (start + end) / 2
    first_half = mergesort(arr, start, mid)
    second_half = mergesort(arr, mid + 1, end)
    result = []
    i = 0
    j = 0
    while i < len(first_half) and j < len(second_half):
        if first_half[i] < second_half[j]:
            result.append(first_half[i])
            i += 1
        else:
            result.append(second_half[j])
            j += 1

    while i < len(first_half):
        result.append(first_half[i])
        i += 1
    while j < len(second_half):
        result.append(second_half[j])
        j += 1

    return result


if __name__ == "__main__":
    print("Merge Sort")