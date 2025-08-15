def quicksort(arr):
    """
    快速排序算法实现
    
    Args:
        arr (list): 待排序的列表
    
    Returns:
        list: 排序后的列表
    
    Example:
        >>> quicksort([64, 34, 25, 12, 22, 11, 90])
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
    return quicksort(left) + middle + quicksort(right)


def test_quicksort():
    """测试快速排序函数"""
    # 测试用例1: 普通数组
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    expected1 = [11, 12, 22, 25, 34, 64, 90]
    result1 = quicksort(arr1.copy())
    assert result1 == expected1, f"测试失败: 期望 {expected1}, 得到 {result1}"
    
    # 测试用例2: 已排序数组
    arr2 = [1, 2, 3, 4, 5]
    expected2 = [1, 2, 3, 4, 5]
    result2 = quicksort(arr2.copy())
    assert result2 == expected2, f"测试失败: 期望 {expected2}, 得到 {result2}"
    
    # 测试用例3: 逆序数组
    arr3 = [5, 4, 3, 2, 1]
    expected3 = [1, 2, 3, 4, 5]
    result3 = quicksort(arr3.copy())
    assert result3 == expected3, f"测试失败: 期望 {expected3}, 得到 {result3}"
    
    # 测试用例4: 包含重复元素
    arr4 = [3, 7, 3, 1, 7, 2]
    expected4 = [1, 2, 3, 3, 7, 7]
    result4 = quicksort(arr4.copy())
    assert result4 == expected4, f"测试失败: 期望 {expected4}, 得到 {result4}"
    
    # 测试用例5: 空数组
    arr5 = []
    expected5 = []
    result5 = quicksort(arr5.copy())
    assert result5 == expected5, f"测试失败: 期望 {expected5}, 得到 {result5}"
    
    # 测试用例6: 单个元素
    arr6 = [42]
    expected6 = [42]
    result6 = quicksort(arr6.copy())
    assert result6 == expected6, f"测试失败: 期望 {expected6}, 得到 {result6}"
    
    print("所有测试用例都通过了!")


if __name__ == "__main__":
    # 示例用法
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", sample_array)
    
    sorted_array = quicksort(sample_array.copy())
    print("排序后数组:", sorted_array)
    
    print("\n运行测试用例:")
    test_quicksort()