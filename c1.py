def is_same(word):
    a = word.lower()
    if a == a[::-1]:
        return 'YES'
    else:
        return 'NO'

def is_same2(arr):
    size = len(arr)
    arr = arr.lower()
    for j in range(size//2):
        if arr[j] != arr[-1 - j]:
            return 'NO'
        else:
            return 'YES'

n = int(input()) # 입력받을 단어의 개수 입력받기
arr = []

for _ in range(n):
    arr.append(input())
    
for i in range(n):
    print("#{}".format(i+1),is_same2(arr[i]))