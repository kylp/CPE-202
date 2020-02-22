import unittest
from lab1 import get_max
from lab1 import reverse
from lab1 import search
from lab1 import fib
from lab1 import factorial_iter
from lab1 import factorial_rec


class TestCase(unittest.TestCase):
    def test_get_max(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(get_max(arr), 5)
        self.assertEqual(get_max([-2, -1, 6, 0, 2]), 6)
        self.assertEqual(get_max([]), None)
        self.assertEqual(get_max([-2, -3, -20]), -2)

    def test_reverse(self):
        self.assertEqual(reverse("qweEerty"), "ytreEewq")
        self.assertEqual(reverse(""), "")
        self.assertEqual(reverse("F"), "F")

    def test_search(self):
        self.assertEqual(search([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(search([], 5), None)
        self.assertEqual(search([1, 3, 5, 7, 8, 10], 3), 1)
        self.assertEqual(search([1, 3, 5, 7, 8, 10], 0), None)
        self.assertEqual(search([1, 3, 5, 7, 8, 10], 11), None)
        self.assertEqual(search([1, 3, 5, 7, 8, 10], 9), None)
        self.assertEqual(search([1, 3, 5, 7, 8, 10], 8), 4)

    def test_fib(self):
        def fib_numbers(n):
            sequence = []
            for i in range(n + 1):
                sequence.append(fib(i))
            return sequence

            # this will test your fib function by calling it multiple times

        self.assertEqual(fib_numbers(10),
                         [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_factorial(self):
        self.assertEqual(factorial_iter(0), 1)
        self.assertEqual(factorial_rec(0), 1)
        self.assertEqual(factorial_iter(3), 6)
        self.assertEqual(factorial_iter(3), factorial_rec(3))
        self.assertEqual(factorial_iter(10), 3628800)
        self.assertEqual(factorial_rec(10), 3628800)
        self.assertRaises(RecursionError, factorial_rec, 10000)


def main():
    # execute unit tests
    unittest.main()


if __name__ == '__main__':
    # execute main() function
    main()
