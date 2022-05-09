n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

res = 0
s=e=n//2 # s와 e는 포인터 변수이다. 

for i in range(n): # 여기서 n은 행을 가리키는 포인터라고 생각하면 된다.
    for j in range(s,e+1): # s포인터부터 e포인터까지의 요소의 개수들을 더하기 / 열 선택
        res += arr[i][j]
    
    if i < n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1

print(res)
