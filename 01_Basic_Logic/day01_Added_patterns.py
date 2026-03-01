"""
Day 01 - Added Pattern Ptoblem
Difficulty: Moderate
Concepts: Loops, Else-IF, Nested loops, Methods

Approach:
1. Create a method for each pattern(Triangle, Pyramid, Inverted_pyrramid)
2. Build Logic for each patterns using loops carefully
3. Create Menu for the patterns using Else-if
4. Call the methods carefully.
5. Check and do the intendation carefully
"""
def triangle(n):
    for i in range(1, n):
        for j in range(i):
            print("*", end="")
        print()
        
def pyramid(n):
    for i in range(1, n+1):
        for j in range(n - i):
            print(" ", end = "")
        for j in range(2 * i - 1):
            print("*", end = "")
        print()
        
def inverted(n):
    for i in range(1, n+1):
        for j in range(i-1):
            print(" ", end="")
        for j in range(2*(n-i)+1):
            print("*", end="")
        print()
        
while True:
    print("Menu")
    print("1.Triangle")
    print("2.Pyramid")
    print("3.Inverted Pyramid")
    print("4.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        n = int(input("No. of Rows: "))
        triangle(n)
    elif choice == 2:
         n = int(input("No. of Rows: "))
         pyramid(n)
         
    elif choice == 3:
              n = int(input("No. of Rows: "))
              inverted(n)
    elif choice == 4:
        print("exiting")
        break
    else:
        print("Invalid choice")