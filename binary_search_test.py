import unittest
from binary_search import binary_search

# test_binary_search.py

class TestBinarySearch(unittest.TestCase):
    
    def test_target_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
    
    def test_target_not_found(self):
        self.assertIsNone(binary_search([1, 2, 3, 4, 5], 6))
    
    def test_empty_list(self):
        self.assertIsNone(binary_search([], 1))
    
    def test_single_element_found(self):
        self.assertEqual(binary_search([1], 1), 0)
    
    def test_single_element_not_found(self):
        self.assertIsNone(binary_search([1], 2))
    
    def test_first_element(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)
    
    def test_last_element(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)
    
    def test_large_list(self):
        large_list = list(range(1000))
        self.assertEqual(binary_search(large_list, 500), 500)
        self.assertIsNone(binary_search(large_list, 1001))

if __name__ == '__main__':
    unittest.main()
