###
### 10815번: 숫자 카드
###

import sys
input = sys.stdin.readline

# 입력값 받기
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

# 이분 탐색을 위해 정렬
cards.sort()

# 이분 탐색 함수
def binary_search(target, start, end):
    if start > end:
        return None
    
    # 중간값 찾기
    ### //: 몫을 구하는 산술 연산자입니다 ~
    mid = (start + end) // 2

    # 원하는 값이면 반환
    if cards[mid] == target:
        return mid
    # 중간값이 원하는 값보다 크면 절반 지점의 왼쪽 부분 확인
    elif cards[mid] > target:
        return binary_search(target, start, mid - 1)
    # 중간값이 원하는 값보다 작으면 절반 지점의 오른쪽 부분 확인
    else:
        return binary_search(target, mid + 1, end)

for i in range(m):
    if binary_search(nums[i], 0, n - 1) != None:
        ### Python의 print 함수는 자동으로 개행이 붙기 때문에 
        ### end 옵션을 사용해 개행 대신 ' '를 붙여줬습니다 ~
        print("1", end = ' ')
    else:
        print("0", end = ' ')
