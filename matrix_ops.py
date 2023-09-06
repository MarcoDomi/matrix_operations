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

#time complexity: O(n*m*j) 
#n = num of rows in matrix1
#m = num of col in matrix2
#j = num of col in matrix1 OR num of rows in matrix2 represents number of multiplication and addition operations performed
#          **matrix1 col and matrix2 rows are equal
def matrix_multiplication(matrix1, matrix2) -> list:
    '''multiply two matrices'''
    #must be equal
    matrix1_col = len(matrix1[0]) 
    matrix2_row = len(matrix2)

    #determins the dimensions of result matrix
    matrix1_row = len(matrix1)
    matrix2_col = len(matrix2[0])

    assert matrix1_col == matrix2_row, "matrix 1 columns must equal matrix 2 rows"

    new_matrix_dimension = matrix1_col
    new_matrix = []

    for row in range(matrix1_row):
        temp_list = []
        for col in range(matrix2_col):
            sum = 0
            for elem in range(new_matrix_dimension):
                sum += matrix1[row][elem] * matrix2[elem][col] 
            temp_list += [sum]
        new_matrix += [temp_list]
        
        if matrix1_row == 1:
            new_matrix = new_matrix[0]

    #if matrix_1 is n X m and matrix_2 is m X 1 then new_matrix will be n X 1
    return new_matrix


def print_matrix(matrix) -> None:
    for row in matrix:
        print(row)


mat1 = [[23,1],[4, 3]]
mat2 = [[4,5,39],[12, 79, 17]]

sum = matrix_addition(mat1, mat2)
matrix_T = matrix_transpose(mat1)
product_matrix = matrix_multiplication(mat1, mat2)
print(product_matrix)