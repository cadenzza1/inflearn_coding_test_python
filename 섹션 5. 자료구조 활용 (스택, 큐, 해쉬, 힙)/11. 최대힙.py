import heapq as hq
# heapq는 기본적으로 최소힙으로 작동을한다!
# 최대힙으로 작동 시킬려면 입력할 때 숫자에 마이너스 붙여서 음수로 넣기!
# 숫자 출력할 때는 똑같이 마이너스 붙여서 원래 숫자로 출력하면 됨! ㅎㅎ

a = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a)) # 2. 출력할 때는 '-'붙여서 원래 숫자로 출력하기
    else:
        hq.heappush(a, -n) # 1. 트리에 삽입할 때는 '-'붙여서 최대힙으로 만들기
