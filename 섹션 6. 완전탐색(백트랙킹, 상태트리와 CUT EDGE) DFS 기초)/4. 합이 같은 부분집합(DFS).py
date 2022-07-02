import sys

def DFS(idx,sum):
    if sum > total//2: # 복잡도 개선. 
        return
    if idx == n:
        if sum == (total - sum):
            print('YES')
            sys.exit(0) # 프로그램 자체를 종료시키는 명령어
    else:
        DFS(idx+1,sum+nums[idx])
        DFS(idx+1,sum)

n = int(input())
nums = list(map(int,input().split()))

total = sum(nums)
DFS(0,0)
print("NO")