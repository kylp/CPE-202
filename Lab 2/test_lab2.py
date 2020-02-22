import unittest
import array_list as array_list
import linked_list as linked_list
from array_list import ArrayList 
from linked_list import Node 

class MyTest(unittest.TestCase):
    def test_array_list1(self):
        lst = ArrayList()
        self.assertEqual(array_list.size(lst), 0)
        self.assertEqual(lst.capacity, 2)

    def test_array_list2(self):
        lst = ArrayList()
        for i in range(3):
            lst = array_list.insert(lst, i, i)
        self.assertEqual(array_list.size(lst), 3)
        self.assertEqual(lst.capacity, 4)

    def test_array_list3(self):
        lst = ArrayList()
        for i in range(3):
            lst = array_list.insert(lst, 0, i)
        pos = array_list.size(lst) - 1
        self.assertEqual(array_list.get(lst, pos), 0)

    def test_array_list4(self):
        lst = ArrayList()
        for i in range(10):
            lst = array_list.insert(lst, i, 0)
        self.assertTrue(array_list.contains(lst, 0))
        self.assertTrue(array_list.contains(lst, 1))
        self.assertTrue(array_list.contains(lst, 2))
        self.assertTrue(array_list.contains(lst, 3))
        self.assertTrue(array_list.contains(lst, 4))
        self.assertTrue(array_list.contains(lst, 5))
        self.assertFalse(array_list.contains(lst, -1))

    def test_array_list5(self):
        lst = ArrayList()
        for i in range(10):
            lst = array_list.insert(lst, i, i)

        for i in range(10):
            self.assertEqual(array_list.search(lst, i), i)
        self.assertEqual(array_list.search(lst, -1), None)

    def test_array_list6(self):
        lst = ArrayList()
        for i in range(3):
            lst = array_list.insert(lst, i, i)
        lst2 = ArrayList()
        lst2.arr = [0, 1, 2, None]
        lst2.capacity = 4
        lst2.num_items = 3 
        self.assertEqual(lst, lst2)
        lst = array_list.remove(lst, 1)
        self.assertEqual(lst.capacity, lst2.capacity)
        lst2.arr = [2, None]
        lst2.capacity = 2 
        lst2.num_items = 1 
        self.assertEqual(array_list.remove(lst, 0), lst2)

    def test_array_list7(self):
        lst = ArrayList()
        for i in range(3):
            lst = array_list.insert(lst, i, 0)

        lst, val = array_list.pop(lst, array_list.size(lst) - 1)
        self.assertEqual(val, 0)
        lst, val = array_list.pop(lst, array_list.size(lst) - 1)
        self.assertEqual(val, 1)

    def test_array_list8(self):
        lst = ArrayList()
        for i in range(3):
            lst = array_list.insert(lst, i, 0)

        lst, val = array_list.pop(lst, 0)
        self.assertEqual(val, 2)
        lst, val = array_list.pop(lst, 0)
        self.assertEqual(val, 1)

    def test_linked_list1(self):
        lst = None
        for i in range(3):
            lst = linked_list.insert(lst, i, i)
        self.assertEqual(lst.val, 0)
        self.assertEqual(lst.next.val, 1)
        self.assertEqual(lst.next.next.val, 2)
        self.assertEqual(lst.next.next.next, None)

    def test_linked_list2(self):
        lst = None
        for i in range(3):
            lst = linked_list.insert(lst, i, 0)
        self.assertEqual(lst.val, 2)
        self.assertEqual(lst.next.val, 1)
        self.assertEqual(lst.next.next.val, 0)
        self.assertEqual(lst.next.next.next, None)

    def test_linked_list3(self):
        lst = None
        for i in range(3):
            lst = linked_list.insert(lst, i, 0)
        self.assertEqual(linked_list.get(lst, 0), 2)
        self.assertEqual(linked_list.get(lst, 1), 1)
        self.assertEqual(linked_list.get(lst, 2), 0)
        self.assertRaises(IndexError, linked_list.get, lst, 3)
        self.assertRaises(IndexError, linked_list.get, lst, -1)

    def test_linked_list4(self):
        lst = None
        for i in range(3):
            lst = linked_list.insert(lst, i, i)
        self.assertEqual(linked_list.search(lst, 0), 0)
        self.assertEqual(linked_list.search(lst, 1), 1)
        self.assertEqual(linked_list.search(lst, 2), 2)
        self.assertEqual(linked_list.search(lst, 3), None)

    def test_linked_list5(self):
        lst = None
        for i in range(3):
            lst = linked_list.insert(lst, i, i)
        self.assertTrue(linked_list.contains(lst, 0))
        self.assertTrue(linked_list.contains(lst, 1))
        self.assertTrue(linked_list.contains(lst, 2))
        self.assertFalse(linked_list.contains(lst, 3))

    def test_linked_list6(self):
        lst = None
        for i in range(3):
            lst = linked_list.insert(lst, i, i)
        self.assertEqual(linked_list.remove(lst, 0), Node(1, Node(2, None)))
        lst = linked_list.remove(lst, 0)
        self.assertEqual(linked_list.remove(lst, 1), Node(2, None))
        lst = linked_list.remove(lst, 1)
        self.assertEqual(linked_list.remove(lst, 2), None)

    def test_linked_list7(self):
        lst = None
        for i in range(3):
            lst = linked_list.insert(lst, i, i)
        self.assertEqual(linked_list.pop(lst, 0), (Node(1, Node(2, None)), 0))
        self.assertEqual(linked_list.pop(lst, 2), (Node(0, Node(1, None)), 2))

    def test_linked_list8(self):
        lst = None
        for i in range(10):
            lst = linked_list.insert(lst, i, 0)
        self.assertEqual(linked_list.size(lst), 10)

if __name__ == '__main__':
    unittest.main()

