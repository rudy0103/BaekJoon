# https://www.acmicpc.net/problem/7569
# 토마토


from sys import stdin as s
from collections import deque

s=open("input.txt","rt")

n,m,hei = map(int, s.readline().strip().split())

box=[]

for _ in range(hei):
    li=[]
    for i in range(m):
        li.append(list(map(int,s.readline().split())))
    box.append(li)

dx=[1,0,-1,0]
dy=[0,1,0,-1]
dh=[0,1,-1]

Q=deque()


for k in range(hei):
    for i in range(m):
        for j in range(n):
            if box[k][i][j]==1:
                Q.append([k,i,j])

while Q:
    now=Q.popleft()
    h=now[0]
    x=now[1]
    y=now[2]

    for k in range(3):
        hh=h+dh[k]
        if hh>=0 and hh<=hei-1:
            if box[hh][x][y]==0:
                box[hh][x][y]=box[h][x][y]+1
                Q.append([hh,x,y])

    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if xx>=0 and xx<=m-1 and yy>=0 and yy<=n-1:
            if box[h][xx][yy]==0:
                box[h][xx][yy]=box[h][x][y]+1
                Q.append([h,xx,yy])

max=0
for k in range(hei):
    for i in range(m):
        for j in range(n):
            if box[k][i][j]==0:
                max=999999
            if box[k][i][j]>max:
                max=box[k][i][j]

print(box)

if max==999999:
    print(-1)
else:
    print(max-1)
                


        
