###
### 3079번: 입국 심사
###

import sys
input = sys.stdin.readline

# 입력값 받기
n, m = map(int, input().split())

time = []
for _ in range(n):
    time.append(int(input()))

# start: 제일 짧은 심사 시간, end: 제일 긴 심사 시간 * 사람 수
start = min(time)
end = result = max(time) * m

while start <= end:
    # 중간값 구하기
    mid = (start + end) // 2

    # mid 시간 동안 심사 받을 수 있는 사람 수 👯‍♀️
    sum = 0
    for t in time:
        sum += mid // t
        if sum > m:
            break
    
    # 심사 받을 수 있는 사람이 m보다 크거나 같으면 (심사 가능 !!!) 시간 줄여보기
    if sum >= m:
        end = mid - 1
        # 더 작은 값 저장
        result = min(result, mid)
    # 심사 불가능하면 시간 늘려보기
    else:
        start = mid + 1

print(result)