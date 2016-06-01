"""
Author: Armao Thao

Description:
    This file implements the quicksort algorithm.
    Complexity Analysis: O(n^2)
"""

from test_utilities import compare_arr_sorted_equal, summarize_results
from time import clock
from selectionsort import selectionsort

GLOBAL_PRINT_DEBUG = False

if __name__ == "__main__":
    runtime = []
    results = []
    print "####################################################"
    data = [1, 100, 5, 2, 50, 25]
    print("Data: " + str(data))
    result = data[:]
    time1 = clock()
    selectionsort(result)
    time2 = clock()
    print "runtime: ", time2 - time1
    runtime.append(time2 - time1)
    output = compare_arr_sorted_equal(data, result)
    results.append(output)
    print "####################################################"
    data = [1, 100, 1000, 55, 500, 504, 23, 4, 3, 23, 45]
    print("Data: " + str(data))
    result = data[:]
    time1 = clock()
    selectionsort(result)
    time2 = clock()
    print "runtime: ", time2 - time1
    runtime.append(time2 - time1)
    output = compare_arr_sorted_equal(data, result)
    results.append(output)
    print "####################################################"
    data = [1, 100, 5, 2, 50, 25, 200, 4, 299, 433, 1]
    print("Data: " + str(data))
    result = data[:]
    time1 = clock()
    selectionsort(result)
    time2 = clock()
    print "runtime: ", time2 - time1
    runtime.append(time2 - time1)
    output = compare_arr_sorted_equal(data, result)
    results.append(output)
    print "####################################################"
    data = [1, 100, 5, 2, 50, 25, 0 , 100, 100000, 1001, 2004, 5223]
    print("Data: " + str(data))
    result = data[:]
    time1 = clock()
    selectionsort(result)
    time2 = clock()
    print "runtime: ", time2 - time1
    runtime.append(time2 - time1)
    output = compare_arr_sorted_equal(data, result)
    results.append(output)
    print "####################################################"
    data = [1, 100, 5, 2, 50, 25, 2343, 432, 43234, 324, 7566]
    print("Data: " + str(data))
    result = data[:]
    time1 = clock()
    selectionsort(result)
    time2 = clock()
    print "runtime: ", time2 - time1
    runtime.append(time2 - time1)
    output = compare_arr_sorted_equal(data, result)
    results.append(output)
    print "####################################################"
    data = [1, 100, 5, 2, 50, 25, 987, 4564, 3554, 45, 657, 898]
    print("Data: " + str(data))
    result = data[:]
    time1 = clock()
    selectionsort(result)
    time2 = clock()
    print "runtime: ", time2 - time1
    runtime.append(time2 - time1)
    output = compare_arr_sorted_equal(data, result)
    results.append(output)
    print "####################################################"
    print "Runtimes: ", runtime
    print "Average runtime: ", str(sum(runtime) / len(runtime))
    summarize_results(results)


