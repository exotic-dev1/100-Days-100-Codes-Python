"""
Day14 :- Matrix Addition
Difficulty :- Easy
Concepts :- nested loops, lists, 2D lists

Approach:
1. Define a function to take input of matrices
2. Use nested loops inside the function and aapend the elements inputed by the user
3. Take input for the number of rows and columns
4. call the function and create two matrices
5. Now using loops again add the matrices and append the result in a new matix
6. Display the resulting matrix
7. Use the nesting of the loops carefully
"""
def input_matrix(rows, columns):
    matrix = []
    for i in range (rows):
        row = []
        for j in range (columns):
            element = int(input("Enter the elemnets: "))
            row.append(element)
        matrix.append(row)
            
    return matrix
    
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

print("Enter the elements of matrix 01: ")
matrix_01 = input_matrix(rows, columns)
print("Enter the elements of matrix 02: ")
matrix_02 = input_matrix(rows, columns)

result = []
for i in range (rows):
    row = []
    for j in range (columns):
        row.append(matrix_01[i][j] + matrix_02[i][j])
    result.append(row)
print("Result matrix is: ")
print(result)
        