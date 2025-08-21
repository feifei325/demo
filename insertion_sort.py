def insertion_sort(arr):
    """
    Insertion sort algorithm implementation.
    
    Args:
        arr (list): List of comparable elements to sort
    
    Returns:
        list: Sorted list in ascending order
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
    """Test cases for insertion sort algorithm"""
    test_cases = [
        ([], []),
        ([1], [1]),
        ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([2, 2, 2, 2], [2, 2, 2, 2]),
        ([-1, 0, -5, 3, 2], [-5, -1, 0, 2, 3])
    ]
    
    for i, (input_list, expected) in enumerate(test_cases):
        result = insertion_sort(input_list.copy())
        assert result == expected, f"Test case {i+1} failed: {result} != {expected}"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_insertion_sort()
    
    sample_data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {sample_data}")
    sorted_data = insertion_sort(sample_data.copy())
    print(f"Sorted array: {sorted_data}")