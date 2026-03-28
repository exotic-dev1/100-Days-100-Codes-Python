"""
Day28 :- Reverse String using Recursion
Difficulty :- Easy
Concepts :- recursion, strings, slicing

Approach:
1. Take input string
2. Define the function
3. Enter base case if string is empty return ""
4. Call the function and include recursion logic
5. Print the result
"""
n = input("Enter the string:")

def reverse_string(n):
    if len(n)== 0:
        return ""
    else:
        return reverse_string(n[1:]) + n[0]

print("The reversed string is:",reverse_string(n))