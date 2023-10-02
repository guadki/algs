from unittest import TestCase
from src.sort import quicksort
from test_utils import is_sorted


class TestQuicksort(TestCase):
    def test_quicksort(self):
        self.assertTrue(is_sorted(quicksort([3, 2, 5, 1, 6, 8, -2, 15])))

    def test_quicksort_zeros(self):
        self.assertTrue(is_sorted(quicksort([0, 0, 0, 0, 0, 0])))

    def test_quicksort_letters(self):
        self.assertTrue(is_sorted(quicksort(["d", "r", "a", "b", "x", "t", "u"])))

    def test_quicksort_empty(self):
        self.assertTrue(is_sorted(quicksort([])))
