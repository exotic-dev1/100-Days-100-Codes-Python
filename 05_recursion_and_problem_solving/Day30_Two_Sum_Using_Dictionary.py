"""
Day31 :- Two Sum (Optimized)
Difficulty :- Medium
Concepts :- dictionary (hashmap), lookup, optimization

Approach:
1. Define the function for two_sum with, n and target 
2. create a empyt dictionary
3. Traverse through the list
4. then needed = target - num
4. use if needed in d return value 
5. close the function
6. input the list
7. input the target
8. display the result
"""
def two_sum(n, target):
    d = {} 

    for i, num in enumerate(n):  
        needed = target - num       

        if needed in d:          
            return [d[needed], i] 
        
        d[num] = i             
        
    return None  
    
n = list(map(int, input("Enter the list: ").split()))

target = int(input("Enter the target: "))

print (two_sum(n, target))