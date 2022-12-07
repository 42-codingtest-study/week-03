# https://www.acmicpc.net/problem/11663

# 선분 위의 점

# 문제
# 일차원 좌표상의 점 N개와 선분 M개가 주어진다. 이때, 각각의 선분 위에 입력으로 주어진 점이 몇 개 있는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 점의 개수 N과 선분의 개수 M이 주어진다. (1 ≤ N, M ≤ 100,000) 둘째 줄에는 점의 좌표가 주어진다. 두 점이 같은 좌표를 가지는 경우는 없다. 셋째 줄부터 M개의 줄에는 선분의 시작점과 끝점이 주어진다. 입력으로 주어지는 모든 좌표는 1,000,000,000보다 작거나 같은 자연수이다.

# 출력
# 입력으로 주어진 각각의 선분 마다, 선분 위에 입력으로 주어진 점이 몇 개 있는지 출력한다.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dot = list(map(int, input().split()))
dot.sort()

def dot_min(a):  # 선분 중 가장 작은 점 구하기 
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2

        if dot[mid] < a:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1

def dot_max(b):   # 선분 중 가장 큰 점 구하기
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2

        if b < dot[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return end

for i in range(M):
    start, end = map(int, input().split())
    print(dot_max(end) - dot_min(start) + 1)