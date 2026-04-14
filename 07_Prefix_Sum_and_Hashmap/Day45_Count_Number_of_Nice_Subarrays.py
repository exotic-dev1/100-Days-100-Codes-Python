"""
Day45 :- Count Number of Nice Subarrays
Difficulty :- Medium
Concepts :- prefix sum, hashmap

Approach:-
1. onvert array → (odd = 1, even = 0)
2. Find subarrays with sum = k
3. Use prefix sum logic
4. Display the output
"""
def numberOfSubarrays(nums, k):
    count = 0
    prefix_sum = 0
    freq = {0: 1}

    for num in nums:
        if num % 2 == 1:
            prefix_sum += 1

        if (prefix_sum - k) in freq:
            count += freq[prefix_sum - k]

        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

    return count

nums = list(map(int, input("Enter the numbers: ").split()))

k = int(input("Enter value of K: "))
print(numberOfSubarrays(nums, k))