n = int(input('5에서 100사이의 숫자를 입력해주세요 :'))
arr = list(map(int,input('10개의 수학점수를 입력해주세요. :').split()))

ave = sum(arr) / 10  # round함수가 반올림 함수는 맞지만 round_half_even 방식이므로
ave += 0.5 # 0.5를 더한 후 int함수로 소수점 부분을 지워버리는 방식을 택한다
ave = int(ave) # 반올림한 것과 같은 결과를 얻을 수 있다.

min = 2222

for idx, x in enumerate(arr):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1

print(ave, res)