n = int(input())
arr = [None] * n

arr = [list(map(int,input().split())) for _ in range(n)]

big = -1

for i in range(n):
    sum1=sum2=0 # sum1은 행, sum2은 열의 합
    for j in range(n):
        sum1 += arr[i][j]
        sum2 += arr[j][i]
        if sum1 > sum2:
            if sum1>big:
                big = sum1
        else:
            if sum2 > big:
                big = sum2

diag1,diag2 = 0,0
for k in range(n):
    diag1 += arr[k][k] 
    diag2 += arr[k][n-1-k]

    if diag1 > big:
        big = diag1
    if diag2 > big:
        big = diag2

print(big)