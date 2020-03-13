import unittest

import bst_rb as bst
from lab10 import TreeMap, import_classmates, search_classmate

class MyTest(unittest.TestCase):
    def test_bst(self):
        t = None
        t = bst.insert(t, 1, 'one')
        self.assertEqual(t.key, 1)
        self.assertEqual(t.color, 'black')
        self.assertEqual(bst.tree_height(t), 0)
        t = bst.insert(t, 2, 'two')
        self.assertEqual(t.key, 1)
        self.assertEqual(t.right.color, 'red')
        self.assertEqual(bst.tree_height(t), 1)
        t = bst.insert(t, 3, 'three')
        self.assertEqual(t.key, 2)
        self.assertEqual(t.color, 'black')
        self.assertEqual(t.left.color, 'black')
        self.assertEqual(t.left.key, 1)
        self.assertEqual(t.right.color, 'black')
        self.assertEqual(t.right.key, 3)
        self.assertEqual(bst.tree_height(t), 1)
        t = bst.insert(t, 4, 'four')
        self.assertEqual(t.key, 2)
        self.assertEqual(t.color, 'black')
        self.assertEqual(t.left.color, 'black')
        self.assertEqual(t.left.key, 1)
        self.assertEqual(t.right.color, 'black')
        self.assertEqual(t.right.key, 3)
        self.assertEqual(t.right.right.color, 'red')
        self.assertEqual(t.right.right.key, 4)
        self.assertEqual(bst.tree_height(t), 2)
        t = bst.insert(t, 5, 'five')
        self.assertEqual(t.key, 2)
        self.assertEqual(t.color, 'black')
        self.assertEqual(t.left.color, 'black')
        self.assertEqual(t.left.key, 1)
        self.assertEqual(t.right.color, 'red')
        self.assertEqual(t.right.key, 4)
        self.assertEqual(t.right.left.color, 'black')
        self.assertEqual(t.right.left.key, 3)
        self.assertEqual(t.right.right.color, 'black')
        self.assertEqual(t.right.right.key, 5)
        self.assertEqual(bst.tree_height(t), 2)

    def test_treemap(self):
        t = TreeMap()
        t.put(1, 'one')
        t.put(2, 'two')
        t.put(3, 'three')
        t.put(4, 'four')
        t.put(5, 'five')
        self.assertEqual(t.tree.key, 2)
        self.assertEqual(t.tree_height(), 2)
        self.assertEqual(t.inorder_list(), [1, 2, 3, 4, 5])
        self.assertEqual(t.preorder_list(), [2, 1, 4, 3, 5])
        self.assertEqual(t.get(1), 'one')
        self.assertEqual(t.get(4), 'four')
        self.assertEqual(t.get(2), 'two')
        self.assertEqual(t.range_search(2, 5), ['two', 'three', 'four'])

    def test_classmates(self):
        filename = '2202-cpe202-05.tsv'
        t = import_classmates(filename)
        #change the following three lines
        self.assertEqual(t.size(), 38)
        v = search_classmate(t, 1)
        self.assertEqual(v.major, 'BMED')
        self.assertRaises(KeyError, search_classmate, t, 0)

if __name__ == '__main__':
    unittest.main()

