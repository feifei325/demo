def bubble_sort(arr):
    """
    冒泡排序算法实现
    
    Args:
        arr (list): 待排序的列表
    
    Returns:
        list: 排序后的列表
    
    Example:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    n = len(arr)
    
    # 遍历所有数组元素
    for i in range(n):
        # 最后i个元素已经排好序了
        swapped = False
        for j in range(0, n-i-1):
            # 如果当前元素比下一个元素大，则交换它们
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # 如果没有发生交换，说明数组已经排好序了
        if not swapped:
            break
    
    return arr


def test_bubble_sort():
    """测试冒泡排序函数"""
    # 测试用例1: 普通数组
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    expected1 = [11, 12, 22, 25, 34, 64, 90]
    result1 = bubble_sort(arr1.copy())
    assert result1 == expected1, f"测试失败: 期望 {expected1}, 得到 {result1}"
    
    # 测试用例2: 已排序数组
    arr2 = [1, 2, 3, 4, 5]
    expected2 = [1, 2, 3, 4, 5]
    result2 = bubble_sort(arr2.copy())
    assert result2 == expected2, f"测试失败: 期望 {expected2}, 得到 {result2}"
    
    # 测试用例3: 逆序数组
    arr3 = [5, 4, 3, 2, 1]
    expected3 = [1, 2, 3, 4, 5]
    result3 = bubble_sort(arr3.copy())
    assert result3 == expected3, f"测试失败: 期望 {expected3}, 得到 {result3}"
    
    # 测试用例4: 包含重复元素
    arr4 = [3, 7, 3, 1, 7, 2]
    expected4 = [1, 2, 3, 3, 7, 7]
    result4 = bubble_sort(arr4.copy())
    assert result4 == expected4, f"测试失败: 期望 {expected4}, 得到 {result4}"
    
    # 测试用例5: 空数组
    arr5 = []
    expected5 = []
    result5 = bubble_sort(arr5.copy())
    assert result5 == expected5, f"测试失败: 期望 {expected5}, 得到 {result5}"
    
    # 测试用例6: 单个元素
    arr6 = [42]
    expected6 = [42]
    result6 = bubble_sort(arr6.copy())
    assert result6 == expected6, f"测试失败: 期望 {expected6}, 得到 {result6}"
    
    print("所有测试用例都通过了!")


if __name__ == "__main__":
    # 示例用法
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", sample_array)
    
    sorted_array = bubble_sort(sample_array.copy())
    print("排序后数组:", sorted_array)
    
    print("\n运行测试用例:")
    test_bubble_sort()