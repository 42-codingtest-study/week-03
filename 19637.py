import sys
input = sys.stdin.readline

N, M = map(int, input().split())
RANK = [input().split() for _ in range(N)]
answer = []

def binary_search(target, RANK):
	start = 0 
	end = len(RANK) - 1
	find = 0
	while start <= end:
		mid = (start + end) // 2
		if int(RANK[mid][1]) >= target:
			end = mid - 1
			find = mid
		else:
			start = mid + 1
	return find

for i in range(M):
	target = int(input())
	find = binary_search(target, RANK)
	answer.append(RANK[find][0])

print('\n'.join(answer))