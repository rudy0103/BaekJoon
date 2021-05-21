from sys import stdin as s
from collections import deque

s=open("input.txt","rt")

h,w = map(int, s.readline().split())

Map=[[0]*(h+2) for _ in range(w+2)]
Visited=[[0]*(h+2) for _ in range(w+2)]


for i in range(1,w+1):
    li=list(map(int,s.readline().split()))
    for j in range(1,h+1):
        Map[i][j]=li[j-1]


Q=deque()

Q.append([0,0])
Visited[0][0]=1

dx1=[0,1,0,-1,1,1]
dx2=[0,1,0,-1,-1,-1]
dy1=[1,0,-1,0, -1,1]



res=0

while Q:
    now=Q.pop()
    y=now[0]
    x=now[1]

    for i in range(6):
        if y%2==0:
            xx=x+dx2[i]
        else:
            xx=x+dx1[i]
        yy=y+dy1[i]
        if xx>=0 and xx<=h+1 and yy>=0 and yy<=w+1:
            if Map[yy][xx]==1:
                res+=1
            else:
                if Visited[yy][xx]==0:
                    Q.append([yy,xx])
                    Visited[yy][xx]=1


print(res)