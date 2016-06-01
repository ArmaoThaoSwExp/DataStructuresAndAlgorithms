"""
Author: Armao Thao

Description:
    singleton unit test
"""
import unittest
from singleton import AppleSingleton


class TestUniqueCharStr(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_apple(self):
        apple = AppleSingleton.getinstance()
        apple.printapple()


if __name__ == "__main__":
    unittest.main(verbosity=2)
