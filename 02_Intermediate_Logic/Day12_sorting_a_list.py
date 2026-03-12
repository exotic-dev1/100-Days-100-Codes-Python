"""
Day12 :- Sort a list without using built-in sort
Difficulty :- Easy
Concepts :- lists, nested loops, swapping

Approach :-
1. Take input as list
2. Convert it into integer
3. create a temp variable
4. Use first loop to traverse the list
5. Second loop to compare and the sort the list
6. compare and swap the elements
7. print the sorted list
"""
n = input("Enter the Unsorted list:").split()
n = [int(x) for x in n]
length = len(n)
temp = 0
for i in range (length):
    for j in range(0,length-i-1):
        a = n[j]
        b = n[j+1]
        if a > b:
            temp = a
            a = b 
            b = temp
            
            n[j] = a
            n[j+1] = b
print ("Sorted list",n)
        
    
