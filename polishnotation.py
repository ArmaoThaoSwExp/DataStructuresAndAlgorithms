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
        if len(buffer) >= 2 and isnum(buffer[-1]) and isnum(buffer[-2]) and \
           (buffer[-3] in POLISH_OPERATORS):
            val2 = buffer.pop()
            val1 = buffer.pop()
            operator = buffer.pop()
            expr = " ".join([str(val1), str(operator), str(val2)])
            print "expr", expr
            buffer.append(eval(expr))
        else:
            break


def polishnotation(inputlist):
    buffer = []
    for item in inputlist:
        if item in POLISH_OPERATORS:
            buffer.append(item)
        else:
            isoperand = isnum(item)
            if not isoperand:
                print item
                raise ValueError("Non-operator values must be of type float or int")
            else:
                buffer.append(item)
                calc_buffer(buffer=buffer)
    if len(buffer) == 1:
        return buffer[0]
    else:
        raise Exception("Invalid polish notation; queue = {0}".format(buffer))


if __name__ == '__main__':
    results = []
    data = ['-', '*', '//', '15', '-', '7', '+', '1', '1', '3', '+', '2', '+', '1', '1']
    print polishnotation(data)

    summarize_results(results)
