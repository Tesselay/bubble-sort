import unittest
import bubbleSort


class TestSorting(unittest.TestCase):
    def test_simple_list(self):
        numbers = [1, 5, 3, 2, 9, 4, 7, 8, 0, 6]
        numbers = bubbleSort.bubble_sort(numbers)

        sorted_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(numbers, sorted_numbers, "Should be of same order")

    def test_negative_list(self):
        numbers = [-3, 2, -1, -7, 4, 9, -12, -11, 5, 7]
        numbers = bubbleSort.bubble_sort(numbers)

        sorted_numbers = [-12, -11, -7, -3, -1, 2, 4, 5, 7, 9]
        self.assertEqual(numbers, sorted_numbers, "Should be of same order")

    def test_duplicates_list(self):
        numbers = [7, 3, 4, 7, 9, 3, 4, 9, 4, 1]
        numbers = bubbleSort.bubble_sort(numbers)

        sorted_numbers = [1, 3, 3, 4, 4, 4, 7, 7, 9, 9]
        self.assertEqual(numbers, sorted_numbers, "Should be of same order")

    def test_float_list(self):
        numbers = [2, 3.6, 7, 4.1, 9, 12, 12.01, -1.2, 5.0000451]
        numbers = bubbleSort.bubble_sort(numbers)

        sorted_numbers = [-1.2, 2, 3.6, 4.1, 5.0000451, 7, 9, 12, 12.01]
        self.assertEqual(numbers, sorted_numbers, "Should be of same order")

    def test_pinf_lists(self):
        aa = [1, 5, 8, 2, 11, 9, 7, 14, 15]
        ab = [33, 23, 15, 8, 99, 15, 15, 12, 3]
        ac = [111, 24, 55, 63, 44, 88, 18, 1, 25]
        ad = [99, 88, 77, 65, 40, 25, 19, 17, 13]

        print("PINF LISTS")

        aa = bubbleSort.bubble_sort(aa)
        ab = bubbleSort.bubble_sort(ab)
        ac = bubbleSort.bubble_sort(ac)
        ad = bubbleSort.bubble_sort(ad)

        aa_sorted = [1, 2, 5, 7, 8, 9, 11, 14, 15]
        ab_sorted = [3, 8, 12, 15, 15, 15, 23, 33, 99]
        ac_sorted = [1, 18, 24, 25, 44, 55, 63, 88, 111]
        ad_sorted = [13, 17, 19, 25, 40, 65, 77, 88, 99]

        self.assertEqual(aa, aa_sorted, "Should be of same order")
        self.assertEqual(ab, ab_sorted, "Should be of same order")
        self.assertEqual(ac, ac_sorted, "Should be of same order")
        self.assertEqual(ad, ad_sorted, "Should be of same order")


if __name__ == '__main__':
    unittest.main()
