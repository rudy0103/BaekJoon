# https://www.acmicpc.net/problem/11725
# 트리의 부모 찾기

from sys import stdin as s
# s=open("input.txt","rt")

n=int(s.readline().strip())

ch=[0 for _ in range(n+1)]
pnode=[0 for _ in range(n+1)]
graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    node1,node2=map(int,s.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

Q=[]
Q.append(1)

while Q:
    now=Q.pop(0)
    if ch[now]==0:
        ch[now]=1
        for node in graph[now]:
            if ch[node]==0:
                Q.append(node)
            if pnode[node]==0:
                pnode[node]=now

for i in range(2,n+1):
    print(pnode[i])