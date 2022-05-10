n,c = map(int,input().split()) # n은 마구간 수 , c는 말 수
List = []
for i in range(n):
    List.append(int(input()))
List.sort()

# C마리의 말을 N개의 마구간에 배치했을 때
# 가장 가까운 두 말의 거리가 최대가 되는 그 최대값구해

def Count(len):
    cnt = 1
    ep = List[0] # 말이 마지막에 배치된 지점
    for i in range(1,n):
        if List[i] - ep >= len:
            cnt+=1
            ep = List[i]
    return cnt

lt = 1 # 최소 거리는 1
rt = List[n-1] # 최대 거리는 마구간 맨 끝 좌표
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= c: #여기서 mid가 가장 가까운 두 말의 거리
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
