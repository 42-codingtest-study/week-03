#나무 자르기 (pypy3)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)

while start <= end:
        mid = ((start + end) // 2) #중간
        cnt = 0 #잘린 나무들의 합
        for i in trees:
            if i > mid: # mid보다 크면 잘림
                cnt += i - mid
        
        if cnt >= m:
            start = mid + 1 #많이 잘렸으면
        else:
            end = mid -1 #덜 잘렸으면
            
print(end)
                
        