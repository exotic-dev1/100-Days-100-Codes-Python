"""
Day39 :- Longest Repeating Character Replacement using python
Difficulty :- Medium
Concepts :- sliding window, dictionary, two pointers

Approach:-
1. Take input string and value of k
2. define replacement function
3. Use dictionary for frequency
4. Track max frequency
5. Expand window and If invalid → shrink
6. Track max length
7. Call the function then display the result
"""
n = input("Enter the string:")
n = n.replace(" ","")
k = int(input("Enter the value of K:"))
def character_replacement(n: str, k: int) -> int:
    freq = {}
    left = 0
    max_freq = 0
    max_length = 0

    for right in range(len(n)):
        char = n[right]
        freq[char] = freq.get(char, 0) + 1
        
        max_freq = max(max_freq, freq[char])

        
        while (right - left + 1) - max_freq > k:
            freq[n[left]] -= 1
            left += 1

        
        max_length = max(max_length, right - left + 1)

    return max_length
    

print(character_replacement(n, k))