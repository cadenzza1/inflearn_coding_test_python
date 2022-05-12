
# 입력값들
# 4 11   
# 802
# 743
# 457
# 539


def Count(len): # len의 길이로 몇 개의 랜선이 나오는지 전달해주는 함수
    cnt = 0
    for x in Line:
        cnt += (x//len)
    return cnt # cnt의 값은 len의 길이로 만들 수 있는 랜선의 개수


k,n = map(int,input().split())
Line = []
for i in range(k):
    Line.append(int(input()))
largest = max(Line)

# 여기부터 binary search 시작
lt = 1
rt = largest
while lt <= rt:
    mid = lt + (rt-lt) // 2 # 여기서 mid는 n개를 만들 때 한 랜선의 길이
    if Count(mid) >= n: # 원하는 n개의 개수보다 많으면 
        res = mid
        lt = mid + 1 # 더 좋은 길이를 찾아야하므로 lt를 변경(키움)
    else: # len의 길이로는 n개 이상의 랜선을 만들지 못하면 (len이 너무 길면)
        rt = mid -1 # 길이를 줄이기

print(res)



