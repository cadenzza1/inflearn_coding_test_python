a = list(range(1,11))

for i in enumerate(a):
    print(i[0])

for index,value in enumerate(range(10)):
    print(index,value)

if all(9>x for x in range(10)):
    print('yes')
else:
    print("no")