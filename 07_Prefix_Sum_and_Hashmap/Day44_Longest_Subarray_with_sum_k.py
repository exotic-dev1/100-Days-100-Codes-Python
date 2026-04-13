"""
Day44 :- Longest Subarray with Sum K
Difficulty :- Medium
Concepts :- prefix sum, hashmap

Approach:
1. Define the function longest subarray with sum k
2. map to store prefix sum: first index
3. if (prefix_sum - k) exists:
    length = current_index - stored_index
4. check all the edge cases
5. Display the result
"""
def longest_subarray_with_sum_k(arr, k):
    
    prefix_map = {}
    current_sum = 0
    max_length = 0

    for i, num in enumerate(arr):
        current_sum += num

        
        if current_sum == k:
            max_length = i + 1

        rem = current_sum - k
        if rem in prefix_map:
            max_length = max(max_length, i - prefix_map[rem])

        if current_sum not in prefix_map:
            prefix_map[current_sum] = i

    return max_length

arr = list(map(int, input("Enter the numbers: ").split()))
k = int(input("Enter value of K: "))
print(longest_subarray_with_sum_k(arr, k)) 
