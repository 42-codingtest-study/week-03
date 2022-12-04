import sys
from bisect import bisect_left, bisect_right
#bisect(a,b)는 b가 a에 들어갈 수 있는 가장 오른쪽 위치 반환

input = sys.stdin.readline

n, m = map(int, input().split())

dot = list(map(int, input().split()))
dot.sort()

for _ in range(m):
    start, end = map(int, input().split())
    left_index = bisect_left(dot, start)
    right_index = bisect_right(dot, end)

    print(right_index - left_index)