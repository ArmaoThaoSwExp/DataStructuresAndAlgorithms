__author__ = 'Armao'

"""
Linked list
"""

from test_utilities import compare_var, summarize_results


class Stack(object):
    def __init__(self):
        self._stack = []

    def pop(self):
        result = None
        if not self.is_empty():
            result = self._stack.pop()
        return result

    def push(self, value):
        self._stack.append(value)

    def peek(self):
        result = None
        if not self.is_empty():
            result = self._stack[-1]
        return result

    def is_empty(self):
        return True if len(self._stack) == 0 else False


if __name__ == '__main__':
    results = []
    print("")
    my_stack = Stack()
    print("Verify stack is empty")
    results.append(compare_var(my_stack.peek(), None, "=="))
    results.append(compare_var(my_stack.pop(), None, "=="))

    print("")
    val = 1
    print("Verify {0} is pushed into the stack".format(val))
    my_stack.push(val)
    results.append(compare_var(my_stack.peek(), val, "=="))

    print("")
    val = 2
    print("Verify {0} is pushed into the stack".format(val))
    my_stack.push(val)
    results.append(compare_var(my_stack.peek(), val, "=="))

    print("")
    val = 5
    print("Verify {0} is pushed into the stack".format(val))
    my_stack.push(val)
    results.append(compare_var(my_stack.peek(), val, "=="))

    print("")
    val = 5
    val2 = 2
    print("Verify {0} is popped off the stack".format(val))
    results.append(compare_var(my_stack.pop(), val, "=="))
    print("Verify {0} is now top of the stack".format(val2))
    results.append(compare_var(my_stack.peek(), val2, "=="))
    print("Verify the stack is not empty")
    results.append(compare_var(my_stack.is_empty(), False, "=="))

    print("")
    val = 2
    val2 = 1
    print("Verify {0} is popped off the stack".format(val))
    results.append(compare_var(my_stack.pop(), val, "=="))
    print("Verify {0} is now top of the stack".format(val2))
    results.append(compare_var(my_stack.peek(), val2, "=="))
    print("Verify the stack is not empty")
    results.append(compare_var(my_stack.is_empty(), False, "=="))

    print("")
    val = 1
    val2 = None
    print("Verify {0} is popped off the stack".format(val))
    results.append(compare_var(my_stack.pop(), val, "=="))
    print("Verify {0} is now top of the stack".format(val2))
    results.append(compare_var(my_stack.peek(), val2, "=="))
    print("Verify the stack is now empty")
    results.append(compare_var(my_stack.is_empty(), True, "=="))



    summarize_results(results)
