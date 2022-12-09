###
### 19637번: IF문 좀 대신 써줘
###

import sys
input = sys.stdin.readline

# 입력값 받기
n, m = map(int, input().split())

title, value = [], []
for _ in range(n):
    tmp = input().split()
    title.append(tmp[0])
    value.append(int(tmp[1]))

# 이진 탐색 함수
def binary_search(target):
    start = 0
    end = n - 1

    while start <= end:
        # 중간값 찾기
        mid = (start + end) // 2

        # 중간값이 비교값보다 크거나 같으면 중간 지점 왼쪽 부분 확인
        # value는 상한값이므로 비교값과 같은 경우에도 그 칭호를 부여 !
        # ex) 10000 : WEAK
        if value[mid] >= target:
            end = mid - 1
        # 중간값이 비교값보다 작으면 중간 지점 오른쪽 부분 확인
        else:
            start = mid + 1

    # 인덱스 리턴
    return start


for i in range(m):
    print(title[binary_search(int(input()))])