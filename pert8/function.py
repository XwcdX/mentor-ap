import math

def makeMatrix(x, y=math.inf):
    if y != math.inf:
        return [[0 for _ in range(x)] for _ in range(y)]
    return [[0 for _ in range(x)] for _ in range(x)]

def printMatrix(list2d):
    for i in list2d:
        for j in i:
            print(j, end=' ')
        print()
    return

def fillDiagonal(list2d):
    if len(list2d) != len(list2d[0]):
        return
    length = len(list2d)
    for i in range(length):
        list2d[i][i] = 1
    return list2d

def editMatrix(list2d):
    length = len(list2d)
    for i in range(length):
        list2d[i] = list(map(int, input().split(' ')))
    #validasi
    for i in list2d:
      if len(i) != length:
          return fillDiagonal(makeMatrix(length))
    return list2d

def addition(list2d1, list2d2):
    finalMatrix = []
    if len(list2d1) == len(list2d2) or len(list2d1[0]) == len(list2d2[0]):
        length = len(list2d1)
        for i in range(length):
            row = []
            for j in range(length):
                row.append(list2d1[i][j] + list2d2[i][j])
            finalMatrix.append(row)
    return finalMatrix

def subtract(list2d1, list2d2):
    finalMatrix = []
    if len(list2d1) == len(list2d2) or len(list2d1[0]) == len(list2d2[0]):
        length = len(list2d1)
        for i in range(length):
            row = []
            for j in range(length):
                row.append(list2d1[i][j] - list2d2[i][j])
            finalMatrix.append(row)
    return finalMatrix

def multiply(list2d1, list2d2):
    finalMatrix = []
    if len(list2d1) == len(list2d2) or len(list2d1[0]) == len(list2d2[0]):
        length = len(list2d1)
        for i in range(length):
            row = []
            for j in range(length):
                allData = []
                for k in range(length):
                    allData.append(list2d1[i][k] * list2d2[k][j])
                row.append(sum(allData))
            finalMatrix.append(row)
    return finalMatrix
       
# n = int(input('n='))
# matrixA = fillDiagonal(makeMatrix(n))
# matrixB = fillDiagonal(makeMatrix(n))

# while True:
#     print("""MENU
# 1. Ubah isi matriks A
# 2. Ubah isi matriks B
# 3. Hasil penjumlahan A+B
# 4. Hasil pengurangan A-B
# 5. Hasil perkalian A*B
# 6. Exit""")
#     option = int(input('option='))
#     match option:
#         case 1:
#             matrixA = editMatrix(matrixA)
#         case 2:
#             matrixB = editMatrix(matrixB)
#         case 3:
#             printMatrix(addition(matrixA, matrixB))
#         case 4:
#             printMatrix(subtract(matrixA, matrixB))
#         case 5:
#             printMatrix(multiply(matrixA, matrixB))
#         case 6:
#             break