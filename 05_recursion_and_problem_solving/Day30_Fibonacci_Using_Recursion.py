"""
Day30 :- Fibonacci using Recursion
Difficulty :- Easy
Concepts :- recursion, multiple recursive calls

Aprroach:-
1. input the term 
2. Define the function
3. Handle all edge cases
4. Dsiplay the result
"""
n = int(input("Enter the term:"))

def fibonacci(n):
    
    if n == 0:
        return 0
        
    if n == 1:
        return 1
        
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
if n <= 0 :    
    
    print("Enter a positive number")
else:
    print(fibonacci(n))