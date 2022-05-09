def digit_sum(x): # 자릿수의 합을 계산하는 함수
    tmp = 0 # 자릿수의 합을 저장할 변수
    for j in range(len(x)): # 자연수를 문자열로 생각해서 자릿수만큼 반복한다.
        tmp += int(x[j]) # tmp변수에 각 자릿수를 더하여 저장한다.
    return tmp


n = int(input("3에서 100 사이의 수를 입력해주세요 :"))
arr = list(input(f'{n}개의 자연수를 입력해주세요:').split())

sum = [] # 자릿수의 합을 저장할 배열

for i in arr: # 자연수를 끄집어오는 반복문
    sum.append(digit_sum(i)) # 자연수를 끄집어와서 digit_sum함수에 넣는다.

# sum 배열에는 각 자연수의 자릿수의 합이 저장되어 있는 상태!

max = 0

for k in range(len(sum)): # 자릿수의 합이 같을 때 더 빠른 수를 출력하기 위한 반복문
    if sum[k] > max:
        max = k

print(arr[k])


