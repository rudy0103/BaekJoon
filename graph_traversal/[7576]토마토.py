# https://www.acmicpc.net/problem/7576
# 토마토

from sys import stdin as s
from collections import deque

# s=open("input.txt","rt")

n,m = map(int, s.readline().strip().split())

box=[]

for i in range(m):
    box.append(list(map(int,s.readline().split())))


dx=[1,0,-1,0]
dy=[0,1,0,-1]

Q=deque()

for i in range(m):
    for j in range(n):
        if box[i][j]==1:
            Q.append([i,j])

while Q:
    now=Q.popleft()
    x=now[0]
    y=now[1]

    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if xx>=0 and xx<=m-1 and yy>=0 and yy<=n-1:
            if box[xx][yy]==0:
                box[xx][yy]=box[x][y]+1
                Q.append([xx,yy])

max=0
for i in range(m):
    for j in range(n):
        if box[i][j]==0:
            max=999999
        if box[i][j]>max:
            max=box[i][j]

if max==999999:
    print(-1)
else:
    print(max-1)
                


        
