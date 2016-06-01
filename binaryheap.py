"""
Author: Armao Thao

Description:
    Binary Heap: a simple example
"""

from test_utilities import compare_var, compare_arr_similar

GLOBAL_PRINT_DEBUG = False


class BinaryMinHeap(object):
    def __init__(self, array=None):
        """
        left index in a heap array: left(i) = 2 * i + 1
        right index in a heap array: right(i) = 2 * i + 2
        parent index: parent(i) = (i - 1) / 2

        :param array:
        :return:
        """
        assert isinstance(array, list) or array is None, \
            "array must be of type array of None, but received {0}".format(type(array))
        self._bheap = array if isinstance(array, list) else []

    def remove_min(self):
        result = None
        if self.is_empty() is False:
            # Set the minimum value equal to the last element in the heap.
            # Then using the new minimum value, sift down the heap.
            result = self._bheap[0]
            self._bheap[0] = self._bheap[-1]
            del self._bheap[-1]
            self._siftdown(0)
        return result

    def peek_min(self):
        if len(self._bheap) > 0:
            return self._bheap[0]
        else:
            return None

    def is_empty(self):
        return True if len(self._bheap) is 0 else False

    def insert(self, value):
        self._bheap.append(value)
        if len(self._bheap) > 1:
            self._siftup(len(self._bheap) - 1)

    def _get_left_child_ind(self, nodeind):
        return (2 * nodeind) + 1

    def _get_right_child_ind(self, nodeind):
        return (2 * nodeind) + 2

    def _get_parent_index(self, nodeind):
        return int((nodeind - 1) / 2)

    def peek_array(self):
        return self._bheap[:]

    def _siftdown(self, nodeindex):
        left_child_ind = self._get_left_child_ind(nodeindex)
        right_child_ind = self._get_right_child_ind(nodeindex)
        hsize = len(self._bheap)
        siftdown = False
        siftind = 0
        if left_child_ind < hsize:
            if right_child_ind < hsize:
                min_child = left_child_ind if self._bheap[left_child_ind] < self._bheap[right_child_ind] \
                    else right_child_ind
            else:
                min_child = left_child_ind
            if self._bheap[nodeindex] > self._bheap[min_child]:
                siftdown = True
                siftind = min_child
        else:
            if right_child_ind < hsize:
                if self._bheap[nodeindex] > self._bheap[right_child_ind]:
                    siftdown = True
                    siftind = right_child_ind

        if siftdown:
            temp = self._bheap[nodeindex]
            self._bheap[nodeindex] = self._bheap[siftind]
            self._bheap[siftind] = temp
            self._siftdown(siftind)

    def _siftup(self, nodeindex):
        parentind = self._get_parent_index(nodeindex)
        if self._bheap[nodeindex] < self._bheap[parentind]:
            temp = self._bheap[parentind]
            self._bheap[parentind] = self._bheap[nodeindex]
            self._bheap[nodeindex] = temp
            if parentind != 0:
                self._siftup(parentind)



if __name__ == "__main__":
    runtime = []
    print "####################################################"
    bheap = BinaryHeap()
    compare_var(bheap.is_empty(), True, "==")
    compare_var(bheap.peek_min(), None, "==")
    compare_var(bheap.remove_min(), None, "==")
    compare_var(bheap.peek_array(), [], "==")

    val = 5
    print("\nAdd one value to the heap: {0}".format(val))
    bheap.insert(val)
    compare_var(bheap.is_empty(), False, "==")
    compare_var(bheap.peek_min(), val, "==")
    compare_var(bheap.peek_array(), [5], "==")

    print("\nRemove min value to the heap: {0}".format(val))
    compare_var(bheap.remove_min(), val, "==")
    compare_var(bheap.is_empty(), True, "==")
    compare_var(bheap.peek_min(), None, "==")
    compare_var(bheap.peek_array(), [], "==")

    print("\nInsert multiple values into binary heap")
    vals = [1, 2, 3, 4, 6, 8, 10, 20, 15, 13, 11, 10]
    barray = []
    for i in range(len(vals)):
        val = vals[i]
        bheap.insert(val)
        barray = bheap.peek_array()
        compare_var(bheap.peek_min(), min(vals), "==")
        compare_arr_similar(barray, vals[:i + 1])

    print("\nRemove each minimum from binary heap")
    vals = [1, 2, 3, 4, 6, 8, 10, 20, 15, 13, 11, 10]
    barray = []
    temp_vals = vals[:]
    temp_vals.sort()
    for i in range(len(vals)):
        compare_var(bheap.remove_min(), temp_vals[0], "==")
        print bheap.peek_array()
        del temp_vals[0]
    print "####################################################"
    vals = [1, 3, 6, 5, 9, 8]
    print("\nCreate binary heap with the following values: {}".format(vals))
    bheap = BinaryHeap(vals)
    compare_var(bheap.peek_array(), vals, "==")
    val = -2

    print("\nInsert {} into binary heap".format(val))
    bheap.insert(val)
    compare_var(bheap.peek_array(), [val, 3, 1, 5, 9, 8, 6], "==")

    print("\nRemove minimum from binary heap")
    bheap.remove_min()
    compare_var(bheap.peek_array(), [1, 3, 6, 5, 9, 8], "==")
    print "####################################################"
    vals = [6, 7, 12, 10, 15, 17]
    print("\nCreate binary heap with the following values: {}".format(vals))
    bheap = BinaryHeap(vals)
    compare_var(bheap.peek_array(), vals, "==")
    val = 5

    print("\nInsert {} into binary heap".format(val))
    bheap.insert(val)
    compare_var(bheap.peek_array(), [val, 7, 6, 10, 15, 17, 12], "==")

