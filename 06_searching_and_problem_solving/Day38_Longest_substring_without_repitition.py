"""
Day38 :- Longest Substring Without Repeating Characters
Difficulty :- Medium
Concepts :- sliding window, set, two pointers

Approach:-
1. Input the string
2. set() to track characters
3. Initailize left and right pointer
4. Main Logic
for right in range:
    if char not in set:
        add → update max length
    else:
        remove from left until valid
5. Return max length
6. Dsiplay the output
"""
n = input("Enter the string:")
n = n.lower()
n = n.replace(" ","")

def longest_substring(n: str) -> int:
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(n)):
        
        while n[right] in char_set:
            char_set.remove(n[left])
            left += 1

        char_set.add(n[right])
        max_length = max(max_length, right - left + 1)

    return max_length


print(longest_substring(n))