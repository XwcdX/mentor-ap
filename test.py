# def box_count(x,y):
#     if x == y:
#         return 1
#     if x < y:
#         return box_count(x, y-x) + 1
#     else:
#         return box_count(x-y, y) + 1
    
# print(box_count(3,7))
#memoization
"""
[1,2,3,4]
{
    1 : "hahaha",
    2 : "nnnn"
}
"""
def fibo (n, memo={}):
    if n in memo:
        return memo[n]
    if n<=0:
        return 0
    if n==1:
        return 1, None
    else: 
        memo[n] = fibo(n-1) + fibo(n-2)
        print(memo)
        res = memo[n]
        return res, memo
        
# dic = {
#     64 : 'a',
#     65 : 'b'
# }

# for i,j in dic.items():
#     print(i, '->', j)

try:
    print('1'+2)
except:
    print('salah 1')

try:
    print('1'*2)
except:
    print('input salah')