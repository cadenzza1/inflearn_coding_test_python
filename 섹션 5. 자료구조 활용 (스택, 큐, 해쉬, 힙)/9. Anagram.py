a=input()
b=list(input())

res = "No"

for i in a:
    if i in b:
        res = "Yes"
        b.remove(i)
        continue
    else:
        res = "No"
        break

print(res)