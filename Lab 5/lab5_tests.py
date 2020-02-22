import unittest

import bst
from lab5 import TreeMap, import_classmates, search_classmate

class MyTest(unittest.TestCase):
    def test_bst1(self):
        t = None
        t = bst.insert(t, 4, 'four')
        t = bst.insert(t, 2, 'two')
        t = bst.insert(t, 3, 'three')
        t = bst.insert(t, 1, 'one')
        t = bst.insert(t, 7, 'seven')
        t = bst.insert(t, 5, 'five')
        t = bst.insert(t, 6, 'six')
        self.assertEqual(t.key, 4)

    def test_bst2(self):
        t = None
        t = bst.insert(t, 4, 'four')
        t = bst.insert(t, 2, 'two')
        t = bst.insert(t, 3, 'three')
        t = bst.insert(t, 1, 'one')
        t = bst.insert(t, 7, 'seven')
        t = bst.insert(t, 5, 'five')
        t = bst.insert(t, 6, 'six')
        self.assertEqual(bst.tree_height(t), 3)

    def test_bst3(self):
        t = None
        t = bst.insert(t, 4, 'four')
        t = bst.insert(t, 2, 'two')
        t = bst.insert(t, 3, 'three')
        t = bst.insert(t, 1, 'one')
        t = bst.insert(t, 7, 'seven')
        t = bst.insert(t, 5, 'five')
        t = bst.insert(t, 6, 'six')
        self.assertEqual(bst.get(t, 5), 'five')
        self.assertEqual(bst.get(t, 4), 'four')

    def test_bst4(self):
        t = None
        t = bst.insert(t, 4, 'four')
        t = bst.insert(t, 2, 'two')
        t = bst.insert(t, 3, 'three')
        t = bst.insert(t, 1, 'one')
        t = bst.insert(t, 7, 'seven')
        t = bst.insert(t, 5, 'five')
        t = bst.insert(t, 6, 'six')

        t = bst.delete(t, 6)
        self.assertEqual(bst.tree_height(t), 2)
        t = bst.delete(t, 7)
        self.assertEqual(bst.tree_height(t), 2)
        t = bst.delete(t, 4)
        self.assertEqual(bst.tree_height(t), 2)
        self.assertEqual(t.key, 5)

    def test_treemap1(self):
        t = TreeMap()
        t.put(4, 'four')
        t.put(2, 'two')
        t.put(3, 'three')
        t.put(1, 'one')
        t.put(7, 'seven')
        t.put(5, 'five')
        t.put(6, 'six')
        self.assertEqual(t.tree.key, 4)

    def test_treemap2(self):
        t = TreeMap()
        t.put(4, 'four')
        t.put(2, 'two')
        t.put(3, 'three')
        t.put(1, 'one')
        t.put(7, 'seven')
        t.put(5, 'five')
        t.put(6, 'six')
        self.assertEqual(t.tree_height(), 3)

    def test_treemap3(self):
        t = TreeMap()
        t.put(4, 'four')
        t.put(2, 'two')
        t.put(3, 'three')
        t.put(1, 'one')
        t.put(7, 'seven')
        t.put(5, 'five')
        t.put(6, 'six')
        self.assertEqual(t.find_min(), (1,'one'))

    def test_treemap4(self):
        t = TreeMap()
        t.put(4, 'four')
        t.put(2, 'two')
        t.put(3, 'three')
        t.put(1, 'one')
        t.put(7, 'seven')
        t.put(5, 'five')
        t.put(6, 'six')
        self.assertEqual(t.find_max(), (7,'seven'))

    def test_treemap5(self):
        t = TreeMap()
        t.put(4, 'four')
        t.put(2, 'two')
        t.put(3, 'three')
        t.put(1, 'one')
        t.put(7, 'seven')
        t.put(5, 'five')
        t.put(6, 'six')
        self.assertEqual(t.inorder_list(), [1, 2, 3, 4, 5, 6, 7])

    def test_treemap6(self):
        t = TreeMap()
        t.put(4, 'four')
        t.put(2, 'two')
        t.put(3, 'three')
        t.put(1, 'one')
        t.put(7, 'seven')
        t.put(5, 'five')
        t.put(6, 'six')
        self.assertEqual(t.preorder_list(), [4, 2, 1, 3, 7, 5, 6])

    def test_treemap7(self):
        t = TreeMap()
        t.put(4, 'four')
        t.put(2, 'two')
        t.put(3, 'three')
        t.put(1, 'one')
        t.put(7, 'seven')
        t.put(5, 'five')
        t.put(6, 'six')
        self.assertEqual(t.get(5), 'five')
        self.assertEqual(t.get(4), 'four')

    def test_treemap8(self):
        t = TreeMap()
        t.put(4, 'four')
        t.put(2, 'two')
        t.put(3, 'three')
        t.put(1, 'one')
        t.put(7, 'seven')
        t.put(5, 'five')
        t.put(6, 'six')
        self.assertEqual(t.range_search(3, 6), ['three', 'four', 'five'])

    def test_treemap9(self):
        t = TreeMap()
        t.put(4, 'four')
        t.put(2, 'two')
        t.put(3, 'three')
        t.put(1, 'one')
        t.put(7, 'seven')
        t.put(5, 'five')
        t.put(6, 'six')
        t.delete(6)
        self.assertEqual(t.tree_height(), 2)
        self.assertEqual(t.find_max(), (7,'seven'))
        self.assertEqual(t.find_min(), (1,'one'))
        t.delete(7)
        self.assertEqual(t.tree_height(), 2)
        self.assertEqual(t.find_max(), (5,'five'))
        t.delete(4)
        self.assertEqual(t.tree_height(), 2)
        self.assertEqual(t.find_max(), (5,'five'))
        self.assertEqual(t.tree.key, 5)

    def test_classmates(self):
        #substitute the file name and the path with yours.
        #filename = '/home/gradzilla/uploads/submissions/grader_programs/CPE202/Lab_5/classmates.tsv'
        #t = import_classmates(filename)
        #self.assertEqual(t.size(), 55)
        #v = search_classmate(t, 24)
        #self.assertEqual(v.major, 'CSC')
        #self.assertRaises(KeyError, search_classmate, t, 0)
        pass

if __name__ == '__main__':
    unittest.main()

