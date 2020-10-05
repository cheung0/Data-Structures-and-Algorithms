'''
time: O(N)
space: O(1)
'''
def binary_search_iterative(array, left, right, target):
    while left <= right:
        middle = (left + right) // 2

        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    
    return -1


'''
time: O(N)
space: O(log N) because of stack space
'''
def binary_search_recursive(array, left, right, target):
    if left <= right:
        middle = (left + right) // 2

        if array[middle] == target:
            return middle
        elif array[middle] < target:
            return binary_search_recursive(array, middle + 1, right, target)
        else:
            return binary_search_recursive(array, left, middle - 1, target)
    else:
        return -1
