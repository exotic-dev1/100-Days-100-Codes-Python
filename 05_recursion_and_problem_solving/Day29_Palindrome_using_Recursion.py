"""
Day29 :- Palindrome Check using Recursion
Difficulty :- Easy
Concepts :- recursion, strings, slicing

Approach:
1. Take input string
2. Define the function
3. The user can add n.lower inside the function if case sensitivity needed
4. Enter base case if len(n)<= 1, return True
5. Else if s[0] != s[-1] → False ,else → check middle (s[1:-1])
6. Display the result
"""
n = input("Enter the string:")

def palindrome_checker(n):
    n = n.lower()
    n = n.replace(" ","")
    
    if len(n) <= 1:
        return True
        
    if n[0] != n[-1]:
        return False
        
    else:
        return palindrome_checker(n[1:-1])
        
print("Is palindrome:",palindrome_checker(n))