"""
Author: Armao Thao

Description:
    This file is a simple bubble sort example.
"""

def bubblesort(arr):
    swap = True
    while swap:
        swap = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swap = True


if __name__ == "__main__":
    print("Bubble Sort")

