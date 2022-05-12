n = int(input())
arr = []

for i in range(n):
    a,b = map(int,input().split())
    arr.append([a,b])

arr.sort(reverse = True)
cnt = 0
maxx = 0


for x,y in arr:
    if y > maxx:
        maxx = y
        cnt += 1

print(cnt)