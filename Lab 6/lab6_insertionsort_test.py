"""Test cases for insertion sort, quick sort, written by Jae Park for CPE 202"""
from unittest import TestCase
import random

from lab6_insertionsort import insertion_sort
from quicksort import quick_sort


class Test(TestCase):
    def test_insertion_sort(self):
        numbers = list(range(100))
        random.shuffle(numbers)
        self.assertNotEqual(numbers, list(range(100)))
        insertion_sort(numbers)
        self.assertEqual(numbers, list(range(100)))

    def test_quicksort(self):
        numbers = list(range(100))
        random.shuffle(numbers)
        self.assertNotEqual(numbers, list(range(100)))
        quick_sort(numbers, 0, len(numbers) - 1)
        self.assertEqual(numbers, list(range(100)))
