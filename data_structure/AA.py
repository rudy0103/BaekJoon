from sys import stdin as s
import sys
s=open("input.txt","rt")

n,m=map(int,s.readline().split())

cnt=0

S=dict()
for i in range(n):
    S[s.readline().strip()]=1

for i in range(m):
    if s.readline().strip() in S:
        cnt+=1
print(cnt)
