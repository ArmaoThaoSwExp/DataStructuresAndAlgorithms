__author__ = 'Armao'

"""
Fibonacci examples
"""
from test_utilities import compare_var, summarize_results


class FibExceptionZero(Exception):
    pass

def fib_recursive(n):
    if n == 0:
        raise FibExceptionZero("n must be greater than 0 for the Fibonacci sequence")
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iterative(n):
    if n == 0:
        raise FibExceptionZero("n must be greater than 0 for the Fibonacci sequence")
    elif n == 1:
        return 0
    # Let's start at n = 2, which has n - 1 as 1, and n - 2 as 0
    result = 1
    prior = 0
    prev = 1
    for i in range(3, n + 1):
        result = prev + prior
        prior = prev
        prev = result
    return result


if __name__ == '__main__':
    print("Fibionacci examples")

    results = []
    print("")
    print "####################################################"
    print("Test case 1: except on 0")
    try:
        fib_recursive(0)
        compare_var(True, False, "==")  # Log failure since fibonacci sequence should not have allowed a 0 passed in
    except FibExceptionZero, err:
        print("FibExceptionZero raised: good")
        compare_var(True, True, "==")

    try:
        fib_iterative(0)
        compare_var(True, False, "==")  # Log failure since fibonacci sequence should not have allowed a 0 passed in
    except FibExceptionZero, err:
        print("FibExceptionZero raised: good")
        compare_var(True, True, "==")

    print("")
    print "####################################################"
    print("Test case 2: n = 1")
    results.append(compare_var(fib_recursive(1), 0, "=="))
    results.append(compare_var(fib_iterative(1), 0, "=="))

    print("")
    print "####################################################"
    print("Test case 3: n = 2")
    results.append(compare_var(fib_recursive(2), 1, "=="))
    results.append(compare_var(fib_iterative(2), 1, "=="))

    print("")
    print "####################################################"
    print("Test case 4: n = 3")
    results.append(compare_var(fib_recursive(3), 1, "=="))
    results.append(compare_var(fib_iterative(3), 1, "=="))

    print("")
    print "####################################################"
    print("Test case 5: n = 4")
    results.append(compare_var(fib_recursive(4), 2, "=="))
    results.append(compare_var(fib_iterative(4), 2, "=="))

    print("")
    print "####################################################"
    print("Test case 6: n = 5")
    results.append(compare_var(fib_recursive(5), 3, "=="))
    results.append(compare_var(fib_iterative(5), 3, "=="))

    print("")
    print "####################################################"
    print("Test case 7: n = 20")
    results.append(compare_var(fib_recursive(20), 4181, "=="))
    results.append(compare_var(fib_iterative(20), 4181, "=="))

    summarize_results(results)

