n,k = map(int,input("n과 k의 값을 입력해주세요 :").split())
a = list(map(int,input(f"{n}개의 값을 입력해주세요. :").split()))

res = set() # set은 자료구조이다. 중복된 값이 여러 개 들어와도 하나만 입력된다!

for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            res.add(a[i]+a[j]+a[m]) # 중복된 값을 제거하면서 res변수에 값들 저장

res=list(res) # 정렬을 해야하는데 set자료구조는 sort함수가 없으니 list로 변환!
res.sort(reverse = True) # 오름차순이 아니라 내림차순으로 정렬해야 하므로 reverse = True
print(res[k-1])