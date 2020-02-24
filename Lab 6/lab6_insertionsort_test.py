"""Test cases for insertion sort, written by Jae Park for CPE 202"""
from unittest import TestCase
import random

from lab6_insertionsort import insertion_sort


class Test(TestCase):
    def test_insertion_sort(self):
        numbers = list(range(100))
        random.shuffle(numbers)
        self.assertNotEqual(numbers, range(100))
        insertion_sort(numbers)
        self.assertEqual(numbers, range(100))
