"""
Day 02 :- Reversing a Number
Difficulty :- Very Easy
Concepts :- While Loops, Reversal Logic

Approach :- 
1. Input the ogrignal number from the user
2. Initalize reversednumber = 0
3. Solve the edge case problem for negatvie integer by storingg sign separatly
4. Use while loop with condition (n > 0)
5. Now apply the logic for reversing
6. Print reversed_num
"""
n = int(input("Enter the number:"))

if n < 0:
    negative = True
    n = abs(n)
else:
    negative = False
reversed_num = 0
while(n > 0):
    digit = n%10
    reversed_num = (reversed_num * 10) + digit
    n = n //10
if negative:
    reversed_num = -reversed_num
       
print(reversed_num)
     