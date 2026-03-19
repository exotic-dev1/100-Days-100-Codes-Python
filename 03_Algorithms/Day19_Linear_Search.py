"""
Day19 :- Linear Search
Difficulty :- Easy
Concepts :- lists, loops, conditional statements

Approach:
1. Take input as a list then convert it to integer
2. input the target element
3. Traverse the list using loop
4. If found print index
5. else element not found
"""
n = input("Enter the list: ").split()
n= [int(x) for x in n]
length = len(n)
target = int(input("Enter the target number: "))
for i in range (length):
    if target == n[i]:
        print("The target element",target,"found at index:",[i])
        break
else:
    print(target,"Not found")
        