__author__ = 'Armao'

"""
Linked list
"""

from test_utilities import compare_var, summarize_results


class NotLLNodeException(Exception):
    pass


class LLNode(object):
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


def insert(head, value):
    if head is None:
        head = LLNode(value, prev=None, next=None)
    else:
        head.next = insert(head.next, value=value)

    return head


def display(head):
    if head is not None:
        assert isinstance(head, LLNode), "head must be of type LLNode"
        print head.value
        display(head.next)


def search(head, value):
    if head is None:
        return False
    assert isinstance(head, LLNode), "head must be of type LLNode"
    if head.value == value:
        return True
    return search(head.next, value=value)


def delete(head, value):
    if head is None:
        return None
    assert isinstance(head, LLNode), "head must be of type LLNode"
    if head.value == value:
        return head.next
    head.next = delete(head.next, value=value)
    return head


if __name__ == '__main__':
    results = []
    print("")
    head = None
    val = 10
    head = insert(head, val)
    display(head)
    print("Verify {0} was inserted successfully into the linked list".format(val))
    results.append(compare_var(True, search(head, val), "=="))

    print("")
    val = 0
    head = insert(head, val)
    display(head)
    print("Verify {0} was inserted successfully into the linked list".format(val))
    results.append(compare_var(True, search(head, val), "=="))

    print("")
    val = 55
    head = insert(head, val)
    display(head)
    print("Verify {0} was inserted successfully into the linked list".format(val))
    results.append(compare_var(True, search(head, val), "=="))

    print("")
    val = 100
    head = insert(head, val)
    display(head)
    print("Verify {0} was inserted successfully into the linked list".format(val))
    results.append(compare_var(True, search(head, val), "=="))

    print("")
    print("Verify that passing an object not of type LLNode will throw an assertion")
    try:
        result = search(object, 0)
        results.append(compare_var(False, True, "=="))  # If the search algorithm didn't throw an exception, register a failure
    except AssertionError, exc:
        print exc.message
        (compare_var("'" + exc.message + "'", "'head must be of type LLNode'", "=="))
    except Exception, exc:
        raise exc

    print("")
    val = 100
    print("Verify {0} was delete successfully from the linked list".format(val))
    head = delete(head, value=val)
    display(head)
    results.append(compare_var(False, search(head, val), "=="))

    print("")
    val = 100
    print("Verify {0} does not exist so deletion was not possible".format(val))
    head = delete(head, value=val)
    display(head)
    results.append(compare_var(False, search(head, val), "=="))

    print("")
    val = 55
    print("Verify {0} was delete successfully from the linked list".format(val))
    head = delete(head, value=val)
    display(head)
    results.append(compare_var(False, search(head, val), "=="))

    print("")
    val = 0
    print("Verify {0} was delete successfully from the linked list".format(val))
    head = delete(head, value=val)
    display(head)
    results.append(compare_var(False, search(head, val), "=="))

    print("")
    val = 10
    print("Verify {0} was delete successfully from the linked list".format(val))
    head = delete(head, value=val)
    display(head)
    results.append(compare_var(False, search(head, val), "=="))

    print("")
    val = 0
    print("Verify {0} does not exist so deletion was not possible".format(val))
    head = delete(head, value=val)
    display(head)
    results.append(compare_var(False, search(head, val), "=="))

    print("")
    val = 35
    print("Verify {0} does not exist so deletion was not possible".format(val))
    head = delete(head, value=val)
    display(head)
    results.append(compare_var(False, search(head, val), "=="))

    summarize_results(results)