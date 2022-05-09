def reverse(arr,start,end):
    size = len(arr[start:end+1])
    for i in range(size // 2):
        arr[start + i], arr[end - i] = arr[end - i], arr[start + i]
    return arr


arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for _ in range(10):
    ai,bi = map(int,input().split())
    reverse(arr,ai,bi)

result = ""
for i in arr[1:]:
    print(i, end = ' ')

