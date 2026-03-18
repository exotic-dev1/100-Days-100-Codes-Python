"""
Day18 :- Decimal to Binary Conversion
Difficulty :- Easy
Concepts :- loops, division, remainder, string/list reversal

Approach:
1. Take input of decimal value
2. create a list to store remainder
3. Handle the edge case if decmial = 0 then print 0
4. Also check for the negative values
5. Use while loop and logic of conversion decimal to binary
6. Store the remainder and reverse the remainder change the reverse list into a string
7. Display thr binary number
"""
decimal = int(input("Enter the decimal number:  "))
remainder = []
n = 0
if decimal == 0:
    print(0)
else:
    negative = decimal < 0
    decimal = abs(decimal)
    while decimal > 0:
        n = decimal%2
        remainder.append(n)
        decimal = decimal//2
        
    result = remainder[::-1]
    binary = "".join(map(str,result))
    if negative:
        print("The binary number is: -"+ binary)
    else:
        print("The Binary number is: ",binary)
    
    
