# https://www.acmicpc.net/problem/2417

# import math
# print(math.ceil(int(input()) ** 0.5))	# ㅋㅋ

#--------------------------------------

n = int(input())
low = 0
high = n
while (low < high) :		# 이분탐색을 하면 최솟값이 최댓값보다 같거나 커지게 되면 그 값이 정답이 된다.
	mid = (low + high) // 2	# 중간 값 찾기
	if (mid ** 2 < n) :		# 중간값의 제곱이 n보다 작다면 중간값을 높여줄 필요가 있다.
		low = mid + 1		# 최솟값을 높여주면 중간값도 높일 수 있음
	else :
		high = mid - 1		# 반대의 경우
print(low)