def is_prime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    tmp = None
    for i in range(2,x):
        if x % i == 0:
            tmp = False
            break
        else:
            tmp = True 
    return tmp

n = int(input('2이상 200,000이하의 수를 입력해주세요 :'))

cnt = 0

for j in range(1,n+1):
    if is_prime(j) == True:
        cnt += 1

print(cnt)
    