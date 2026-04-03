"""
Day34 :- Move Zeroes to End
Difficulty :- Medium
Concepts :- two pointers, list manipulation

Approach:-
1. define the function to move zeroes
2. position pointer for next non-zero
3. Traverse the list
4. When non zero found swap it
5. Increment the position pointer
6. input the number list
7. Call the function print the result

"""
def move_zeroes(nums):
    pos = 0 

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]

            pos += 1
            

        return nums

number_list = list(map(int, input("Enter numbers: ").split()))
print(move_zeroes(number_list))