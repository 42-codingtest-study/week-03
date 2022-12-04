import sys

input = sys.stdin.readline

n = int(input())
sj_card = list(map(int, input().split()))
m = int(input())
check_card = list(map(int, input().split()))
result = []
# 탐색하기 위해 정렬해 줌
sj_card.sort()

def binary_search(check, sj_card, start, end):
	while start <= end:
		mid = (start + end) // 2
		if sj_card[mid] == check:
			result.append('1')
			return True
		elif sj_card[mid] > check:
			end = mid -1
		else:
			start = mid + 1
	# 배열에서 못 찾은 경우
	result.append('0')

for check in check_card:
	binary_search(check, sj_card, 0, n-1)

print(' '.join(result))