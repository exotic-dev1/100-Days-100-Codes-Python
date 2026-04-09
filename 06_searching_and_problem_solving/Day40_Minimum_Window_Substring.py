"""
Day40 :- Minimum Window Substring
Difficulty :- Hard
Concepts :- Advanced sliding window, dictionary,pointers, dictionary, loops, conditional statement

Approach:-
1. Take input for main string
2. Input sub string
3. Count frequency of t
4. Expand window
5. Track matched characters
6. When valid → shrink window
7. Track minimum
8. Print result
"""
n = input("Enter the main string: ")
t = input("Enter the sub string: ")
n = n.replace(" ", "")

def min_window_substring(n: str, t: str):
    if not n or not t:
        return ""
    
    needed = {}
    for ch in t:
        needed[ch] = needed.get(ch, 0) + 1
        
    have = {}
    required = len(needed)
    formed = 0
    
    l = 0
    min_len = float("inf")
    res_l = 0
    
    for r in range(len(n)):
        char = n[r]
        have[char] = have.get(char, 0) + 1
        
        if char in needed and have[char] == needed[char]:
            formed += 1
                
        while formed == required:
            if (r - l + 1) < min_len:
                min_len = r - l + 1
                res_l = l
                
            left_char = n[l]
            have[left_char] -= 1
            
            if left_char in needed and have[left_char] < needed[left_char]:
                formed -= 1
                    
            l += 1
                
    if min_len == float("inf"):
        return ""
    else:
        return n[res_l:res_l + min_len]

result = min_window_substring(n, t)
print("Minimum window substring:", result)