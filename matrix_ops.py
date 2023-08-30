
def matrix_addition(matrix1, matrix2) -> list:
    row_num = len(matrix1)
    col_num = len(matrix1[0])
    sum_mat = []
    
    for row in range(row_num):
        temp_row = []
        for col in range(col_num):
            element_sum = matrix1[row][col] + matrix2[row][col]
            temp_row += [element_sum] #use brackets so the sum gets included as an element in temp_row list
        sum_mat += [temp_row] #use brackets so the temp_row list is included as an element in sum_mat
    return sum_mat


mat1 = [[23,1,8],[40, 32, 67], [52, 15, 3]]
mat2 = [[4,5,39],[12, 79, 17], [24, 19, 7]]

sum = matrix_addition(mat1, mat2)
print(sum)