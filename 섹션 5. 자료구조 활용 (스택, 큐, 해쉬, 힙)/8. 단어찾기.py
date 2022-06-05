n = int(input())
written = []

for i in range(n):
    written.append(input())

for i in range(n-1):
    tmp = input()
    if tmp in written:
        written.remove(tmp)

print(written[0])