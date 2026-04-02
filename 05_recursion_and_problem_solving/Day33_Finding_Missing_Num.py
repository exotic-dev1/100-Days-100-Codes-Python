"""
Day33 :- Find Missing Number
Difficulty :- Easy
Concepts :- math, loops, summation

Approach:- 
1. Input the number list
2. calculate the n
3. calculate the expected sum
4. initalize the actual sum = 0
5. use for loop and calculate actual sum
6. find missing num = expected - actual
7. Display the missing number
"""
number_list = list(map(int, input("Enter numbers: ").split()))
length = len(number_list)

n = length + 1

expected_sum = n * (n + 1) // 2

actual_sum = 0
for i in range(length):
    actual_sum = actual_sum + number_list[i]

missing = expected_sum - actual_sum

print("Missing number is:", missing)