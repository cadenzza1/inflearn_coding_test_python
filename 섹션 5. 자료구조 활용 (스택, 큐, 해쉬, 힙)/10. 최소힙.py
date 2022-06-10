import heapq as hq

# pop될 땐 가장 밑의 레벨의 가장 오른쪽 노드가 루트노드가 된다. (다운힙 과정)
# 루트노드와 자식노드중 더 작은 값과 변경한다.
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
