"""
Day24 :- Valid Parentheses
Difficulty :- Medium
Concepts :- stack, strings, condition checking

Approach:- 
1. Take input string of parenthesis
2. create an empty stack
3. create a list for open_brackets and a list for their pairs
4. traverse through each charater of the string
5. check characters in open_brackets if yes push them to the stack
6. now check char in pairs if stack top is equal to 0 print invalid
7. check the matching condition if top != pairs print invalid
8. else pop the element then check if stack became empty print valid else invalid
9. Display the result
"""
n = input("Enter the parenthesis:")
stack = []
open_brackets = {'(','{','['}
pairs = {')': '(', '}': '{', ']': '['}

for char in n:
    if char in open_brackets:
        stack.append(char)
    elif char in pairs:
        
        if len(stack) == 0:
            print("Invalid")
            break
        if stack[-1] != pairs[char]:
            print("Invalid")
            break
        stack.pop()
else:
    if len(stack) == 0:
        print("Valid")
    else:
        print("Invalid")
        
            