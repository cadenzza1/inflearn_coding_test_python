import numbers
import re

def find_yaksu(num):
    cnt = 0
    for i in range(1,num+1):
        if num % i == 0:
            cnt+=1
    return cnt

n = input()
size = len(n)

numbers = re.findall("\d+", n)

result = ""
for i in range(len(numbers)):
    result += numbers[i]
result = str(result)

for j in range(size):
    if result[j] == 0:
        result = result[j+1:]
    else:
        break

print(int(result))
print(find_yaksu(int(result)))

