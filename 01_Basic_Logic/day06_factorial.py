"""
Day 06 :- Factorial of a number'
Difficulty :- Easy
Concepts :- for loop, conditional statements

Approach
1. Take input 
2. Validate the input if negative print "invalid input"
3. If input is 0 then 0! = 1
4. Use for loop from 1 to n 
5. result = result*i
6. Print the factorial
"""
n = int(input("Enter the number:"))
result = 1
if n < 0:
    print("Factorial of a negative number does not exist")
elif n == 0:
    print("Factorial = 1")
else :
    for i in range (1, n+1):
        result = result * i
print("The factorial of the number is:", result)
        