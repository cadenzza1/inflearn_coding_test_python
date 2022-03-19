# 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 
# 확률이 높은 숫자를 출력하는 프로그램을 작성하세요.
# 정답이 여러 개일 경우 오름차순으로 출력합니다.

n,m = map(int, input('n과 m을 입력해주세요. : ').split())

sum = [] # 주사위 각 면의 합을 저장할 배열
cnt = [] # 각 합이 몇 번 나왔는지 저장할 배열
#cnt = [0] * (n+m) 이렇게 쓰면 길게 안쓰고 0이 n+m만큼 할당됨!
for _ in range(0,(n+m) +1): # n+m개 만큼의 공간을 할당한 후
    cnt.append(0)  # 전부 0으로 초기화
# cnt배열은 0부터 n+m까지 n+m개의 공간이 생겼으며, 전부 0으로 할당되었음


for i in range(1,n+1):
    for j in range(1,m+1):
        sum.append(i+j) # sum 배열에 주사위에서 나온 값의 합들을 저장
        cnt[i+j] += 1 # 나온 값의 합에 해당하는 cnt배열의 인덱스에 해당하는 값을 1씩 증가

result_arr = [] # 정답에 해당하는 숫자들을 저장할 배열

for k in range(len(cnt)): # cnt배열의 값들을 일일이 확인하며 result배열에 값 넣기
    if cnt[k] == max(cnt): # max함수를 활용하여 cnt배열에서 가장 큰 값과 같은 값들을
        result_arr.append(k) # 전부 result배열에 넣기

for l in result_arr:
    print(l,end = ' ')




