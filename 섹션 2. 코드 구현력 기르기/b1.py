N,K = map(int, input().split())

yaksu = [j for j in range(1,K+1) if N % j == 0]

if len(yaksu) < K:
    print("-1")
else:
    print("입력하신 숫자 K는 N의 {}번째로 작은 약수입니다.".format(1+ yaksu.index(K)))


#--------------------------------------------------------------------------------

#n, k = map(int, input().split())
#cnt = 0
#for i in range(1, n+1):
#    if n % i == 0:
#        cnt += 1
#    if cnt == k:
#        print(i)
#        break
#else:
#    print(-1)