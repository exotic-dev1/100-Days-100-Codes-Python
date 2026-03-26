"""
Day26 :- Sum of Digits using Recursion
Difficulty :- Easy
Concepts :- recursion, base case, modulus, division

Aproach:
1. Take input of the number
2. Define recursion function for addition
3. Use base case, if the number become single digit return the return number
4. Else use the logic of sum of digit and return the sum of all digit
5. Display the result
"""
n = int(input("Enter the number: "))

def addition(n):
    if n < 10:
        return n
    else:
        last_digit = n%10
        remaining_number = n//10
        return last_digit + addition(remaining_number)
        
        
print("The sum of digits is :", addition(n))