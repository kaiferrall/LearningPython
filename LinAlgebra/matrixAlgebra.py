# INCLUDES some other general helpers like dot product


def dotProduct(vector_a, vector_b):
    if len(vector_a) != len(vector_b):
        return "ERROR: Size must match"
    else:
        val = 0
        for i in range(len(vector_a)):
            val += vector_a[i]*vector_b[i]
        return val

# THINK of better way to do this (for not N^2)


def multiplication(matrix_a, matrix_b):
    if type(matrix_a[0]) is int and type(matrix_b[0]) is int:
        if (len(matrix_a) == len(matrix_b)):
            val = 0
            for i in range(len(matrix_a)):
                val += matrix_a[i]*matrix_b[i]
            return val
        else:
            return "ERROR: Incorrect dimensions of vectors"
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)

    if cols_a != rows_b:
        return "rows of B must match columns of a A"

    cols_b = len(matrix_b[0])
    rows_a = len(matrix_a)

    resultant = [[None for cols in range(cols_b)]
                 for rows in range(rows_a)]

    for i in range(cols_b):
        for j in range(rows_a):
            # Find better way to iterate through for this
            vector_b = [matrix_b[j2][i] for j2 in range(rows_b)]
            vector_a = matrix_a[j]
            val = multiplication(vector_a, vector_b)
            resultant[j][i] = val
    return resultant


test1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
test2 = [[1, 1], [2, 2], [3, 4]]
test3 = [1, 1, 1, 1]
test4 = [2, 2, 2, 2]
AB = multiplication(test1, test2)
print(AB)
