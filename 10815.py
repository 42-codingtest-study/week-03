# https://www.acmicpc.net/problem/10815

int(input())	# 필요 없음 1
sg = set(map(int, input().split()))		# set 자료구조는 요소 검색 시 시간복잡도가 O(1)
int(input())	# 필요 없음 2
cards = list(map(int, input().split()))
for card in cards :
    if card in sg :						# 요소를 검색함
        print(1, end = ' ')
    else :
        print(0, end = ' ')
