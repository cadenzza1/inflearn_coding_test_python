def isPrime(x):
    if x == 1 or x == 2: return True
    for i in range(3,x):
        if x % i == 0:
            return False
            #break 필요 없는 구문임. 어차피 return에서 함수는 끝났음.
        else:
            return True
    

a = [1,2,39,28,29,11,13]

for j in a:
    print(isPrime(j))