"""
Day15 :- Matrix Multiplication
Difficulty :- Medium
Concepts :- nested loops, 2D lists, matrix operations

Approach:
1. Define a function to take input of matrices
2. Use nested loops inside the function and aapend the elements inputed by the user
3. Take input for the number of rows and columns
4. call the function and create two matrices
5. After inputting matrices now using three loops perform multiplication
6. Logic should be total += matrix_01[i][k] * matrix_02[k][j]
7. Display the resulting matrix
"""
def input_matrix(rows, columns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            element = int(input("Enter the elements: "))
            row.append(element)
        matrix.append(row)
        
    return matrix
    
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

print("Enter the elements of matrix_01: ")
matrix_01 = input_matrix(rows, columns)
print("Enter the elements of matrix_02: ")
matrix_02 = input_matrix(rows, columns)
print("First Matrix: \n",matrix_01, end = " ")
print("\nSecond Matrix: \n ", matrix_02, end = " ")

print("\nThe reultant matrix is: ")
for i in range(rows):
    for j in range(columns):
        total = 0
        for k in range(columns):
            total += matrix_01[i][k] * matrix_02[k][j]
        print(total, end= " ")
    print()