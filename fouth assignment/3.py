def transpose(matrix,n):
    transpose_matrix=[[0 for i in range(n)]for i in range(n)]
    for i in range(n):
        for j in range(n):
            transpose_matrix[j][i]=matrix[i][j]

    return transpose_matrix


value=transpose([[1,2,3],[4,5,6],[7,8,9]],3)
print(value)




