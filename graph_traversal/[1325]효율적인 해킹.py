# https://www.acmicpc.net/problem/1325
# 효율적인 해킹
from sys import stdin as s
import sys
# s=open("input.txt","rt")
n,m=map(int,s.readline().split())

graph=[[] for _ in range(n+1)]
cnt=[[i,0] for i in range(n+1)]
ch=[ 0 for i in range(n+1)]

for _ in range(m):
    c1,c2=map(int, s.readline().split())
    graph[c2].append(c1)

for i in range(1,n+1):
    Q=[]    
    Q.append(i)
    ch[i]=1
    while Q:
        now=Q.pop()
        for next in graph[now]:
            if ch[next]==0:
                Q.append(next)
                ch[next]=1
                cnt[i][1]+=1

    for j in range(1,n+1):
        ch[j]=0


cnt.sort(key=lambda x:(x[1],-x[0]),reverse=True)

max=cnt[0][1]

for c in cnt:
    if c[1]==max:
        print(c[0],end=" ")
    else:
        break
    