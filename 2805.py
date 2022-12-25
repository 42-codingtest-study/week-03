import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

def binary_search(start, end, trees):
	result = 0
	while start <= end:
		mid = (start + end) // 2
		total = 0
		for tree in trees:
			if tree > mid:
				total += tree - mid
		if total >= M :
			result = mid
			start = mid + 1
		else :
			end = mid - 1
	return result

result = binary_search(0, max(trees), trees)
print (result)