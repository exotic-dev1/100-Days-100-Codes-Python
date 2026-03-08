"""
Day 08 :- GCD AND LCM
Difficulty :- Easy
Concepts :- while loop, conditional statements, Dvisibility

Approach
1. Take input a and b 
2. Handle edge cases
3. if a and b both are zero then gcd and lcm are not defined
4. if either a or b one of them is zero then :
   GCD = max(a,b)
   LCM = min(a,b)
5. Calculate the gcd by using while loop
6. Calculate the LCM (lcm = a*b//gcd)
7. Display the results
"""
a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))
n = min(a,b)
p = max(a,b)
if (a == 0 and b == 0):
    print("GCD of",a,"and",b,"is not defined")
    print("LCM of",a,"and",b,"is not defined")
elif (a == 0 or b == 0):
    print("GCD: ",p)
    print("LCM: ",n)
else :
    while n > 1:
        if(a%n == 0 and b%n == 0):
             break
        n -= 1
    print("GCD of", a, "and", b, "is:", n)
# LCM
LCM = a * b// n
print("LCM of a and b is:", LCM)
    
     
    

    