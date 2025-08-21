def insertion_sort(arr):
    """
    插入排序算法实现
    
    参数:
        arr: 待排序的列表
    
    返回:
        排序后的列表
    """
    if not arr:
        return arr
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr


def test_insertion_sort():
    """测试插入排序算法"""
    test_cases = [
        ([], []),
        ([1], [1]),
        ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([2, 2, 2, 2], [2, 2, 2, 2])
    ]
    
    for i, (input_arr, expected) in enumerate(test_cases):
        result = insertion_sort(input_arr.copy())
        assert result == expected, f"测试用例 {i+1} 失败: 期望 {expected}, 实际 {result}"
    
    print("所有测试用例通过！")


if __name__ == "__main__":
    test_insertion_sort()
    
    sample = [64, 34, 25, 12, 22, 11, 90]
    print(f"原始数组: {sample}")
    sorted_arr = insertion_sort(sample.copy())
    print(f"排序后数组: {sorted_arr}")