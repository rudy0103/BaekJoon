# https://www.acmicpc.net/problem/1764
# 듣보잡
import sys
from sys import stdin as s
# s=open("input.txt","rt")

n,m=map(int, s.readline().split())

cnt=0
A=dict()
res=[]


for _ in range(n):
    name=s.readline().strip()
    A[name]=1

for _ in range(m):
    name=s.readline().strip()
    if name in A:
        A[name]+=1

for k,v in A.items():
    if v==2:
        cnt+=1
        res.append(k)

res.sort()
print(cnt)
for i in res:
    sys.stdout.write(i+'\n')