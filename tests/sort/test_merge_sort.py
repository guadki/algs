from unittest import TestCase
from algs.sort import merge_sort
from test_utils import is_sorted


class TestMergeSort(TestCase):
    def test_merge_sort(self):
        self.assertTrue(is_sorted(merge_sort([3, 2, 5, 1, 6, 8, -2, 15])))

    def test_merge_sort_zeros(self):
        self.assertTrue(is_sorted(merge_sort([0, 0, 0, 0, 0, 0])))

    def test_merge_sort_letters(self):
        self.assertTrue(is_sorted(merge_sort(["d", "r", "a", "b", "x", "t", "u"])))

    def test_merge_sort_empty(self):
        self.assertTrue(is_sorted(merge_sort([])))
