n = int(input())

q = 0
end = n

while q <= end:
	mid = (q + end) // 2
	if mid ** 2 < n:
		q = mid + 1
	else:
		end = mid - 1

print(q)