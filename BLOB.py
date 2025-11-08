row=int(input())
col=int(input())
matrix=[]

# input
for i in range(row):
    list1=input().split()
    matrix.append(list1)

"""
o o o o o x o x o
x o x x x o o o x
o x o x x x o o o
"""    
def cari_ubah_x(rowNow, colNow):
    if rowNow < 0 or rowNow > row-1 or colNow < 0 or colNow > col-1:
        return
    if matrix[rowNow][colNow] != 'x':
        return
    
    matrix[rowNow][colNow] = 'o'
    
    # 8 arah mata angin
    """
    -1 -1 -> kiri atas
    -1 0 -> atas
    -1 1 -> kanan atas
    dst
    """
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue    
            cari_ubah_x(rowNow + i, colNow + j)
                
    return

# def print_matrix(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             print(matrix[i][j], end=' ')
#         print()
#     print()
        
# main -> mencari x pada matrix
count = 0
for baris in range(row):
    for kolom in range(col):
        if matrix[baris][kolom] == "x":
            count+=1
            cari_ubah_x(baris,kolom)
            # print_matrix(matrix)
            
print(count)