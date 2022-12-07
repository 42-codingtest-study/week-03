#숫자카드
n = int(input())
card = set(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
for i in check:
    if i in card:
        print(1, end=' ')
    else:
        print(0, end=' ')
    
