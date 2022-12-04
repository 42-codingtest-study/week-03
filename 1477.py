###
### 1488번: 휴게소 세우기
###

import sys
input = sys.stdin.readline

# 입력값 받기
n, m, l = map(int, input().split())
spots = [0] + sorted(list(map(int, input().split()))) + [l]

# 고속도로의 끝에 세울 수 없음
start, end = 1, l - 1

while start <= end:
    # 중간값 찾기
    mid = (start + end) // 2

    # 두 휴게소 사이 거리가 mid보다 크면 사이에 휴게소 세우기 ... 🏠
    sum = 0
    for i in range(1, len(spots)):
        if spots[i] - spots[i - 1] > mid:
            sum += (spots[i] - spots[i - 1] - 1) // mid
            if sum > m:
                break

    # 휴게소가 m개보다 많으면 거리 늘려보기
    if sum > m:
        start = mid + 1
    # 휴게소가 m개보다 적거나 같으면 거리 줄여보기
    else:
        end = mid - 1

print(start)