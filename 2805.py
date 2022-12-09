###
### 2805번: 나무 자르기
###

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

# 범위는 0부터 가장 긴 나무 길이까지
start, end = 0, max(trees)

while start <= end:
    # 중간값 찾기
    mid = (start + end) // 2

    # 나무 자르기 🪵
    sum = 0
    ### Python의 for문에서는 배열을 인덱스가 아닌 요소 단위(?)로 반복할 수 있습니다 ~
    for tree in trees:
        if tree > mid:
            sum += tree - mid
        # 🌟🌟🌟🌟🌟 이미 필요한 나무보다 많으면 반복문 탈출
        if sum > m:
            break

    # 자른 나무의 총합이 필요한 나무보다 많거나 같으면 절단기 높이를 늘이기
    if sum >= m:
        start = mid + 1
    # 자른 나무의 총합이 필요한 나무보다 적으면 절단기 높이를 줄이기
    else:
        end = mid - 1

print(end)