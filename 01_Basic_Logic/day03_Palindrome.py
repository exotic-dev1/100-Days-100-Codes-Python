"""
Day 03 :- Palindrome Checker For any String
Difficulty :- Easy
Concepts :- Normalizing, Trimming of a string and Slicing

Approach :- 
1. Input the ogrignal String from the user
2. Start Normalizing
3. Lowercase all the string (.lower())
4. Trim :- Remove any spaces from both sides of the string(.strip())
5. Remove any space in between of string (.replace(" ",""))
6. Reverse the normalized string using slicing [ : : -1]
7. Check Whether the normalized and reversed strings are equal or not
"""
n = str(input("Enter the srting:"))
normalized_str = n.lower().strip().replace(" ","")
reversed_str = normalized_str[ : : -1]
print("The original String:", n)
print("Normalized String:",normalized_str)
print("Reversed String :", reversed_str)
if reversed_str == normalized_str:
   print("yes it is a palindrome")
else:
   print("The given string is not a palindrome")