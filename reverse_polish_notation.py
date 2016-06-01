__author__ = 'Armao'

"""
Polish notation:
    ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5
    - * / 15 - 7 + 1 1 3 + 2 + 1 1
"""

from test_utilities import compare_var, summarize_results


POLISH_OPERATORS = ['+', '-', '*', '/', '//']


def isnum(val):
    result = False
    if isinstance(val, str):
        try:
            float(val)
            result = True
        except ValueError, valerr:
            pass  # result = True
        except Exception, exc:
            raise exc
    elif isinstance(val, int) or isinstance(val, float):
        result = True
    return result


def calc_buffer(buffer):
    while True:
        if len(buffer) >= 3 and isnum(buffer[-2]) and isnum(buffer[-3]):
            operator = buffer.pop()
            val2 = buffer.pop()
            val1 = buffer.pop()
            expr = " ".join([str(val1), str(operator), str(val2)])
            print "expr", expr
            buffer.append(eval(expr))
        else:
            break


def reversepolishnotation(inputlist):
    buffer = []
    for item in inputlist:
        if item in POLISH_OPERATORS:
            buffer.append(item)
            calc_buffer(buffer)
        else:
            if not isnum(item):
                print item
                raise ValueError("Non-operator values must be of type float or int: {0}".format(item))
            buffer.append(item)
    if len(buffer) == 1:
        return buffer[0]
    else:
        raise Exception("Invalid reverse polish notation; queue = {0}".format(buffer))


if __name__ == '__main__':
    results = []

    pol_arr = ["4", "1", "+", "2.5", "*"]
    print("\nReverse polish notation: " + str(pol_arr))
    results.append(compare_var(reversepolishnotation(pol_arr), 12.5, "=="))

    pol_arr = ["5", "80", "40.0", "/", "+"]
    print("\nReverse polish notation: " + str(pol_arr))
    results.append(compare_var(reversepolishnotation(pol_arr), 7, "=="))

    summarize_results(results)
