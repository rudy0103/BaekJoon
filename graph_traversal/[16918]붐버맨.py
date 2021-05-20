# https://www.acmicpc.net/problem/16918
# 붐버맨

from sys import stdin as s
# s=open("input.txt","rt")
from collections import deque

dx=[1,0,-1,0]
dy=[0,1,0,-1]

r,c,n=map(int, s.readline().split())


Map=[[0]*c for _ in range(r)]


for i in range(r):
    inp_str=s.readline().strip()
    for j in range(len(inp_str)):
        if inp_str[j]==".":
            Map[i][j]=0
        else:
            Map[i][j]=1

sec=1
        
while sec<n:
    Q=deque()
    for i in range(r):
        for j in range(c):
            Map[i][j]+=1
            if(Map[i][j]==2):
                Q.append([i,j])
    sec+=1
    if sec==n:
        break

    while Q:
        now=Q.pop()
        x=now[0]
        y=now[1]
        Map[x][y]=0
        for k in range(4):
            xx=x+dx[k]
            yy=y+dy[k]

            if xx>=0 and xx<r and yy>=0 and yy<c:
                Map[xx][yy]=0
    sec+=1
    if sec==n:
        break

    

for i in range(r):
    for j in range(c):
        if Map[i][j]>0:
            print("O",end="")
        else:
            print(".",end="")
    print()



