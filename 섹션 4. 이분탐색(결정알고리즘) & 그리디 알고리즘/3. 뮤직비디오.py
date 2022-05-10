n,m = map(int,input().split())
time = list(map(int,input().split()))

def Count(capacity): # dvd의 용량을 capacity로 했을 때 필요한 dvd 개수를 리턴하는 함수
    cnt = 1
    sum = 0
    for x in time:
        if sum+x>capacity: # 노래를 넣으면 dvd용량이 초과되면
            cnt+=1 # dvd개수 1개 증가
            sum = x
        else:
            sum += x
    return cnt

maxx = max(time)
lt = 1
rt = sum(time)
res = 0

# 이분 검색 시작
while lt<=rt:
    mid = lt + (rt - lt) // 2
    if mid >= maxx and Count(mid) <= m: # mid>=maxx 의 이유는 dvd의 용량이 플레이 시간이 가장 긴 음악보다 커야 하기 때문!!!!
        res = mid
        rt = mid - 1 # 더 작은 용량으로 가능한지 알아보기 위해 최대 용량 줄이기
    else:
        lt = mid + 1

print(res)
