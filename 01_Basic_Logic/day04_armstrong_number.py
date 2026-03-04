"""
Day 04 :- To determine an armstrong number
Difficulty :- Easy
Concepts :- While Loops, Digit extraction and power

Approach :- 
1. Input the ogrignal number from the user
2. Store the original number
3. Count the number of digits using a loop
4. Use another loop to calculate the armstrong number
5. Compare the original number to the total
6. Print whether the number is armstrong or not
"""
n = int(input("Enter the number :"))
original = n
temp = n
count = 0
total = 0
while temp > 0:
    count += 1
    temp = temp//10
while (n >0) :
    digit = n%10
    total = total + (digit)**count
    n = n//10
if total == original :
    print("The number is an Armstrong Number")
else:
    print("The number is not an Armstrong Number")