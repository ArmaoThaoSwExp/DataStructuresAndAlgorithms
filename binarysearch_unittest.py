"""
Author: Armao Thao

Description:
    Merge Sort: a simple binary search example.
    Complexity Analysis: O(logn) on average
"""
from binarysearch import binarysearch
from test_utilities import compare_var, summarize_results

if __name__ == "__main__":
    runtime = []
    results = []
    print "####################################################"
    data = [1, 2, 5, 5, 23, 100, 300, 555]
    exp_result = binarysearch(data, 5, 0, len(data) - 1)
    output = compare_var(exp_result, True, "==")
    results.append(output)
    print "####################################################"
    data = [1, 2, 5, 5, 23, 100, 300, 555]
    exp_result = binarysearch(data, 10, 0, len(data) - 1)
    output = compare_var(exp_result, False, "==")
    results.append(output)
    print "####################################################"
    data = [1, 2, 5, 5, 23, 100, 300, 555]
    exp_result = binarysearch(data, 555, 0, len(data) - 1)
    output = compare_var(exp_result, True, "==")
    results.append(output)
    print "####################################################"
    data = [1, 2, 5, 5, 23, 100, 300, 555]
    exp_result = binarysearch(data, 556, 0, len(data) - 1)
    output = compare_var(exp_result, False, "==")
    results.append(output)
    print "####################################################"
    data = [1, 2, 5, 5, 23, 100, 300, 555]
    exp_result = binarysearch(data, 101, 0, len(data) - 1)
    output = compare_var(exp_result, False, "==")
    results.append(output)
    print "####################################################"
    data = [1, 2, 5, 5, 23, 100, 300, 555]
    exp_result = binarysearch(data, 3, 0, len(data) - 1)
    output = compare_var(exp_result, False, "==")
    results.append(output)
    print "####################################################"
    data = [1, 2, 5, 5, 23, 100, 300, 555]
    exp_result = binarysearch(data, 2, 0, len(data) - 1)
    output = compare_var(exp_result, True, "==")
    results.append(output)
    print "####################################################"
    data = [1, 2, 5, 5, 23, 100, 300, 555, 555, 555, 5556]
    exp_result = binarysearch(data, 555, 0, len(data) - 1)
    output = compare_var(exp_result, True, "==")
    results.append(output)

    summarize_results(results)
