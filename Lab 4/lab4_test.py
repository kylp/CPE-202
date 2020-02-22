import unittest

from ordered_list import OrderedList

class MyTest(unittest.TestCase):
    def test_1(self):
        ordered_list = OrderedList()
        self.assertEqual(ordered_list.is_empty(), True)
        ordered_list.add(2)
        self.assertEqual(ordered_list.head.val, 2)
        self.assertEqual(ordered_list.tail.val, 2)
        ordered_list.add(1)
        ordered_list.add(3)
        self.assertEqual(ordered_list.size(), 3)

    def test_2(self):
        ordered_list = OrderedList()
        ordered_list.add(2)
        self.assertEqual(ordered_list.head.val, 2)
        self.assertEqual(ordered_list.tail.val, 2)
        ordered_list.add(1)
        ordered_list.add(3)
        self.assertEqual(ordered_list.index(1), 0)
        self.assertEqual(ordered_list.index(2), 1)
        self.assertEqual(ordered_list.index(3), 2)
        self.assertRaises(LookupError, ordered_list.index, 4)

    def test_3(self):
        ordered_list = OrderedList()
        self.assertEqual(ordered_list.is_empty(), True)
        ordered_list.add(2)
        self.assertEqual(ordered_list.head.val, 2)
        self.assertEqual(ordered_list.tail.val, 2)
        ordered_list.add(1)
        ordered_list.add(3)
        self.assertEqual(ordered_list.search_forward(3), True)
        self.assertEqual(ordered_list.search_backward(3), True)

    def test_4(self):
        ordered_list = OrderedList()
        self.assertEqual(ordered_list.is_empty(), True)
        ordered_list.add(2)
        ordered_list.add(1)
        ordered_list.add(3)
        self.assertEqual(ordered_list.head.val, 1)
        self.assertEqual(ordered_list.tail.val, 3)
        self.assertRaises(ValueError, ordered_list.remove, 4)
        self.assertEqual(ordered_list.remove(2), 1)
        self.assertEqual(ordered_list.pop(0), 1)
        self.assertEqual(ordered_list.pop(), 3)

    def test_5(self):
        ordered_list = OrderedList()
        ordered_list.add(1)
        ordered_list.add(2)
        ordered_list.add(5)
        ordered_list.add(3)
        self.assertEqual(ordered_list.head.val, 1)
        self.assertEqual(ordered_list.tail.val, 5)
        self.assertEqual(ordered_list.size(), 4)

    def test_6(self):
        ordered_list = OrderedList()
        ordered_list.add(1)
        ordered_list.add(2)
        ordered_list.add(5)
        ordered_list.add(3)
        self.assertEqual(ordered_list.head.val, 1)
        self.assertEqual(ordered_list.tail.val, 5)
        self.assertEqual(ordered_list.index(1), 0)
        self.assertEqual(ordered_list.index(2), 1)
        self.assertEqual(ordered_list.index(3), 2)
        self.assertEqual(ordered_list.index(5), 3)
        self.assertRaises(LookupError, ordered_list.index, 4)

    def test_7(self):
        ordered_list = OrderedList()
        ordered_list.add(1)
        ordered_list.add(2)
        ordered_list.add(5)
        ordered_list.add(3)
        self.assertEqual(ordered_list.head.val, 1)
        self.assertEqual(ordered_list.tail.val, 5)
        self.assertEqual(ordered_list.search_forward(4), False)
        self.assertEqual(ordered_list.search_forward(6), False)
        self.assertEqual(ordered_list.search_forward(1), True)
        self.assertEqual(ordered_list.search_backward(4), False)
        self.assertEqual(ordered_list.search_backward(2), True)
        self.assertEqual(ordered_list.search_backward(5), True)

    def test_8(self):
        ordered_list = OrderedList()
        ordered_list.add(1)
        ordered_list.add(2)
        ordered_list.add(5)
        ordered_list.add(3)
        self.assertEqual(ordered_list.head.val, 1)
        self.assertEqual(ordered_list.tail.val, 5)
        self.assertEqual(ordered_list.pop(), 5)
        self.assertEqual(ordered_list.pop(1), 2)
        self.assertEqual(ordered_list.pop(), 3)
        self.assertRaises(IndexError, ordered_list.pop, 1)
        self.assertEqual(ordered_list.index(1), 0)
        self.assertEqual(ordered_list.pop(), 1)
        self.assertRaises(IndexError, ordered_list.pop)

if __name__ == '__main__':
    unittest.main()

