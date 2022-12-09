###
### 11663번: 선분 위의 점
###

import sys
input = sys.stdin.readline

# 입력값 받기
n, m = map(int, input().split())
dots = list(map(int, input().split()))

# 이분 탐색을 위해 정렬
dots.sort()

# 이분 탐색 함수
def binary_search(target, flag):
    ### 17라인, 37라인에 있는 start, end는 다른 변수입니다 ~
    start, end = 0, n - 1

    while start <= end:
        mid = (start + end) // 2

        if dots[mid] == target:
            return mid
        elif dots[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    # flag를 두어 최소점, 최대점 리턴값을 다르게 함
    if flag == 0:
        return start
    else:
        return end
    
for _ in range(m):
    start, end = map(int, input().split())
    
    # 선분 위의 최소점 인덱스 찾기
    min = binary_search(start, 0)
    # 선분 위의 최대점 인덱스 찾기
    max = binary_search(end, 1)

    print(max - min + 1)