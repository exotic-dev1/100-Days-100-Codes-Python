"""
Day11 :- Finding Second Largest Number
Difficulty :- Easy
Concepts :- lists, Loops, Conditional Statements, list traversal

Approach :-
1. Take input 
2. Remove the duplicates from the list
3. Sort the list in ascending order
4. Print the largest and second largest number
"""
n = input("Enter the List of Numbers:")
original_list = n.split()
unique_list = []
for ch in original_list:
    if ch not in unique_list:
        unique_list.append(ch)
print(unique_list)

unique_list.sort()
print(unique_list)
largest = max(unique_list)
print("The Largest Number is:", largest)
second_largest = unique_list[-2]
print("The Second largest number:", second_largest)

