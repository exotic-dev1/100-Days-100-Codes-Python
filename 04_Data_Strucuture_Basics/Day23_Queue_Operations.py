"""
Day23:- Queue Operations
Difficulty:- Medium
Concept:- Queue, Lists, Loop, Conditional Statements

Approach:
1. Create a Queue using list
2. Use while loop and create menu
3. Input the choice from user
4. Use Else-if and define each operations:- enqueue, dequeue, display and front
5. Execute the program
"""
Queue = []
while True:
    print("\nQueue Operations\n")
    print("1.ENQUEUE")
    print("2.DEQUEUE")
    print("3.FRONT")
    print("4.DISPLAY")
    print("5.EXIT")
    
    choice = int(input("Enter the choice:"))
    if choice == 1:
        val = int(input("Enter value: "))
        Queue.append(val)

    elif choice == 2:
        if len(Queue) == 0:
            print("Empty Queue")
        else:
            print("Dequeue:", Queue.pop(0))

    elif choice == 3:
        if len(Queue) == 0:
            print("Queue is empty")
        else:
            print("Front element:", Queue[0])

    elif choice == 4:
        print("Queue:", Queue)

    elif choice == 5:
        break
    else:
        print("Invalid choice")
        