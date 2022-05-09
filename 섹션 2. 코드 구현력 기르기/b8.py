def reverse(x):
    res = ''
    for i in x:
        if i == '0':
            continue
        res = i + res
    return res


def isPrime(y):

    if y == 2:
        return True

    tmp = None
    for j in range(2,y):
        if y % j == 0:
            return False
        else:
            tmp = True
    return tmp

n = input() # 입력될 숫자의 갯수를 입력받는다.
arr = list(input().split())

for k in arr:
    if isPrime(int(reverse(k))) == True:
        print(reverse(k), end = ' ')