from unittest import TestCase
from src.sort import selection_sort
from test_utils import is_sorted


class TestSelectionSort(TestCase):
    def test_selection_sort(self):
        self.assertTrue(is_sorted(selection_sort([3, 2, 5, 1, 6, 8, -2, 15])))

    def test_selection_sort_zeros(self):
        self.assertTrue(is_sorted(selection_sort([0, 0, 0, 0, 0, 0])))

    def test_selection_sort_letters(self):
        self.assertTrue(is_sorted(selection_sort(["d", "r", "a", "b", "x", "t", "u"])))

    def test_selection_sort_empty(self):
        self.assertTrue(is_sorted(selection_sort([])))
