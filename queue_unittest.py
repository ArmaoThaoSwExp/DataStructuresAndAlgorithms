"""
Author: Armao Thao

Description:
    Unit test for hash table.
"""

import queue
import unittest


class TestQueueAlg(unittest.TestCase):
    def assertRaisesWithMessage(self, msg, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            self.assertFail()
        except Exception as inst:
            self.assertEqual(inst.message, msg)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_all_cmds(self):
        self.queue = queue.Queue()
        print("\nTest out empty queue")
        self.assertEqual(self.queue.size(), 0)
        self.assertEqual(self.queue.is_empty(), True)
        self.assertRaisesWithMessage("Cannot dequeue because queue is empty!", self.queue.dequeue)

        print("\nTest inserting items into queue and checking for item")
        data = []
        for i in range(50):
            if (i % 2) == 0:
                data.append(str(i))
            else:
                data.append(i)
            self.queue.enqueue(data[-1])
            self.assertEqual(self.queue.size(), len(data))
            self.assertEqual(self.queue.is_empty(), False)

        print("\nTest dequeuing items into queue and checking for item")
        for i in range(49):
            item = self.queue.dequeue()
            self.assertEqual(item, data.pop(0))
            self.assertEqual(self.queue.size(), len(data))
            self.assertEqual(self.queue.is_empty(), False)

        item = self.queue.dequeue()
        self.assertEqual(item, data.pop(0))
        self.assertEqual(self.queue.size(), len(data))
        self.assertEqual(self.queue.is_empty(), True)

        print("\nTest that queue is empty again")
        self.assertEqual(self.queue.size(), 0)
        self.assertEqual(self.queue.is_empty(), True)
        self.assertRaisesWithMessage("Cannot dequeue because queue is empty!", self.queue.dequeue)


if __name__ == "__main__":
    print("\nRun Queue unit test")
    unittest.main(verbosity=2)
