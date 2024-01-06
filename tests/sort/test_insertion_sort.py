from unittest import TestCase
from algs.sort import insertion_sort
from test_utils import is_sorted


class TestInsertionSort(TestCase):
    def test_insertion_sort(self):
        self.assertTrue(is_sorted(insertion_sort([3, 2, 5, 1, 6, 8, -2, 15])))

    def test_insertion_sort_zeros(self):
        self.assertTrue(is_sorted(insertion_sort([0, 0, 0, 0, 0, 0])))

    def test_insertion_sort_letters(self):
        self.assertTrue(is_sorted(insertion_sort(["d", "r", "a", "b", "x", "t", "u"])))

    def test_insertion_sort_empty(self):
        self.assertTrue(is_sorted(insertion_sort([])))
