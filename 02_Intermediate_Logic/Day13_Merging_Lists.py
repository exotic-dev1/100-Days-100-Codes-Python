"""
Day13 :- Merge two lists
Difficulty :- Easy
Concepts :- lists, loops, list traversal

Approach:
1. Input 2 lists
2. Convert both lists in integer
3. Traverse the list 01 and 02 using separate loops
4. Append the values in a sperate new list
5. Display the merged list
"""
list_01 = input("Enter list 01:").split()
list_01 = [int(x) for x in list_01]
list_02 = input("Enter list 02:").split()
list_02 = [int(x) for x in list_02]
length = len(list_01)
lengths = len(list_02)
new_list = []

for i in range (length):
    new_list.append(list_01[i])
for j in range (lengths):
    new_list.append(list_02[j])
print("The merged List is: ",new_list)