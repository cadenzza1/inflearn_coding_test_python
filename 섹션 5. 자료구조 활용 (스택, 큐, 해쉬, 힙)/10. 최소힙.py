import heapq as hq

a = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a)) # 루트노드 출력
    else:
        hq.heappush(a, n) # a라는 힙에 최소힙 형태로 n을 삽입해라
