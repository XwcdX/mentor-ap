# 1. Print Numbers
for i in range(1, 11):
    print(i)

# 2. String Length Without len()
s = "hello"
count = 0
for _ in s:
    count += 1
print(count)

# 3. Sum of Natural Numbers
n = 5
total = 0
for i in range(1, n + 1):
    total += i
print(total)

# 4. Menu-Driven Program
while True:
    print("1. Find factorial")
    print("2. Reverse a number")
    print("3. Exit")
    choice = int(input())
    if choice == 1:
        n = int(input())
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        print("Factorial =", fact)
    elif choice == 2:
        num = int(input())
        rev = 0
        while num > 0:
            rev = rev * 10 + num % 10
            num //= 10
        print("Reversed =", rev)
    elif choice == 3:
        print("Exiting program...")
        break

# 5. Largest Element in a List
nums = [10, 25, 3, 99, 42]
largest = nums[0]
for x in nums:
    if x > largest:
        largest = x
print(largest)

# 6. Palindrome Check
word = "Madam"
w = word.lower()
rev = ""
for i in range(len(w)-1, -1, -1):
    rev += w[i]
if w == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# 7. Fibonacci Sequence
n = 6
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a+b
print()

# 8. Prime Numbers Up to N
n = 10
for num in range(2, n+1):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")
print()

# 9. Pattern Printing
n = 5
for i in range(1, n+1):
    print("*" * i)

# 10. Matrix Multiplication
A = [[1,2],[3,4]]
B = [[2,0],[1,2]]
result = [[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += A[i][k] * B[k][j]
for row in result:
    print(*row)

# 11. GCD Using Loops (repeated subtraction)
a, b = 48, 18
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print(a)

# 12. Bubble Sort
arr = [64, 25, 12, 22, 11]
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)

# 13. Josephus Problem (simulation)
n, k = 7, 3
people = list(range(1, n+1))
idx = 0
while len(people) > 1:
    idx = (idx + k - 1) % len(people)
    people.pop(idx)
print(people[0])

# 14. Collatz Conjecture
num = 6
steps = 0
while num != 1:
    if num % 2 == 0:
        num //= 2
    else:
        num = 3*num + 1
    steps += 1
print(steps)

# 15. Water Jug Puzzle (BFS-like simulation)
from collections import deque
m, n, d = 3, 2, 1
visited = set()
q = deque([(0,0,0)])  # jug1, jug2, steps
ans = -1
while q:
    a,b,steps = q.popleft()
    if (a,b) in visited: continue
    visited.add((a,b))
    if a == d or b == d:
        ans = steps
        break
    q.append((m,b,steps+1)) # fill jug1
    q.append((a,n,steps+1)) # fill jug2
    q.append((0,b,steps+1)) # empty jug1
    q.append((a,0,steps+1)) # empty jug2
    pour = min(a, n-b)
    q.append((a-pour,b+pour,steps+1))
    pour = min(b, m-a)
    q.append((a+pour,b-pour,steps+1))
print(ans)

# 16. Knight’s Tour (Backtracking)
n = 5
board = [[-1]*n for _ in range(n)]
moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
board[0][0] = 0
pos = 1
def safe(x,y):
    return 0<=x<n and 0<=y<n and board[x][y]==-1
def solve(x,y,pos):
    if pos == n*n:
        return True
    for dx,dy in moves:
        nx,ny = x+dx,y+dy
        if safe(nx,ny):
            board[nx][ny] = pos
            if solve(nx,ny,pos+1):
                return True
            board[nx][ny] = -1
    return False
solve(0,0,1)
for row in board:
    print(row)

# 17. N-Queens Problem
n = 4
board = [["."]*n for _ in range(n)]
cols, diag1, diag2 = set(), set(), set()
def backtrack(r):
    if r == n:
        for row in board:
            print(" ".join(row))
        print()
        return True
    for c in range(n):
        if c in cols or (r-c) in diag1 or (r+c) in diag2:
            continue
        board[r][c] = "Q"
        cols.add(c); diag1.add(r-c); diag2.add(r+c)
        if backtrack(r+1): return True
        board[r][c] = "."
        cols.remove(c); diag1.remove(r-c); diag2.remove(r+c)
    return False
backtrack(0)

# 18. Sudoku Solver
grid = [
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,8,0,3,0,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]
]
def valid(r,c,num):
    for i in range(9):
        if grid[r][i]==num or grid[i][c]==num: return False
    sr,sc=3*(r//3),3*(c//3)
    for i in range(sr,sr+3):
        for j in range(sc,sc+3):
            if grid[i][j]==num: return False
    return True
def solve():
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                for num in range(1,10):
                    if valid(i,j,num):
                        grid[i][j]=num
                        if solve(): return True
                        grid[i][j]=0
                return False
    return True
solve()
for row in grid:
    print("".join(map(str,row)))
