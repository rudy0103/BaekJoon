# https://www.acmicpc.net/problem/14425
# 문자열 집합

from sys import stdin as s
import sys
# s=open("input.txt","rt")

n,m=map(int,s.readline().split())

cnt=0

S=set()
for i in range(n):
    S.add(s.readline().strip())

for i in range(m):
    if s.readline().strip() in S:
        cnt+=1
print(cnt)
