"""
Day27 :- Power Function using Recursion
Difficulty :- Easy
Concepts :- recursion, base case, exponentiation

Approach:
1. Take input of the number and the power
2. define function use base case
3. Display the result
"""
a = int(input("Enter the number:"))
b = int(input("Enter the power:"))

def exponent(a,b):
        if b == 0:
            return 1
        else:
            return a* exponent(a, b-1)
print("The Calculated Power is:",exponent(a,b))