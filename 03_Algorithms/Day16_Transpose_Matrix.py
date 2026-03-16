"""
Day16 :- Transpose of a Matrix
Difficulty :- Easy
Concepts :- nested loops, 2D lists, matrix operations

Approach:
1. Take input for rows and columns
2. Input the matrix elements from the user
3. Using nested loop perform the tranpose
4. Display the result
"""
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
matrix = []
for i in range (rows):
    row = []
    for j in range (columns):
        element = int(input("Enter the elements: "))
        row.append(element)
    matrix.append(row)
print("The original matrix is: ", matrix)
transpose = []
for i in range(columns):
    row = []
    for j in range(rows):
        row.append(matrix[j][i])
    transpose.append(row)
print("Transpose", transpose)