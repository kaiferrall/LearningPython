#Pass in the row and column sizes as i, as well as the matrix
def determinant(i, matrix):
    det = 0
    #Make sure the matrix is square at every row
    for i in range(0, len(matrix)):
        if (matrix[i] != len(matrix) | i != len(matrix[i])):
            return  "Not square \n"
    #Return determinant when it is 2 by 2
    if (i == 2):
        det = (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
        return det
    #Loop through each column, create a copy and recursively
    #calculate the determinant of that new matrix
    else:
        for a in range(0, i):
            copy_matrix = [[0 for i in range(i-1)] for j in range(i-1)]
            for p in range(1, i):
                for q in range(0, i):
                    if q != a:
                        if q > a:
                            copy_matrix[p-1][q-1] = matrix[p][q]
                        else:
                            copy_matrix[p-1][q] = matrix[p][q]
            if a % 2 == 0:
                det = det + (matrix[0][a] * determinant(i-1, copy_matrix))
            else:
                det = det -  (matrix[0][a] *determinant(i-1, copy_matrix))
    return det
