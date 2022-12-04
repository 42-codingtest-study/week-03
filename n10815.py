n = int(input())

num = set(map(int, input().split()))

m = int(input())

check = list(map(int, input().split()))

for i in range(m):
    if check[i] in num:
        print(1, end=' ')
    else:
        print(0, end=' ')