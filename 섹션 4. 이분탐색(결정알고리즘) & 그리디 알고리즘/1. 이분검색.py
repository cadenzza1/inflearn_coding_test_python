import sys
sys.stdin = open(
    r"C:\Users\김민규\Desktop\A.A.P\인프런 파이썬 알고리즘 문제풀이(코딩테스트 대비)\inflearn_python\섹션 4. 이분탐색(결정알고리즘) & 그리디 알고리즘\input.txt", "r")

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()


def binary_search(arr, l, r, key):
    mid = l + (r-l) // 2

    if arr[mid] == key:
        print(mid+1)
            
    elif arr[mid] > key:
        binary_search(arr, l, mid-1, key)
    else:
        binary_search(arr, mid+1, r, key)


binary_search(nums, 0, len(nums)-1, 32)
