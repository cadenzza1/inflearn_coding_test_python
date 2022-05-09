#5
#10 13 10 12 15
#12 39 30 23 11
#11 25 50 53 15
#19 27 29 37 27
#19 13 30 13 19
#3
#2 0 3
#5 1 2
#3 1 4
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

m = int(input())

for _ in range(m):
    h, t, k = (map(int,input().split()))

    if t == 0:
        for _ in range(k):
            arr[h-1].append(arr[h-1].pop(0))

    else:
        for _ in range(k):
            arr[h-1].insert(0 , arr[h-1].pop())
    
left,right = 0,n
tot = 0
for i in range(n):
    for j in range(left,right):
        tot += arr[i][j]

    if i < (left + right) // 2:
        left += 1
        right -= 1
    else:
        left -= 1
        right += 1

print(tot)

