"""
Day25 :- Factorial using Recursion
Difficulty :- Easy
Concepts :- recursion, base case, function calls

Approach:
1. Take input for the factorial
2. define factorial function 
3. Set base case for the recursion
4. Display the result
"""
n = int(input("Enter the number: "))
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)
print("The factorial of the",n,"is", factorial(n))