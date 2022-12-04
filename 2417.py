###
### 2417번: 정수 제곱근
###

n = int(input())

start = 0
end = n

while start <= end:
    # 중간값 찾기
    mid = (start + end) // 2

    # 중간값의 제곱이 n보다 크면 절반 지점의 왼쪽 부분 확인
    if mid ** 2 >= n:
        end = mid - 1
    # 중간값의 제곱이 n보다 작으면 절반 지점의 오른쪽 부분 확인
    else:
        start = mid + 1

print(start)