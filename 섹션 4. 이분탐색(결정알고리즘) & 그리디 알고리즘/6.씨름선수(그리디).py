n = int(input())

List = []
for i in range(n):
    h,w = map(int,input().split())
    List.append((h,w))
List.sort(reverse=True) # 키,몸무게 리스트를 키에대한 내림차순으로 정렬
largest = 0
cnt = 0

for x,y in List:
    if y>largest:
        largest = y
        cnt +=1

print(cnt)
        
            
