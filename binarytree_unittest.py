"""
Author: Armao Thao

Description:
    Binary tree implementation
"""
from binarytree import BinaryTree, BinaryTreeEnum
import unittest

GLOBAL_PRINT_DEBUG = False


class UnitTestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.btree = BinaryTree()

    def tearDown(self):
        pass

    def test_insert_one(self):
        self.btree.insert(1)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [1])

    def test_insert_one_duplicate(self):
        self.btree.insert(1)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [1])

        self.btree.insert(1)  # Insert duplicate
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        # Results should show only 1 entry in the btree since the insert was duplicate
        self.assertEqual(result, [1])

    def test_insert_left(self):
        self.btree.insert(2)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [2])

        # Insert a value smaller than the root, this should go on the left
        self.btree.insert(1)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [1, 2])

    def test_insert_right(self):
        self.btree.insert(2)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [2])

        # Insert a value smaller than the root, this should go on the left
        self.btree.insert(3)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [2, 3])

    def test_insert_multiple(self):
        """

                    5
            4        |      6
        3   |    4.5 |  5.5   |    7
    2   |  3.5       |      6.5

        """
        self.btree.insert(5)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [5])

        # Insert a value smaller than the root, this should go on the left
        self.btree.insert(4)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [4, 5])

        # Insert a value bigger than root, this should go to the right
        self.btree.insert(6)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [4, 5, 6])

        # Insert a value smaller than the first child node of the root node
        self.btree.insert(3)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [3, 4, 5, 6])

        # Insert next value
        self.btree.insert(4.5)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [3, 4, 4.5, 5, 6])

        # Insert next value
        self.btree.insert(5.5)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [3, 4, 4.5, 5, 5.5, 6])

        # Insert next value
        self.btree.insert(7)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [3, 4, 4.5, 5, 5.5, 6, 7])

        # Insert next value
        self.btree.insert(2)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [2, 3, 4, 4.5, 5, 5.5, 6, 7])

        # Insert next value
        self.btree.insert(3.5)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [2, 3, 3.5, 4, 4.5, 5, 5.5, 6, 7])

        # Insert next value
        self.btree.insert(6.5)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [2, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7])

    def test_remove_one(self):
        # Insert a value
        self.btree.insert(0)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [0])

        # Remove the value
        self.btree.remove(0)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [])

        # Insert a value
        self.btree.insert(1.0)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [1.0])

        # Remove the value
        self.btree.remove(1.0)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [])

        # Insert a value
        self.btree.insert(65535)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [65535])

        # Remove the value
        self.btree.remove(65535)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [])

        # Insert a value
        self.btree.insert(65536)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [65536])

        # Remove the value
        self.btree.remove(65536)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [])

    def test_remove_left(self):
        # Insert a root value and a value to the left of the root
        self.btree.insert(10)
        self.btree.insert(5)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [5, 10])

        # Remove the value to the left of the root
        self.btree.remove(5)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [10])

    def test_remove_right(self):
        # Insert a root value and a value to the right of the root
        self.btree.insert(10)
        self.btree.insert(15)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [10, 15])

        # Remove the value to the left of the root
        self.btree.remove(15)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [10])

    def test_remove_multiple(self):
        """
                        5
              4                      6
        3          4.5        5.5            7
      2   3.5                            6.5
        """
        self.test_insert_multiple()

        # Remove one from left
        self.btree.remove(2)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7])

        # Remove one from right
        self.btree.remove(5.5)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [3, 3.5, 4, 4.5, 5, 6, 6.5, 7])

        # Remove root from right
        self.btree.remove(5)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [3, 3.5, 4, 4.5, 6, 6.5, 7])

        # Remove one by one in remaining tree
        self.btree.remove(3)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [3.5, 4, 4.5, 6, 6.5, 7])

        # Remove one by one in remaining tree
        self.btree.remove(3.5)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [4, 4.5, 6, 6.5, 7])

        # Remove one by one in remaining tree
        self.btree.remove(4)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [4.5, 6, 6.5, 7])

        # Remove one by one in remaining tree
        self.btree.remove(4.5)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [6, 6.5, 7])

        # Remove one by one in remaining tree
        self.btree.remove(7)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [6, 6.5])

        # Remove one by one in remaining tree
        self.btree.remove(6)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [6.5])

        # Remove one by one in remaining tree
        self.btree.remove(6.5)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [])

    def test_remove_empty(self):
        # Ensure binary tree is empty
        self.assertEqual(self.btree.max_depth(), 0)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [])

        # Try removing a value from the empty btree
        self.btree.remove(6)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [])

        # Try removing another value from the empty btree
        self.btree.remove(1000)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [])

        # Try removing another value from the empty btree
        self.btree.remove(65535)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [])

        # Insert a few values
        self.btree.insert(100)
        self.btree.insert(1)
        self.btree.insert(1000)
        self.btree.insert(99)
        self.btree.insert(101)
        self.btree.insert(500)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [1, 99, 100, 101, 500, 1000])

        # Remove all values
        self.btree.remove(100)
        self.btree.remove(1)
        self.btree.remove(1000)
        self.btree.remove(99)
        self.btree.remove(101)
        self.btree.remove(500)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [])

        # Ensure binary tree is empty
        self.assertEqual(self.btree.max_depth(), 0)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [])

        # Try removing a value from the empty btree
        self.btree.remove(6)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [])

    def test_max_depth_none(self):
        # Ensure binary tree is empty
        self.assertEqual(self.btree.max_depth(), 0)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [])

        self.assertEqual(self.btree.max_depth(), 0)

    def test_max_depth_one(self):
        # Ensure binary tree is empty
        self.assertEqual(self.btree.max_depth(), 0)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [])

        self.assertEqual(self.btree.max_depth(), 0)

        # Insert one value and then verify max depth is now 1
        self.btree.insert(1)
        self.assertEqual(self.btree.max_depth(), 1)

        # Remove the value and verify max depth is 0 again
        self.btree.remove(1)
        self.assertEqual(self.btree.max_depth(), 0)

        # Insert one value and then verify max depth is now 1
        self.btree.insert(10)
        self.assertEqual(self.btree.max_depth(), 1)

        # Remove the value and verify max depth is 0 again
        self.btree.remove(10)
        self.assertEqual(self.btree.max_depth(), 0)

    def test_max_depth_left_tree_only(self):
        for i in range(100, -1, -1):
            self.btree.insert(i)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [i for i in range(101)])  # 0..100 (inclusive)

        # Verify the max depth is 101 due to 101 items being inserted only as left tree nodes
        self.assertEqual(self.btree.max_depth(), 101)

    def test_max_depth_right_tree_only(self):
        for i in range(0, 101, 1):
            self.btree.insert(i)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [i for i in range(101)])  # 0..100 (inclusive)

        # Verify the max depth is 101 due to 101 items being inserted only as right tree nodes
        self.assertEqual(self.btree.max_depth(), 101)

    def test_max_depth_ten(self):
        for i in range(0, 100, 10):
            self.btree.insert(i)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [i for i in range(0, 100, 10)])

        # Verify the max depth is 10 (only right tree items were inserted)
        self.assertEqual(self.btree.max_depth(), 10)

        # Insert a few left tree items, but less than total on right tree
        for i in range(5, 85, 10):
            self.btree.insert(i)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        expected_result = sorted(list(set([i for i in range(0, 100, 10)] + [i for i in range(5, 85, 10)])))
        self.assertEqual(result, expected_result)

        # Verify the max depth is 10
        self.assertEqual(self.btree.max_depth(), 10)

        # Insert one more to the left of the most right node to create a max depth of 11
        self.btree.insert(99)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, sorted(expected_result + [99]))

        # Verify the max depth is 11 (one extra item was added)
        self.assertEqual(self.btree.max_depth(), 11)

    def test_min_one(self):
        # Ensure binary tree is empty
        self.assertEqual(self.btree.max_depth(), 0)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [])

        self.assertEqual(self.btree.max_depth(), 0)

        self.btree.insert(50)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [50])
        self.assertEqual(self.btree.min().value, 50)

    def test_min_left_only(self):
        for i in range(1000, 199, -100):
            self.btree.insert(i)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, sorted([i for i in range(1000, 199, -100)]))
        self.assertEqual(self.btree.min().value, 200)

    def test_min_right_only(self):
        for i in range(200, 1001, 100):
            self.btree.insert(i)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [i for i in range(200, 1001, 100)])
        self.assertEqual(self.btree.min().value, 200)

    def test_min_left_right(self):
        data = []
        for i in range(131, 200, 1):
            if i % 3:
                data.append(i)
                self.btree.insert(i)
            elif i % 5:
                data.append(i)
                self.btree.insert(i)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, data)
        self.assertEqual(self.btree.min().value, 131)

    def test_search_empty(self):
        # Ensure binary tree is empty
        self.assertEqual(self.btree.max_depth(), 0)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [])

        self.assertEqual(self.btree.search(0), False)
        self.assertEqual(self.btree.search(100), False)
        self.assertEqual(self.btree.search(200), False)
        self.assertEqual(self.btree.search(155), False)

    def test_search_one(self):
        # Ensure binary tree is empty
        self.assertEqual(self.btree.max_depth(), 0)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [])

        self.btree.insert(1)
        self.assertEqual(self.btree.search(1), True)
        self.assertEqual(self.btree.search(0), False)
        self.assertEqual(self.btree.search(2), False)

    def test_search_multiple(self):
        """
                        5
              4                      6
        3          4.5        5.5            7
      2   3.5                            6.5
        """
        # Create tree
        self.test_insert_multiple()

        # Search for existent values
        self.assertEqual(self.btree.search(2), True)
        self.assertEqual(self.btree.search(3), True)
        self.assertEqual(self.btree.search(3.5), True)
        self.assertEqual(self.btree.search(4), True)
        self.assertEqual(self.btree.search(4.5), True)
        self.assertEqual(self.btree.search(5), True)
        self.assertEqual(self.btree.search(5.5), True)
        self.assertEqual(self.btree.search(6), True)
        self.assertEqual(self.btree.search(7), True)
        self.assertEqual(self.btree.search(6.5), True)

        # Search for non-existent values
        self.assertEqual(self.btree.search(0), False)
        self.assertEqual(self.btree.search(1), False)
        self.assertEqual(self.btree.search(8), False)

    def test_print_inorder(self):
        # Create tree
        self.test_insert_multiple()

        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [2, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7])

    def test_print_preorder(self):
        # Create tree
        self.test_insert_multiple()

        result = self.btree.print_tree(order=BinaryTreeEnum.PrintPreOrder, returnresult=True)
        self.assertEqual(result, [5, 4, 3, 2, 3.5, 4.5, 6, 5.5, 7, 6.5])

    def test_print_postorder(self):
        # Create tree
        self.test_insert_multiple()

        result = self.btree.print_tree(order=BinaryTreeEnum.PrintPostOrder, returnresult=True)
        self.assertEqual(result, [2, 3.5, 3, 4.5, 4, 5.5, 6.5, 7, 6, 5])

    def test_is_balanced_empty(self):
        # Ensure binary tree is empty
        self.assertEqual(self.btree.max_depth(), 0)
        result = self.btree.print_tree(order=BinaryTreeEnum.PrintInOrder, returnresult=True)
        self.assertEqual(result, [])

        self.assertEqual(self.btree.is_balanced(), True)

    def test_is_balanced_left_by_one(self):
        # Insert 2 elements on left
        self.btree.insert(5)
        self.btree.insert(4)
        # Verify tree is balanced
        self.assertEqual(self.btree.is_balanced(), True)

    def test_is_balanced_left_by_one_multiple_elements(self):
        # Insert 1 root node, 2 left child nodes and one right child node.
        self.btree.insert(5)
        self.btree.insert(4)
        self.btree.insert(3)
        self.btree.insert(6)
        # Verify tree is balanced
        self.assertEqual(self.btree.is_balanced(), True)

    def test_is_balanced_left_by_two(self):
        # Insert 1 root node, 3 left child nodes and one right child node.
        self.btree.insert(5)
        self.btree.insert(4)
        self.btree.insert(3)
        self.btree.insert(2)
        self.btree.insert(6)
        # Verify tree is balanced
        self.assertEqual(self.btree.is_balanced(), False)

    def test_is_balanced_right_by_one(self):
        # Insert 2 elements on right
        self.btree.insert(5)
        self.btree.insert(6)
        # Verify tree is balanced
        self.assertEqual(self.btree.is_balanced(), True)

    def test_is_balanced_right_by_one_multiple_elements(self):
        # Insert 1 root node, 2 right child nodes and one left child node.
        self.btree.insert(5)
        self.btree.insert(6)
        self.btree.insert(7)
        self.btree.insert(4)
        # Verify tree is balanced
        self.assertEqual(self.btree.is_balanced(), True)

    def test_is_balanced_right_by_two(self):
        # Insert 1 root node, 3 right child nodes and one left child node.
        self.btree.insert(5)
        self.btree.insert(6)
        self.btree.insert(7)
        self.btree.insert(8)
        self.btree.insert(4)
        # Verify tree is balanced
        self.assertEqual(self.btree.is_balanced(), False)

    def test_is_balanced_left_by_many(self):
        """
                    5
            4        |      6
        3   |    4.5 |  5.5   |    7
    2   |  3.5       |      6.5
        """
        self.test_insert_multiple()
        # Verify tree is balanced
        self.assertEqual(self.btree.is_balanced(), True)

        # Insert one more on the left
        self.btree.insert(3.2)
        # Verify tree is balanced
        self.assertEqual(self.btree.is_balanced(), True)

        # Insert one more on the left, which will create one more depth level on the left
        self.btree.insert(3.3)
        # Verify tree is no longer balanced
        self.assertEqual(self.btree.is_balanced(), False)

    def test_is_balanced_right_by_many(self):
        """
                    5
            4        |      6
        3   |    4.5 |  5.5   |    7
    2   |  3.5       |      6.5
        """
        self.test_insert_multiple()
        # Verify tree is balanced
        self.assertEqual(self.btree.is_balanced(), True)

        # Insert one more on the left
        self.btree.insert(6.6)
        # Verify tree is balanced
        self.assertEqual(self.btree.is_balanced(), True)

        # Insert one more on the left, which will create one more depth level on the left
        self.btree.insert(6.7)
        # Verify tree is no longer balanced
        self.assertEqual(self.btree.is_balanced(), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)
