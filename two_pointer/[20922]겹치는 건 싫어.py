# https://www.acmicpc.net/problem/20922
# 겹치는 건 싫어
from sys import stdin as s

# s=open("input.txt","rt")

n,k=map(int,s.readline().split())

num=list(map(int,s.readline().split()))

table=[0]*100001

p1=0
p2=0
l=1
m=1
while p2<n:
    table[num[p2]]+=1
    if table[num[p2]]<=k:
        p2+=1
    else:
        l=p2-p1
        if l>m:
            m=l
        while table[num[p2]]>k:
            table[num[p1]]-=1
            p1+=1
        p2+=1
l=p2-p1
if l>m:
    m=l

print(m)

