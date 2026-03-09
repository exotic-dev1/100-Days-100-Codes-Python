"""
Day09 :- Counting Vowels, Consonants and digits
Difficulty :- Easy
Concepts :- Loops, Conditional Statements, String traversal

Approach :-
1. Take input
2. intialise counters for vowels, consonants and digits
3. Use for loop and traverse each character of the string one by one
4. Check for digits using (ch.isdigit()), incremenet the counter if true
5. Check for vowels and convert the string into lowercase to avoid any problems
6. Check for consonants usinf (ch.isalpha())
7. Print the Results
"""
n = str(input("Enter The String:"))
digits = 0
vowels = 0
consonant = 0
for ch in n:
    if ch.isdigit():
        digits += 1
    elif ch.lower() in "aeiou" :
        vowels += 1
    elif ch.isalpha() :
        consonant += 1
    
print("consonants:", consonant)
print("vowels:", vowels)
print("digits:", digits)
    
    
    