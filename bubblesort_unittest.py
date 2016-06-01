"""
Author: Armao Thao

Description:
    This file is a simple bubble sort test.
"""
from bubblesort import bubblesort
from test_utilities import compare_var, compare_arr_similar, compare_arr_sorted_equal, summarize_results
from time import clock


runtime = []
results = []
print "####################################################"
data = [1, 100, 5, 2, 50, 25]
result = data[:]
time1 = clock()
bubblesort(result)
time2 = clock()
print "runtime: ", time2 - time1
runtime.append(time2 - time1)
output = compare_arr_sorted_equal(data, result)
results.append(output)
print "####################################################"
data = [1, 100, 1000, 55, 500, 504, 23, 4, 3, 23, 45]
result = data[:]
time1 = clock()
bubblesort(result)
time2 = clock()
print "runtime: ", time2 - time1
runtime.append(time2 - time1)
output = compare_arr_sorted_equal(data, result)
results.append(output)
print "####################################################"
data = [1, 100, 5, 2, 50, 25, 200, 4, 299, 433, 1]
result = data[:]
time1 = clock()
bubblesort(result)
time2 = clock()
print "runtime: ", time2 - time1
runtime.append(time2 - time1)
output = compare_arr_sorted_equal(data, result)
results.append(output)
print "####################################################"
data = [1, 100, 5, 2, 50, 25, 0 , 100, 100000, 1001, 2004, 5223]
result = data[:]
time1 = clock()
bubblesort(result)
time2 = clock()
print "runtime: ", time2 - time1
runtime.append(time2 - time1)
output = compare_arr_sorted_equal(data, result)
results.append(output)
print "####################################################"
data = [1, 100, 5, 2, 50, 25, 2343, 432, 43234, 324, 7566]
result = data[:]
time1 = clock()
bubblesort(result)
time2 = clock()
print "runtime: ", time2 - time1
runtime.append(time2 - time1)
output = compare_arr_sorted_equal(data, result)
results.append(output)
print "####################################################"
data = [1, 100, 5, 2, 50, 25, 987, 4564, 3554, 45, 657, 898]
result = data[:]
time1 = clock()
bubblesort(result)
time2 = clock()
print "runtime: ", time2 - time1
runtime.append(time2 - time1)
output = compare_arr_sorted_equal(data, result)
results.append(output)
print "####################################################"
print "Runtimes: ", runtime
print "Average runtime: ", str(sum(runtime) / len(runtime))
summarize_results(results)