###
### 10815번: 숫자 카드
###

import sys

# 입력값 받기
n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

# 이분 탐색을 위해 정렬
cards.sort()

# 이분 탐색 함수
def binary_search(array, target, start, end):
    if start > end:
        return None
    
    # 중간값 찾기
    mid = (start + end) // 2

    # 원하는 값이면 반환
    if array[mid] == target:
        return mid
    # 찾은 값이 원하는 값보다 크면 절반 지점의 왼쪽 부분 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 찾은 값이 원하는 값보다 작으면 절반 지점의 오른쪽 부분 확인
    else:
        return binary_search(array, target, mid + 1, end)

for i in range(m):
    if binary_search(cards, nums[i], 0, n - 1) != None:
        print("1", end = ' ')
    else:
        print("0", end = ' ')
