"""
Day42 :- Product except self
Difficulty :- Medium
Concepts :- prefix, suffix, loops

Approach:-
1. define the functions 
2. use prefix and suffix
3. left pass - prefix
4. right pass - suffix
5. Display the result
"""
def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
        
    postfix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
        
    return result
    
nums = list(map(int, input("Enter the nummbers: ").split()))
print(product_except_self(nums))

