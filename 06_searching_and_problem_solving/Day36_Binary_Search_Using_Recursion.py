"""
Day36 :- Binary Search (Recursive)
Difficulty :- Medium
Concepts :- recursion, divide and conquer

Approach:
1. Take sorted array input
2. Take target value
3. Define recursive function with:
low index
high index
4. Base case:
if low > high → not found
5. Find mid
6. Compare and call recursively
7. Print result

"""

def binary_search(arr, low, high, target):
    if low > high:
        return -1  
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid 
    elif arr[mid] > target:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)


arr = [2, 4, 6, 8, 10, 12, 14]
target = 10

result = binary_search(arr, 0, len(arr) - 1, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")