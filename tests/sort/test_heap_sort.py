from unittest import TestCase
from src.sort import heap_sort
from test_utils import is_sorted


class TestHeapSort(TestCase):
    def test_heap_sort(self):
        self.assertTrue(is_sorted(heap_sort([3, 2, 5, 1, 6, 8, -2, 15])))

    def test_heap_sort_zeros(self):
        self.assertTrue(is_sorted(heap_sort([0, 0, 0, 0, 0, 0])))

    def test_heap_sort_letters(self):
        self.assertTrue(is_sorted(heap_sort(["d", "r", "a", "b", "x", "t", "u"])))

    def test_heap_sort_empty(self):
        self.assertTrue(is_sorted(heap_sort([])))
