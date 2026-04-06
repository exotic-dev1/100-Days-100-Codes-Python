"""
Day37 :- First Non-Repeating Character
Difficulty :- Easy
Concepts :- dictionary, strings, frequency count

Approach:-
1. Input the string
2. Create a dictionary for count
3. Count Frequency
4. Loop String Again
5. Print 1st character with frequency = 1
"""
n = input("Enter the string:")
n = n.lower()
n = n.replace(" ","")
frequency_count = {}
for char in n:
    frequency_count[char] = frequency_count.get(char, 0) + 1
    
for char in n:
    if frequency_count[char] == 1:
        print ("First Non Repeating Character:",char)
        break