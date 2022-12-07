#IF문 좀 대신 써줘
import sys
input = sys.stdin.readline

n,m=map(int,input().split())
res = []
for i in range(n):
    tmp = input().split() 
    tmp[1] = int(tmp[1])
    res.append(tmp)

for i in range(m):
    tmp = int(input())
    start,end = 0, n-1
    mid = int((start + end) // 2)
    while (start <= end):
        if (tmp > res[mid][1]):
            start = mid + 1
        else:
            end = mid - 1
        mid = int((start + end) // 2)
    mid = start
    print(res[mid][0])