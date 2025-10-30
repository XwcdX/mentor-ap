n = int(input("matrix size: "))
spiral = [0 for _ in range(n*n)]
top, bottom = 0, n-1
left, right = 0, n-1
num = 1

while num <= n*n:
    # ke kanan
    for i in range(left, right+1):
        spiral[top*n + i] = num
        num += 1
    top += 1

    # ke bawah
    for i in range(top, bottom+1):
        spiral[i*n + right] = num
        num += 1
    right -= 1

    # ke kiri
    for i in range(right, left-1, -1):
        spiral[bottom*n + i] = num
        num += 1
    bottom -= 1

    # ke atas
    for i in range(bottom, top-1, -1):
        spiral[i*n + left] = num
        num += 1
    left += 1

for i in range(n):
    for j in range(n):
        print(spiral[i*n + j], end=" ")
    print()