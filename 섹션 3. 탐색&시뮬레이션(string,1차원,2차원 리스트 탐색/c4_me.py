n = int(input())
n_num = list(map(int,input().split()))

m = int(input())
m_num = list(map(int,input().split()))

arr = n_num + m_num
arr.sort()

print(arr)

# 이렇게 코드짜면 O(nlogn)임. 우리가 원하는건 0(n)을 원함. 코드 다시짜보자! ---> c4_him.py