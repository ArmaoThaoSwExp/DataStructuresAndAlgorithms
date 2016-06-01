__author__ = 'Armao'

"""
Queue
"""

from test_utilities import compare_var, summarize_results


class Queue(object):
    def __init__(self):
        self._queue = []

    def enqueue(self, val):
        self._queue.append(val)

    def dequeue(self):
        assert self.size() > 0, "Cannot dequeue because queue is empty!"
        if not self.is_empty():
            return self._queue.pop(0)

    def peek(self):
        if not self.is_empty():
            return self._queue[0]

    def size(self):
        return len(self._queue)

    def is_empty(self):
        return True if not len(self._queue) else False


if __name__ == '__main__':
    print("Queue Class")

