from unittest import TestCase
from algs.sort import bubble_sort
from test_utils import is_sorted


class TestBubbleSort(TestCase):
    def test_bubble_sort(self):
        self.assertTrue(is_sorted(bubble_sort([3, 2, 5, 1, 6, 8, -2, 15])))

    def test_bubble_sort_zeros(self):
        self.assertTrue(is_sorted(bubble_sort([0, 0, 0, 0, 0, 0])))

    def test_bubble_sort_letters(self):
        self.assertTrue(is_sorted(bubble_sort(["d", "r", "a", "b", "x", "t", "u"])))

    def test_bubble_sort_empty(self):
        self.assertTrue(is_sorted(bubble_sort([])))
