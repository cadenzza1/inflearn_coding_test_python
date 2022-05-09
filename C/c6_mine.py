n = int(input())
arr = [None] * n

arr = [list(map(int,input().split())) for _ in range(n)]
#for i in range(n):
#    arr[i] = list(map(int,input().split()))

max = sum(arr[0])
for j in range(1,n):
    if sum(arr[j]) > max:
        max = sum(arr[j])

for k in range(n):
    tmp = arr[0][k] + arr[1][k] + arr[2][k] + arr[3][k] + arr[4][k]
    if tmp>max:
        max = tmp

tmp = arr[0][0] + arr[1][1] + arr[2][2] + arr[3][3] + arr[4][4]
if tmp > max:
    max = tmp

tmp = arr[0][4] + arr[1][3] + arr[2][2] + arr[3][1] + arr[4][0]
if tmp> max:
    max = tmp

print(max)


