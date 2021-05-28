# https://www.acmicpc.net/problem/15650
# N과 M(2)
# 라이브러리 사용

from sys import stdin as s
from collections import deque
from itertools import combinations

s=open("input.txt","rt")

n,m=map(int,s.readline().split())

arr=[i for i in range(1,n+1)]
res=list(combinations(arr,m))

for i in res:
    for j in i:
        print(j,end=" ")
    print()