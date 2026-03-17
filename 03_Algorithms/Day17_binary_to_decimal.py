"""
Day17 :- Binary to Decimal Conversion
Difficulty :- Easy
Concepts :- loops, strings, power calculation
"""
n = input("Enter the Binary number: ")
reverse = n[::-1]
power = 0
decimal = 0
for i in reverse:
    if (i == '1'):
        decimal += 1 * 2**power
    power +=1
print("The Binary Number is: ", n)
print("The Decimal number is: ",decimal)