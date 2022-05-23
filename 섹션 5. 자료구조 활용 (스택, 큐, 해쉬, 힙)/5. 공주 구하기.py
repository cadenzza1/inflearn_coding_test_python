from collections import deque

n,k = map(int,input().split())
deq = deque(range(1,n+1))

while len(deq) > 1:
    deq.rotate(-2)
    deq.popleft()

print(deq[0])
