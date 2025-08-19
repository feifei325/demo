def bubble_sort(arr):
    """
    冒泡排序算法实现
    
    参数:
        arr: 需要排序的列表
    
    返回:
        排序后的列表
    """
    n = len(arr)
    arr = arr.copy()
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr


def main():
    test_data = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_data)
    
    sorted_data = bubble_sort(test_data)
    print("排序后数组:", sorted_data)


if __name__ == "__main__":
    main()