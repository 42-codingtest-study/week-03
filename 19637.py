# https://www.acmicpc.net/problem/19637

import sys

input = sys.stdin.readline
if_list = []
score_set = set()
N, M = list(map(int, input().split()))
tmp_list = list(input().split())
tmp_list[0] = int(tmp_list[0])
score_set.add(tmp_list[0])
if_list.append(tmp_list)
for _ in range(N - 1) :
    tmp_list = list(input().split())
    tmp_list[0] = int(tmp_list[0])
    if (tmp_list[0] not in score_set) :
        score_set.add(tmp_list[0])
        if_list.append(tmp_list)
score_list = list(score_set)
for _ in range(M) :
    