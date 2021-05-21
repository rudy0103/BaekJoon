# https://www.acmicpc.net/problem/2636
# 치즈
from sys import stdin as s
from collections import deque
s= open("input.txt","rt")

h,w = map(int,s.readline().split())

Map=[list(map(int,s.readline().split())) for _ in range(h)]
Visited=[[0]* w for _ in range(h)]


Q=deque()
Q.append([0,0])
dx=[0,1,0,-1]
dy=[1,0,-1,0]

time=0

def is_remain():
    global k
    cnt=0
    for i in range(h):
        for j in range(w):
            if Map[i][j]==1:
                cnt+=1
    if cnt!=0:
        k=cnt
    return cnt



while is_remain():
    time+=1
    Q=deque()
    Q.append([0,0])
    while Q:
        x,y=Q.pop()
        Visited[x][y]=1

        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]

            if xx>=0 and xx<h and yy>=0 and yy<w:
                if Map[xx][yy]==0 and Visited[xx][yy]==0:
                    Q.append([xx,yy])
                    Visited[xx][yy]=1

                elif Map[xx][yy]==1:
                    Map[xx][yy]=0
                    Visited[xx][yy]=1

    for i in range(h):
        for j in range(w):
            Visited[i][j]=0

                    


print(time)
print(k)