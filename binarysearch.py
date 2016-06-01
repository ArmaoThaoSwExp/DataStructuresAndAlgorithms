__author__ = 'Armao'

"""
Binary Search
"""


def binarysearch(arr, val, start, end):
    if start > end:
        return False
    mid = (start + end) / 2
    if val == arr[mid]:
        return True
    elif val >= arr[mid]:
        return binarysearch(arr, val=val, start=mid+1, end=end)
    else:
        return binarysearch(arr, val=val, start=start, end=mid-1)


if __name__ == '__main__':
    print("Binary Search")



