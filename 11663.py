import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dots = list(map(int, input().split()))
dots.sort()
answer = []

def binary_search(target, type):
	start = 0
	end = N - 1
	while start <= end:
		mid = (start + end) // 2
		if target > dots[mid]:
			start = mid + 1
		elif target < dots[mid]:
			end = mid - 1
		else:
			return mid
	
	if type == 0:
		return start
	else :
		return end
	

for _ in range(M):
	start, end = map(int, input().split())
	left = binary_search(start, 0)
	right = binary_search(end, 1)
	answer.append(str(right - left + 1))

print('\n'.join(answer))