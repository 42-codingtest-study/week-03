import sys
from bisect import bisect_left
#bisect(a,b)는 b가 a에 들어갈 수 있는 가장 오른쪽 위치 반환

input = sys.stdin.readline

n, m = map(int, input().split())
name = []
power = []

for _ in range(n):
    t, p = input().split()

    name.append(t)
    power.append(int(p))

'''
for j in range(m):
    x = int(sys.stdin.readline())
    y = 0

    while y != 1:
        for k in int_power:
            if x <= k:
                z = int_power.index(k)
                print(name[z])
                y = 1
                break
            else:
                y = 1
'''

for j in range(m):
    print(name[bisect_left(power, int(input()))])

