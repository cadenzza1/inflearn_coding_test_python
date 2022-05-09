a = [0,2,3] * 4
print(a)

b = [[0]*3 for _ in range(3)]
print(b)
print(b[0])
print(b[0][0])

b[0][1] = 1
b[0][2] = 2
b[1][0] = 3
b[1][1] = 4
b[1][2] = 5
b[2][0] = 6
b[2][1] = 7
b[2][2] = 8

print(b)

for i in b:
    for j in i:
        print(j,end = ' ')