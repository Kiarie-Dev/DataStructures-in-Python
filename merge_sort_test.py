import unittest
from merge2 import merge_sort2

class TestMergeSort(unittest.TestCase):
    
    def test_sorted_list(self):
        self.assertEqual(merge_sort2([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted_list(self):
        self.assertEqual(merge_sort2([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
    def test_duplicate_elements(self):
        self.assertEqual(merge_sort2([3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])
    
    def test_empty_list(self):
        self.assertEqual(merge_sort2([]), [])
    
    def test_single_element_list(self):
        self.assertEqual(merge_sort2([1]), [1])
    
    def test_negative_numbers(self):
        self.assertEqual(merge_sort2([-1, -3, -2, 0, 2, 1]), [-3, -2, -1, 0, 1, 2])
    
    def test_large_list(self):
        large_list = list(range(1000, 0, -1))
        sorted_large_list = list(range(1, 1001))
        self.assertEqual(merge_sort2(large_list), sorted_large_list)

if __name__ == '__main__':
    unittest.main()