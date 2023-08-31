#NOTE e/ row of a matrix must have same number of elements
def matrix_addition(matrix1, matrix2) -> list:
    '''add elements of two matrices and return the sum matrix'''
    row_num = len(matrix1)    #get num rows
    col_num = len(matrix1[0]) #get num cols **use first row length to account for length of every row. it is assumed all rows have same num of columns
    sum_mat = []
    
    for row in range(row_num):
        temp_row = []       #used to temporarily store elements
        for col in range(col_num):
            element_sum = matrix1[row][col] + matrix2[row][col]
            temp_row += [element_sum] #use brackets so the sum gets included as an element in temp_row list
        sum_mat += [temp_row]         #use brackets so the temp_row list is included as an element in sum_mat
    return sum_mat

def matrix_transpose(matrix) -> list:
    '''return the transpose of a matrix'''
    row_num = len(matrix) 
    col_num = len(matrix[0])
    transposed_matrix = []

    for col in range(col_num):
        temp = []
        for row in range(row_num):
            temp += [matrix[row][col]] #obtain e/ element in current column and append to temp 
        transposed_matrix += [temp]    #add temp list to transposed_matrix
    
    return transposed_matrix


def print_matrix(matrix) -> None:
    for row in matrix:
        print(row)


mat1 = [[23,1,8],[40, 32, 67], [52, 15, 3]]
mat2 = [[4,5,39],[12, 79, 17], [24, 19, 7]]

sum = matrix_addition(mat1, mat2)
matrix_T = matrix_transpose(mat1)
print_matrix(mat1)
print()
print_matrix(matrix_T)