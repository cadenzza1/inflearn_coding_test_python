n = int(input())
a = list(map(int,input().split()))

m = int(input())
b = list(map(int,input().split()))

c = []

p0,p1 = 0,0

while p0 < n and p1 < m:
    if a[p0] <= b[p1]:
        c.append(a[p0])
        p0 += 1
        
    elif b[p1] < a[p0]:
        c.append(b[p1])
        p1 += 1

if p0 < n:
    c = c + a[p0:]
else:
    c = c + b[p1]
    

print(c)