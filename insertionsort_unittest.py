"""
Author: Armao Thao

Description:
    This is a unit test file for insertionsort.py.

"""

from test_utilities import compare_arr_sorted_equal, summarize_results
from time import clock
from insertionsort import insertionsort

GLOBAL_PRINT_DEBUG = False

if __name__ == "__main__":
    runtime = []
    results = []
    print "####################################################"
    print("Test case 1")
    data = [1, 5, 3, 6, 10, 9, 4]
    result = data[:]
    time1 = clock()
    insertionsort(result)
    time2 = clock()
    print "runtime: ", time2 - time1
    runtime.append(time2 - time1)
    output = compare_arr_sorted_equal(data, result)
    print(output)
    results.append(output)
    print "####################################################"
    print("Test case 2")
    data = [0, 999, 1000, 10, 100, 500, 300, 35, 598, 456, 985, 874]
    result = data[:]
    time1 = clock()
    insertionsort(result)
    time2 = clock()
    print "runtime: ", time2 - time1
    runtime.append(time2 - time1)
    output = compare_arr_sorted_equal(data, result)
    print(output)
    results.append(output)
    print "####################################################"
    print("Test case 3")
    data = [10000, 8000, 9000, 5000, 1000, 2000, 4500]
    result = data[:]
    time1 = clock()
    insertionsort(result)
    time2 = clock()
    print "runtime: ", time2 - time1
    runtime.append(time2 - time1)
    output = compare_arr_sorted_equal(data, result)
    print(output)
    results.append(output)
    print "####################################################"
    print("Test case 4")
    data = [1, 100, 5, 2, 50, 25, 0 , 100, 100000, 1001, 2004, 5223]
    result = data[:]
    time1 = clock()
    insertionsort(result)
    time2 = clock()
    print "runtime: ", time2 - time1
    runtime.append(time2 - time1)
    output = compare_arr_sorted_equal(data, result)
    print(output)
    results.append(output)
    print "####################################################"
    print("Test case 5")
    data = [500, 100, 5, 2, 50, 25, 2343, 432, 43234, 324, 7566]
    result = data[:]
    time1 = clock()
    insertionsort(result)
    time2 = clock()
    print "runtime: ", time2 - time1
    runtime.append(time2 - time1)
    output = compare_arr_sorted_equal(data, result)
    print(output)
    results.append(output)
    print "####################################################"
    print("Test case 6")
    data = [100, 5, 2, 50, 25, 987, 4564, 3554, 45, 657, 898]
    result = data[:]
    time1 = clock()
    insertionsort(result)
    time2 = clock()
    print "runtime: ", time2 - time1
    runtime.append(time2 - time1)
    output = compare_arr_sorted_equal(data, result)
    print(output)
    results.append(output)
    print "####################################################"
    print "Runtimes: ", runtime
    print "Average runtime: ", str(sum(runtime) / len(runtime))
    summarize_results(results)

