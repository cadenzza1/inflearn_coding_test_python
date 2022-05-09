n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

arr.insert(0,[0]*n)
arr.append([0]*n)

for x in arr:
    x.insert(0,0)
    x.append(0)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

cnt = 0

for i in range(1,n+1): # 행 선택 반복문
    for j in range(1,n+1): # 열 선택 반복문
        if all(arr[i][j] > arr[i+dx[k]][j+dy[k]] for k in range(4)):
        # 내 방식(원초적)if arr[i][j] > arr[i-1][j] and arr[i][j] > arr[i][j-1] and arr[i][j] > arr[i+1][j] and arr[i][j] > arr[i][j+1]:
            cnt+=1

print(cnt)
