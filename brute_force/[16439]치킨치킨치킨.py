# https://www.acmicpc.net/problem/16439
# 치킨치킨치킨
from sys import stdin as s
from itertools import combinations
# s=open("input.txt","rt")

n,m=map(int,s.readline().split())

ck=[]
arr=[i for i in range(m)]

a=[0 for i in range(n)]

for _ in range(n):
    ck.append(list(map(int,s.readline().split())))

res=0

li=combinations(arr,3)

total=0
for l in li:
    for i in l:    
        for j in range(n):
            if ck[j][i]>a[j]:
                a[j]=ck[j][i]
    tmp=sum(a)
    if res<tmp:
        res=tmp
    for k in range(n):
        a[k]=0

print(res)