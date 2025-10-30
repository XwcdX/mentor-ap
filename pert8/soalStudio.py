from function import *

n = int(input('n = '))
matrix =editMatrix(makeMatrix(n))

for i in range(1, n-1):
    for j in range(1, n-1):
        if i == 1 or i == n-2 or j == 1 or j == n-2:
            if i == j == 1:
                matrix[i][j] += matrix[i-1][j] + matrix[i][j-1] + matrix[i-1][j-1]
            elif i == 1 and j == n-2:
                matrix[i][j] += matrix[i-1][j] + matrix[i][j+1] + matrix[i-1][j+1]
            elif i == j == n-2:
                matrix[i][j] += matrix[i+1][j] + matrix[i][j+1] + matrix[i+1][j+1]
            elif j == 1 and i == n-2:
                matrix[i][j] += matrix[i+1][j] + matrix[i][j-1] + matrix[i+1][j-1]
            elif i == 1 and j < n-2:
                matrix[i][j] += matrix[i-1][j]
            elif j == n-2 and i < n-2:
                matrix[i][j] += matrix[i][j+1]
            elif j == 1 and i < n-2:
                matrix[i][j] += matrix[i][j-1]
            else:
                matrix[i][j] += matrix[i+1][j]
        else:
            print(matrix[i][j], end=' ')
            continue
        print(matrix[i][j], end=' ')
    print()