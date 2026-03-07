"""
Day 07 :- Fibonacci series
Difficulty :- Easy
Concepts :- Loop, conditonal statements

Approach :-
1. Take the input
2. intialize a = first number, b = second number of fibonacci sequence
3. Handle the edge cases and negative values
4. Before using the loop keep in mind to print first and second numbers
5. Implement the loop carefully
"""
n = int(input("Enter the number:"))
a = 0
b = 1

if n <= 0:
    print("Please enter a positive number")
elif n == 1:
    print(a)
else :
    print(a)
    print(b)
    for i in range (2, n):
        next_num = a+b
        print(next_num)
        a = b
        b = next_num
      
    