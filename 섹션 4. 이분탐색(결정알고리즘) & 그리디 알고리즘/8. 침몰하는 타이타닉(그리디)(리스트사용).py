n, m = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()
cnt = 0 # 구명보트의 개수

while arr: # 배열이 비어있지 않으면 계속 반복문 실행
    if len(arr) == 1: # 최후에 한 명만 남았을 시 그냥 태워 보내깅
        cnt += 1
        break 
    if arr[0] + arr[-1] > m:
        arr.pop() # 둘의 무게를 합친게 제한보다 크면 젤 무거운놈만 태워 보내기 (pop시키기)
        cnt += 1
    else:
        arr.pop(0)
        arr.pop()
        cnt += 1

print(cnt)

# 리스트를 사용하면 젤 앞의 요소를 pop할 때마다 뒤의 요소들이 한 칸씩 앞으로 땡겨짐 --> 상당히 비효율적
# '데크'라는 자료구조를 사용하면 이런 땡겨지는 연산 없이, pop되면 알아서 포인터가 다음 요소를 가리키도록 변경됨
# 그래서 데크 자료구조도 사용해서 구현해봅시다.