"""
Day41 :- Longest Consecutive Sequence
Difficulty :- Medium
Concepts :- set, loops, optimization

Approach:-
1. Input the list
2. Convert it into set
3. Only start when:
4. num - 1 not in set
5. Expand forward using while loop
6. Display the result
"""
n = list(map(int, input("Enter the list: ").split()))
n_set = set(n)
longest = 0
for n in n_set:
    
    if n - 1 not in n_set:
            current = n
            length = 1


            while current + 1 in n_set:
                current += 1
                length += 1

            longest = max(longest, length)

print("Length of longest consecutive sequence is:",longest)