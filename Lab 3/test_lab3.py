import unittest

from queues import QueueArray
from queues import QueueLinked


class MyTest(unittest.TestCase):
    def test_is_empty(self):
        """tests is_empty() function"""
        my_queue = QueueArray(3)
        self.assertTrue(my_queue.is_empty())
        my_queue.enqueue(0)
        self.assertFalse(my_queue.is_empty())
        my_queue.dequeue()
        self.assertTrue(my_queue.is_empty())

        my_linked = QueueLinked(3)
        self.assertTrue(my_linked.is_empty())
        my_linked.enqueue(0)
        self.assertFalse(my_linked.is_empty())
        my_linked.dequeue()
        self.assertTrue(my_linked.is_empty())

    def test_is_full(self):
        """tests is_full() function"""
        my_queue = QueueArray(3)
        self.assertFalse(my_queue.is_full())
        my_queue.enqueue(1)
        self.assertFalse(my_queue.is_full())
        my_queue.enqueue(2)
        self.assertFalse(my_queue.is_full())
        my_queue.enqueue(3)
        self.assertTrue(my_queue.is_full())
        my_queue.dequeue()
        self.assertFalse(my_queue.is_full())

        my_linked = QueueLinked(3)
        self.assertFalse(my_linked.is_full())
        my_linked.enqueue(1)
        self.assertFalse(my_linked.is_full())
        my_linked.enqueue(2)
        self.assertFalse(my_linked.is_full())
        my_linked.enqueue(3)
        self.assertTrue(my_linked.is_full())
        my_linked.dequeue()
        self.assertFalse(my_linked.is_full())

    def test_queue_array(self):
        """tests enqueue() function"""
        my_queue = QueueArray(3)
        my_queue.enqueue(0)
        self.assertEqual(my_queue.items, [0, None, None, None])
        my_queue.enqueue(1)
        self.assertEqual(my_queue.items, [0, 1, None, None])
        my_queue.enqueue(2)
        self.assertEqual(my_queue.items, [0, 1, 2, None])
        self.assertRaises(IndexError, my_queue.enqueue, 3)

        val = my_queue.dequeue()
        self.assertEqual(val, 0)
        my_queue.enqueue(3)
        self.assertEqual(my_queue.size(), 3)
        val = my_queue.dequeue()
        self.assertEqual(val, 1)
        self.assertEqual(my_queue.size(), 2)
        my_queue.enqueue(4)
        self.assertEqual(my_queue.items, [4, 1, 2, 3])
        self.assertEqual(my_queue.size(), 3)
        self.assertRaises(IndexError, my_queue.enqueue, 5)

    def test_queue_linked(self):
        my_linked = QueueLinked(3)
        my_linked.enqueue(0)
        my_linked.enqueue(1)
        my_linked.enqueue(2)
        self.assertRaises(IndexError, my_linked.enqueue, 3)
        my_linked.dequeue()
        my_linked.enqueue(3)
        my_linked.dequeue()
        my_linked.enqueue(4)
        self.assertEqual(my_linked.dequeue(), 2)
        self.assertEqual(my_linked.size(), 2)
        self.assertEqual(my_linked.dequeue(), 3)
        self.assertEqual(my_linked.size(), 1)
        self.assertEqual(my_linked.dequeue(), 4)
        self.assertEqual(my_linked.size(), 0)
        self.assertRaises(IndexError, my_linked.dequeue)

if __name__ == '__main__':
    unittest.main()

