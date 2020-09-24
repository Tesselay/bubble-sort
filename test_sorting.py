import unittest
import bubbleSort


class TestSorting(unittest.TestCase):
    def test_simple_list(self):
        numbers = [1, 5, 3, 2, 9, 4, 7, 8, 0, 6]
        numbers = bubbleSort.bubble_sort(numbers)

        sorted_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(numbers, sorted_numbers, "Should be of same order")


if __name__ == '__main__':
    unittest.main()
