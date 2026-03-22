"""
Day22:- Stack Operations
Difficulty:- Medium
Concept:- Stack, Lists, Loop, Conditional Statements

Approach:
1. Create stack list
2. Use while loop and create menu
3. Imput the choice from user
4. Use Else-if and define each operations
5. Execute the program
"""
stack = []
while True:
    print("\nStack Operations\n")
    print("1.PUSH")
    print("2.POP")
    print("3.PEEK")
    print("4.DISPLAY")
    
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        val = int(input("Enter value: "))
        stack.append(val)

    elif choice == 2:
        if len(stack) == 0:
            print("Stack Underflow")
        else:
            print("Popped:", stack.pop())

    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:", stack[-1])

    elif choice == 4:
        print("Stack:", stack)

    elif choice == 5:
        break
    else:
        print("Invalid choice")
