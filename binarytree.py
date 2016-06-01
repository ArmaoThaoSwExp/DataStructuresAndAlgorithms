"""
Author: Armao Thao

Description:
    Binary tree implementation
"""

GLOBAL_PRINT_DEBUG = False


class BNode(object):
    def __init__(self, value, left=None, right=None):
        assert isinstance(left, BNode) or left is None, "left must be of type BNode or None"
        assert isinstance(right, BNode) or right is None, "right must be of type BNode or None"
        self.value = value
        self.left = left
        self.right = right


class BinaryTreeEnum(object):
    PrintInOrder, PrintPreOrder, PrintPostOrder = range(3)


class BinaryTree(object):
    def __init__(self):
        self._root = None

    def insert(self, value):
        if self._root is None:
            self._root = BNode(value=value, left=None, right=None)
        else:
            self._insert(value=value, node=self._root)

    def _insert(self, value, node):
        if node.value == value:
            return
        elif value < node.value:
            if node.left is None:
                node.left = BNode(value=value, left=None, right=None)
            else:
                self._insert(value, node=node.left)
        else:
            if node.right is None:
                node.right = BNode(value=value, left=None, right=None)
            else:
                self._insert(value, node=node.right)

    def min(self):
        return self._min(self._root)

    def _min(self, node):
        if node.left is None:
            return node
        return self._min(node.left)

    def remove(self, value):
        if self._root is None:
            return
        elif self._root.value == value:
            if self._root.left is None:
                # If left is None, just set it equal to right.
                # Regardless of whether right is None or right is actually a valid node,
                # setting the root to right would link the additional nodes or set it to None if applicable.
                self._root = self._root.right
            elif self._root.right is None:
                self._root = self._root.left
            else:
                # If both left and right are not empty,
                # set the current node value equal to the minimum value on the right side of the tree,
                # and then delete the minimum right node.
                self._root.value = self._min(self._root.right).value
                self._remove(self._root, self._root.value)
        else:
            self._root = self._remove(self._root, value)

    def _remove(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._remove(node.left, value)
            return node
        elif value > node.value:
            node.right = self._remove(node.right, value)
            return node
        else:
            if node.left is None:
                # If left is None, just set it equal to right.
                # Regardless of whether right is None or right is actually a valid node,
                # setting the root to right would link the additional nodes or set it to None if applicable.
                node = node.right
                return node
            elif node.right is None:
                node = node.left
                return node
            else:
                # If both left and right are not empty,
                # set the current node value equal to the minimum value on the right side of the tree,
                # and then delete the minimum right node.
                node.value = self._min(self._root.right).value
                node.right = self._remove(node.right, node.value)
                return node

    def search(self, value):
        if self._root is None:
            return False
        if value == self._root.value:
            return True
        else:
            return self._search(self._root, value)

    def _search(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def is_balanced(self):
        if self._root is None:
            return True
        if abs(self._max_depth(self._root.left) - self._max_depth(self._root.right)) <= 1:
            return True
        else:
            return False

    def max_depth(self):
        return self._max_depth(self._root)

    def _max_depth(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self._max_depth(node.left), self._max_depth(node.right))

    def print_tree(self, order=BinaryTreeEnum.PrintInOrder, returnresult=False):
        result = [] if returnresult else None
        self._print_tree(self._root, order=order, returnresult=result)
        return result if returnresult else None

    def _print_tree(self, node, order=BinaryTreeEnum.PrintInOrder, returnresult=False):
        assert isinstance(returnresult, list) or isinstance(returnresult, bool) or isinstance(returnresult, None), \
            "returnresult must be one of the following types: list, None or False" \
            "\nInstead, received type {0}".format(type(returnresult))
        if node is None:
            return
        if order == BinaryTreeEnum.PrintInOrder:
            self._print_tree(node.left, order=order, returnresult=returnresult)
            print node.value
            if isinstance(returnresult, list):
                returnresult.append(node.value)
            self._print_tree(node.right, order=order, returnresult=returnresult)
        elif order == BinaryTreeEnum.PrintPreOrder:
            print node.value
            if isinstance(returnresult, list):
                returnresult.append(node.value)
            self._print_tree(node.left, order=order, returnresult=returnresult)
            self._print_tree(node.right, order=order, returnresult=returnresult)
        else:
            self._print_tree(node.left, order=order, returnresult=returnresult)
            self._print_tree(node.right, order=order, returnresult=returnresult)
            print node.value
            if isinstance(returnresult, list):
                returnresult.append(node.value)


if __name__ == "__main__":
    print("Binary Tree")
