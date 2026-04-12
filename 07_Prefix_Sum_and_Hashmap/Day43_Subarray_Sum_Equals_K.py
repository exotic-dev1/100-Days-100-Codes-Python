"""
Day43 :- Subarray Sum Equals K
Difficulty :- Medium
Concepts :- prefix sum, hashmap

Approach:-
1. Define the subbarray_sum
2. Keep running sum
3. Check current sum = current_sum-K
4. If seen before → count increases
5. Display the result
"""
def subarray_Sum(nums, k):
    count = 0
    prefix_sum = 0
    prefix_map = {0: 1}

    for num in nums:
        prefix_sum += num

        if prefix_sum - k in prefix_map:
            count += prefix_map[prefix_sum - k]

        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

    return count
    
nums = list(map(int, input("Enter the nummbers: ").split()))
k = int(input("Enter value of K: "))
print(subarray_Sum(nums, k))