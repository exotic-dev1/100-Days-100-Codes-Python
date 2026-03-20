"""
Day19 :- Linear Search
Difficulty :- Easy
Concepts :- lists, loops, conditional statements

Approach:
1. Input the list
2. Sort the list
3. Take input of target element
4. use a flag variable to track of target element
5. use while loop, find mid using (lower+upper)//2
6. Check if target is equal to mid element print it
7. Elif Check and repeat for right and left part until you find target
"""
n = input("Enter the Unsorted list: ").split()
n = [int(x) for x in n]

# Sorting section :- Bubble Sort
length = len(n)
for i in range(length):
    for j in range(0, length - i - 1):
        if n[j] > n[j + 1]:
            temp = n[j]
            n[j] = n[j + 1]
            n[j + 1] = temp

print("Sorted list:", n)

# Searching section: Binary Search
target = int(input("Enter the target element: "))
lower = 0
upper = len(n) - 1

found = False # Flag variables

while lower <= upper:
    mid = (lower + upper) // 2
    
    if n[mid] == target:
        print("Element found at index:", mid)
        found = True
        break
    elif target > n[mid]:
        lower = mid + 1
    else:
        upper = mid - 1

if not found:
    print("Element not found")