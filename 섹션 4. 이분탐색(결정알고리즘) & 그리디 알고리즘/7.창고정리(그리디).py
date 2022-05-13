l = int(input())
num = list(map(int,input().split()))
m = int(input())

for i in range(m):
    big = num.index(max(num))
    small = num.index(min(num))
    num[big] -= 1
    num[small] += 1

print(max(num) - min(num))
