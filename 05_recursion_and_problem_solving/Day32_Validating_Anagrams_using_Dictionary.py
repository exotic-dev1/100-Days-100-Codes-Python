"""
Day32 :- Valid Anagram
Difficulty :- Easy
Concepts :- dictionary, frequency count, strings

Approach:
1. Define the function 
2. Remove spaces from both the wordsand convert them into lowercase
3. check if If lengths not equal →  return False
4. create dictionary for both strings
5. using for loop compare both
6. return dictionary_01 == dictionary_02
7. Take input for both words 
8. Call the function and display the results
"""
def anagrams(string_01, string_02):
    
    string_01 = string_01.replace(" ","").lower()
    string_02 = string_02.replace(" ","").lower()
    
    if len(string_01) != len(string_02):
        return False
        
    dictionary_01 = {}
    dictionary_02 = {}
    
    for char in string_01:
        dictionary_01[char] = dictionary_01.get(char, 0) +1
        
    for char in string_02:
        dictionary_02[char] = dictionary_02.get(char, 0) + 1
        
    return dictionary_01 == dictionary_02
    
string_01 = input("Enter the string 01:")
string_02 = input("Enter the string 02:")

if anagrams(string_01, string_02):
    print(string_01,"and",string_02,"are anagrams")
    
else:
    print(string_01,"and",string_02,"are not anagrams")