def quicksort_simple(arr):
    """
    快速排序算法实现 (简单版本)
    
    Args:
        arr (list): 待排序的列表
    
    Returns:
        list: 排序后的列表
    
    Example:
        >>> quicksort_simple([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    # 基本情况：如果数组长度小于等于1，直接返回
    if len(arr) <= 1:
        return arr
    
    # 选择基准元素（这里选择中间元素）
    pivot = arr[len(arr) // 2]
    
    # 分割数组
    left = [x for x in arr if x < pivot]      # 小于基准的元素
    middle = [x for x in arr if x == pivot]   # 等于基准的元素
    right = [x for x in arr if x > pivot]     # 大于基准的元素
    
    # 递归排序并合并结果
    return quicksort_simple(left) + middle + quicksort_simple(right)


def quicksort(arr):
    """
    Quicksort algorithm implementation with in-place sorting (Lomuto partition).
    
    Args:
        arr: List of comparable elements to be sorted
        
    Returns:
        List: Sorted list in ascending order
    """
    if len(arr) <= 1:
        return arr
    
    # Create a copy to avoid modifying the original array
    arr_copy = arr.copy()
    _quicksort_helper(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy


def _quicksort_helper(arr, low, high):
    """
    Helper function for recursive quicksort implementation.
    
    Args:
        arr: List to be sorted
        low: Starting index
        high: Ending index
    """
    if low < high:
        # Partition the array and get pivot index
        pivot_index = partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        _quicksort_helper(arr, low, pivot_index - 1)
        _quicksort_helper(arr, pivot_index + 1, high)


def partition(arr, low, high):
    """
    Partition function using last element as pivot (Lomuto partition scheme).
    
    Args:
        arr: List to be partitioned
        low: Starting index
        high: Ending index
        
    Returns:
        int: Final position of pivot element
    """
    # Choose rightmost element as pivot
    pivot = arr[high]
    
    # Index of smaller element indicates right position of pivot
    i = low - 1
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort_iterative(arr):
    """
    Iterative implementation of quicksort algorithm.
    
    Args:
        arr: List of comparable elements to be sorted
        
    Returns:
        List: Sorted list in ascending order
    """
    if len(arr) <= 1:
        return arr
    
    arr_copy = arr.copy()
    stack = [(0, len(arr_copy) - 1)]
    
    while stack:
        low, high = stack.pop()
        
        if low < high:
            pivot_index = partition(arr_copy, low, high)
            
            # Push left and right subarrays to stack
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))
    
    return arr_copy


def test_quicksort():
    """测试快速排序函数"""
    # 测试用例1: 普通数组
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    expected1 = [11, 12, 22, 25, 34, 64, 90]
    result1 = quicksort_simple(arr1.copy())
    assert result1 == expected1, f"测试失败: 期望 {expected1}, 得到 {result1}"
    
    # 测试用例2: 已排序数组
    arr2 = [1, 2, 3, 4, 5]
    expected2 = [1, 2, 3, 4, 5]
    result2 = quicksort_simple(arr2.copy())
    assert result2 == expected2, f"测试失败: 期望 {expected2}, 得到 {result2}"
    
    # 测试用例3: 逆序数组
    arr3 = [5, 4, 3, 2, 1]
    expected3 = [1, 2, 3, 4, 5]
    result3 = quicksort_simple(arr3.copy())
    assert result3 == expected3, f"测试失败: 期望 {expected3}, 得到 {result3}"
    
    # 测试用例4: 包含重复元素
    arr4 = [3, 7, 3, 1, 7, 2]
    expected4 = [1, 2, 3, 3, 7, 7]
    result4 = quicksort_simple(arr4.copy())
    assert result4 == expected4, f"测试失败: 期望 {expected4}, 得到 {result4}"
    
    # 测试用例5: 空数组
    arr5 = []
    expected5 = []
    result5 = quicksort_simple(arr5.copy())
    assert result5 == expected5, f"测试失败: 期望 {expected5}, 得到 {result5}"
    
    # 测试用例6: 单个元素
    arr6 = [42]
    expected6 = [42]
    result6 = quicksort_simple(arr6.copy())
    assert result6 == expected6, f"测试失败: 期望 {expected6}, 得到 {result6}"
    
    print("所有测试用例都通过了!")


if __name__ == "__main__":
    print("=== 快速排序算法演示 ===")
    # 中文版本示例用法
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", sample_array)
    
    sorted_array = quicksort_simple(sample_array.copy())
    print("排序后数组:", sorted_array)
    
    print("\n运行中文版测试用例:")
    test_quicksort()
    
    print("\n=== English Quicksort Algorithm Test Results ===")
    print("=" * 60)
    
    # Test cases for English version
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [],
        [3, 3, 3, 3],
        [9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]
    
    for i, arr in enumerate(test_arrays, 1):
        original = arr.copy()
        sorted_recursive = quicksort(arr)
        sorted_iterative = quicksort_iterative(arr)
        
        print(f"Test {i}:")
        print(f"Original:  {original}")
        print(f"Recursive: {sorted_recursive}")
        print(f"Iterative: {sorted_iterative}")
        print(f"Correct:   {sorted_recursive == sorted(original)}")
        print("-" * 40)
