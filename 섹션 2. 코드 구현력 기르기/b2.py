# 6 2 5 3
# 5 2 7 3 8 9
# 15 3 10 3
# 4 15 8 16 6 6 17 3 10 11 18 7 14 7 15

t = int(input("테스트 케이스 개수를 입력해주세요 :"))

for i in range(t):
    n, s, e, k = map(int,input("n,s,e,k를 입력해주세요.").split())
    arr = list(map(int,input(f'{n}개의 숫자를 입력해주세요 :').split())) # 리스트 형성
    #arr = arr[s-1:e].sort() s번째부터 e번쨰까지 슬라이싱 하고 sort연달아 하려 했는데 NONE이 리턴됨!
    arr = arr[s-1:e]
    arr.sort()
    print(f"#{i+1} {arr[k-1]}")


# T = int(input())
#for t in range(T):
 #   n, s, e, k = map(int, input().split())
  #  a = list(map(int, input().split()))
  #  a = a[s-1:e]
  #  a.sort()
  #  print(a[k-1])