import unittest
from stacks import StackArray
from stacks import StackLinked

class MyTest(unittest.TestCase):
    def test_stack_array1(self):
        stack = StackArray()
        self.assertEqual(stack.size(), 0)
        self.assertTrue(stack.is_empty())

    def test_stack_array2(self):
        stack = StackArray()
        for i in range(3):
            stack.push(i)
        self.assertEqual(stack.size(), 3)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.peek(), 2)

    def test_stack_array3(self):
        stack = StackArray()
        for i in range(3):
            stack.push(i)
        self.assertEqual(stack.size(), 3)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), 0)
        self.assertEqual(stack.size(), 0)
        self.assertTrue(stack.is_empty())

    def test_stack_array4(self):
        stack = StackArray()
        for i in range(10):
            stack.push(i)
        for i in range(10):
            val = stack.pop()
        self.assertRaises(IndexError, stack.pop)
        self.assertRaises(IndexError, stack.peek)

    def test_stack_array5(self):
        stack = StackArray()
        for i in range(3):
            stack.push(i)
            val = stack.pop()
            stack.push(val)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.peek(), 1)
        self.assertEqual(stack.pop(), 1)

    def test_stack_linked1(self):
        stack = StackLinked()
        self.assertEqual(stack.size(), 0)
        self.assertTrue(stack.is_empty())

    def test_stack_linked2(self):
        stack = StackLinked()
        for i in range(3):
            stack.push(i)
        self.assertEqual(stack.size(), 3)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.peek(), 2)

    def test_stack_linked3(self):
        stack = StackLinked()
        for i in range(3):
            stack.push(i)
        self.assertEqual(stack.size(), 3)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), 0)
        self.assertEqual(stack.size(), 0)
        self.assertTrue(stack.is_empty())

    def test_stack_linked4(self):
        stack = StackLinked()
        for i in range(10):
            stack.push(i)
        for i in range(10):
            val = stack.pop()
        self.assertRaises(IndexError, stack.pop)
        self.assertRaises(IndexError, stack.peek)

    def test_stack_linked5(self):
        stack = StackLinked()
        for i in range(3):
            stack.push(i)
            val = stack.pop()
            stack.push(val)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.peek(), 1)
        self.assertEqual(stack.pop(), 1)

if __name__ == '__main__':
    unittest.main()

