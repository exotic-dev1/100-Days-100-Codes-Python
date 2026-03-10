"""
Day10 :- Removing duplicates from a list
Difficulty :- Easy
Concepts :- lists, Loops, Conditional Statements, list traversal

Approach :-
1. Take input
2. convert that into list
3. create an empty list which will contain all unique values
4. Traverse through the original list using for loop
5. check if element not present in unique_list append it
6. Display the unique list
"""
n = input("Enter the list:")
original_list = n.split()
unique_list = []
for ch in original_list:
    if ch not in unique_list:
        unique_list.append(ch)
print("Unique list:", unique_list)