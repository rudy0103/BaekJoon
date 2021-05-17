# https://www.acmicpc.net/problem/1260
# DFS와 BFS

from sys import stdin as s
# s=open("input.txt","rt")

n,m,v=map(int,s.readline().split())

graph=[ [] for _ in range(n+1)]
ch = [ 0 for i in range(n+1)]



for _ in range(m):
    start,destination=map(int,s.readline().split())
    graph[start].append(destination)
    graph[destination].append(start)
for li in graph:
    li.sort()

def DFS(v):
    if ch[v]==0:
        ch[v]=1
        print(v,end=" ")
        for next in graph[v]:
            if(ch[next]==0):
                DFS(next)
    else:
        return;


Q=[]

def BFS(v):
    Q.append(v)
    while Q:
        now=Q.pop(0)
        if ch[now]==0:
            print(now,end=" ")
            ch[now]=1
            for node in graph[now]:
                Q.append(node)



DFS(v)
print()

for i in range(n+1):
    ch[i]=0


BFS(v)
