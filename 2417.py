###
### 2417번: 정수 제곱근
###

n = int(input())

start = 0
end = n

while start <= end:
    # 중간값 찾기
    mid = (start + end) // 2

    # 중간값의 제곱이 n보다 크거나 같으면 절반 지점의 왼쪽 부분 확인
    ### **: 제곱을 구하는 산술 연산자입니다 ~
    if mid ** 2 >= n:
        end = mid - 1
    # 중간값의 제곱이 n보다 작으면 절반 지점의 오른쪽 부분 확인
    else:
        start = mid + 1

print(start)