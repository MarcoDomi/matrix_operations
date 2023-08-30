
def matrix_addition(matrix1, matrix2) -> list:
    row_num = len(matrix1)
    col_num = len(matrix1[0])
    sum_mat = []
    
    for row in range(row_num):
        temp_row = []
        for col in range(col_num):
            element_sum = matrix1[row][col] + matrix2[row][col]
            temp_row += [element_sum] #add
        sum_mat += [temp_row]
    return sum_mat


mat1 = [[23,1,8],[40, 32, 67], [52, 15, 3]]
mat2 = [[4,5,39],[12, 79, 17], [24, 19, 7]]

sum = matrix_addition(mat1, mat2)
print(sum)