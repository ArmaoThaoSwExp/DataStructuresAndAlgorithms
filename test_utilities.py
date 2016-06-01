"""
Author: Armao Thao

Description:
    This file implements test utilities.
"""


def compare_var(var1, var2, operator):
    result = "***PASSED***"
    eval_str = "{var1} {operator} {var2}".format(var1=var1, var2=var2, operator=operator)
    print("Evaluate: " + eval_str)
    if not eval(eval_str):
        result = "***FAILED***"
    print(result)
    return result


def compare_arr_similar(arr_1, arr_2):
    result = "***PASSED***"
    print "Array 1: ", arr_1
    print "Array 2: ", arr_2
    print "Array 1 length: ", len(arr_1)
    print "Array 2 length: ", len(arr_2)
    if len(arr_1) != len(arr_2):
        result = "***FAILED***"
    else:
        for item in arr_1:
            if item not in arr_2:
                result = "***FAILED***"
                break
    print(result)
    return result


def compare_arr_sorted_equal(arr_1, arr_2):
    result = "***PASSED***"
    print()
    arr_1.sort()
    print("Comparing Array 1 Sorted {0} == Array 2 {1}".format(arr_1, arr_2))
    # print("Array 1 Sorted: {}".format(arr_1))
    # print "Array 2: ", arr_2
    if arr_1 != arr_2:
        result = "***FAILED***"
    print(result)
    return result


def summarize_results(results):
    assert isinstance(results, list), "results has to be a list of strings for 'PASSED' or 'FAILED'"
    failed_cnt = results.count("***FAILED***")
    result_str = "\n\nTOTAL TEST PASSED: {}".format(len(results) - failed_cnt)
    result_str += "\nTOTAL TEST FAILED: {}".format(failed_cnt)
    result_str += "\nTOTAL TESTS: {}".format(len(results))
    result_str += "\n\nOVERALL RESULTS: "
    if failed_cnt is not 0:
        result_str += "FAILED"
    else:
        result_str += "PASSED"
    print(result_str)
