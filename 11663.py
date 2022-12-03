#선분 위의 점
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tmp = list(map(int, input().split()))
dot = sorted(tmp)

for i in range(m):
    find = list(map(int, input().split()))
    start,end = 0, n-1
    while start <= end:
        mid = ((start + end) // 2)
        if find[0] > dot[mid]:
            start = mid + 1
        else:
            end = mid - 1
    min = start
    start,end = 0, n-1
    while start <= end:
        mid = ((start + end) // 2)
        if find[1] < dot[mid]:
            end = mid - 1
        else:
            start = mid + 1
    max = end + 1
    print(max-min)