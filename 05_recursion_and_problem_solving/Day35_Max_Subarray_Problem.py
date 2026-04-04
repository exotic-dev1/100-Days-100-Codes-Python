"""
Day35 : Maximum Sub array Problem (kadane's Algorithm)
Difficulty :- Medium
Concept :- loops, list manipulation

Approach:-
1. Define function
2. Maintain max sum and current sum
3. Start from first element
4. use for loop and keep updating current sum
5. Also track the max sum
6. Input the number list
7. Call the function and display the result
"""
def kadane(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    
    for i in range (1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        
        max_sum = max(max_sum, current_sum)
        
    return max_sum
    
nums = list(map(int, input("Enter Elements: ").split()))
print("Maximum Subarray Sum:",kadane(nums))
        