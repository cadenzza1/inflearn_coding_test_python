def two(x):
    if x>0:
        two(x//2)
        print(x%2,end = '')


if __name__ == "__main__":
    n = int(input())
    two(n)
