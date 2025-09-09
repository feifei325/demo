def quick_sort(arr):
    """
    快速排序算法实现
    
    Args:
        arr: 待排序的列表
    
    Returns:
        排序后的列表
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
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr, low=0, high=None):
    """
    原地快速排序算法实现（更节省空间）
    
    Args:
        arr: 待排序的列表
        low: 排序范围的起始索引
        high: 排序范围的结束索引
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # 分区操作，返回基准元素的正确位置
        pivot_index = partition(arr, low, high)
        
        # 递归排序基准元素左右两部分
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)


def partition(arr, low, high):
    """
    分区函数，将数组分为两部分
    
    Args:
        arr: 数组
        low: 起始索引
        high: 结束索引
    
    Returns:
        基准元素的最终位置
    """
    # 选择最后一个元素作为基准
    pivot = arr[high]
    
    # 较小元素的索引
    i = low - 1
    
    for j in range(low, high):
        # 如果当前元素小于或等于基准
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # 将基准元素放到正确位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# 测试代码
if __name__ == "__main__":
    # 测试快速排序
    test_arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_arr1)
    
    sorted_arr1 = quick_sort(test_arr1.copy())
    print("快速排序结果:", sorted_arr1)
    
    # 测试原地快速排序
    test_arr2 = [64, 34, 25, 12, 22, 11, 90]
    print("\\n原始数组:", test_arr2)
    
    quick_sort_inplace(test_arr2)
    print("原地快速排序结果:", test_arr2)
    
    # 测试边界情况
    print("\\n边界情况测试:")
    print("空数组:", quick_sort([]))
    print("单元素数组:", quick_sort([1]))
    print("已排序数组:", quick_sort([1, 2, 3, 4, 5]))
    print("逆序数组:", quick_sort([5, 4, 3, 2, 1]))
    print("重复元素数组:", quick_sort([4, 2, 4, 1, 2, 3]))