"""
Author: Armao Thao

Description:
    Binary Heap: a simple example test example
"""

from test_utilities import compare_var, compare_arr_similar, summarize_results
from binaryheap import BinaryMinHeap

GLOBAL_PRINT_DEBUG = False


if __name__ == "__main__":
    runtime = []
    results = []
    print "####################################################"
    print("Test Case 1")
    bheap = BinaryMinHeap()
    results.append(compare_var(bheap.is_empty(), True, "=="))
    results.append(compare_var(bheap.peek_min(), None, "=="))
    results.append(compare_var(bheap.remove_min(), None, "=="))
    results.append(compare_var(bheap.peek_array(), [], "=="))

    print "####################################################"
    print("Test Case 2")
    val = 5
    print("\nAdd one value to the heap: {0}".format(val))
    bheap.insert(val)
    results.append(compare_var(bheap.is_empty(), False, "=="))
    results.append(compare_var(bheap.peek_min(), val, "=="))
    results.append(compare_var(bheap.peek_array(), [5], "=="))

    print "####################################################"
    print("Test Case 3")
    print("\nRemove min value to the heap: {0}".format(val))
    results.append(compare_var(bheap.remove_min(), val, "=="))
    results.append(compare_var(bheap.is_empty(), True, "=="))
    results.append(compare_var(bheap.peek_min(), None, "=="))
    results.append(compare_var(bheap.peek_array(), [], "=="))

    print "####################################################"
    print("Test Case 4")
    print("\nInsert multiple values into binary heap")
    vals = [1, 2, 3, 4, 6, 8, 10, 20, 15, 13, 11, 10]
    barray = []
    for i in range(len(vals)):
        val = vals[i]
        bheap.insert(val)
        barray = bheap.peek_array()
        results.append(compare_var(bheap.peek_min(), min(vals), "=="))
        compare_arr_similar(barray, vals[:i + 1])

    print "####################################################"
    print("Test Case 5")
    print("\nRemove each minimum from binary heap")
    vals = [1, 2, 3, 4, 6, 8, 10, 20, 15, 13, 11, 10]
    barray = []
    temp_vals = vals[:]
    temp_vals.sort()
    print("Binary heap: {0}".format(bheap.peek_array()))
    print("vals array: {0}".format(vals))
    for i in range(len(vals)):
        results.append(compare_var(bheap.remove_min(), temp_vals[0], "=="))
        del temp_vals[0]
        print("")
        print("Binary heap: {0}".format(bheap.peek_array()))
        print("Binary heap (sorted): {0}".format(sorted(bheap.peek_array())))
        print("temp vals array: {0}".format(temp_vals))

    print "####################################################"
    print("Test Case 6")
    vals = [1, 3, 6, 5, 9, 8]
    print("\nCreate binary heap with the following values: {}".format(vals))
    bheap = BinaryMinHeap(vals)
    results.append(compare_var(bheap.peek_array(), vals, "=="))
    val = -2

    print("\nInsert {} into binary heap".format(val))
    bheap.insert(val)
    results.append(compare_var(bheap.peek_array(), [val, 3, 1, 5, 9, 8, 6], "=="))

    print("\nRemove minimum from binary heap")
    bheap.remove_min()
    results.append(compare_var(bheap.peek_array(), [1, 3, 6, 5, 9, 8], "=="))

    print "####################################################"
    print("Test Case 7")
    vals = [6, 7, 12, 10, 15, 17]
    print("\nCreate binary heap with the following values: {}".format(vals))
    bheap = BinaryMinHeap(vals)
    results.append(compare_var(bheap.peek_array(), vals, "=="))
    val = 5

    print("\nInsert {} into binary heap".format(val))
    bheap.insert(val)
    results.append(compare_var(bheap.peek_array(), [val, 7, 6, 10, 15, 17, 12], "=="))

    print "####################################################"
    summarize_results(results)
