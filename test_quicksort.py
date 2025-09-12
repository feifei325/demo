import unittest
from quicksort import quicksort, quicksort_inplace


class TestQuickSort(unittest.TestCase):
    
    def test_empty_array(self):
        """测试空数组"""
        self.assertEqual(quicksort([]), [])
        
        arr = []
        quicksort_inplace(arr)
        self.assertEqual(arr, [])
    
    def test_single_element(self):
        """测试单元素数组"""
        self.assertEqual(quicksort([5]), [5])
        
        arr = [5]
        quicksort_inplace(arr)
        self.assertEqual(arr, [5])
    
    def test_sorted_array(self):
        """测试已排序数组"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(quicksort(arr), [1, 2, 3, 4, 5])
        
        arr_inplace = [1, 2, 3, 4, 5]
        quicksort_inplace(arr_inplace)
        self.assertEqual(arr_inplace, [1, 2, 3, 4, 5])
    
    def test_reverse_sorted_array(self):
        """测试逆序数组"""
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(quicksort(arr), [1, 2, 3, 4, 5])
        
        arr_inplace = [5, 4, 3, 2, 1]
        quicksort_inplace(arr_inplace)
        self.assertEqual(arr_inplace, [1, 2, 3, 4, 5])
    
    def test_random_array(self):
        """测试随机数组"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(quicksort(arr), expected)
        
        arr_inplace = [64, 34, 25, 12, 22, 11, 90]
        quicksort_inplace(arr_inplace)
        self.assertEqual(arr_inplace, expected)
    
    def test_duplicate_elements(self):
        """测试包含重复元素的数组"""
        arr = [3, 1, 3, 2, 1, 3]
        expected = [1, 1, 2, 3, 3, 3]
        self.assertEqual(quicksort(arr), expected)
        
        arr_inplace = [3, 1, 3, 2, 1, 3]
        quicksort_inplace(arr_inplace)
        self.assertEqual(arr_inplace, expected)
    
    def test_negative_numbers(self):
        """测试包含负数的数组"""
        arr = [-3, 1, -2, 4, 0, -1]
        expected = [-3, -2, -1, 0, 1, 4]
        self.assertEqual(quicksort(arr), expected)
        
        arr_inplace = [-3, 1, -2, 4, 0, -1]
        quicksort_inplace(arr_inplace)
        self.assertEqual(arr_inplace, expected)
    
    def test_large_array(self):
        """测试大数组"""
        import random
        arr = [random.randint(1, 1000) for _ in range(100)]
        sorted_arr = sorted(arr)
        
        self.assertEqual(quicksort(arr), sorted_arr)
        
        arr_copy = arr.copy()
        quicksort_inplace(arr_copy)
        self.assertEqual(arr_copy, sorted_arr)


if __name__ == '__main__':
    unittest.main()