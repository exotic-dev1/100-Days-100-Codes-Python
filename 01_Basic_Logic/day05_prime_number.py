"""
Day 05 :- To determine Prime number
Difficulty :- Easy
Concepts :- for loop, conditional statements

Approach :- 
1. Input the ogrignal number from the user
2. Check the number if it less then one display not a prime number
3. Use For loop in range(2,n-1) to find all the divisors
4. Check if remainder of any divisor is equals to zero the nota a prime 
5. Break the Loop 
6. else the number is a prime number

"""
n = int(input("Enter the number :"))
if n <= 1:
    print("Invalid Input")
else :
    for i in range (2, n) :
        if n%i == 0:
          print("Not a prime number")
          break
    else:
          print("The number is a prime number")
            