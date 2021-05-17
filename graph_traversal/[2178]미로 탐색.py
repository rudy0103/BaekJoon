# https://www.acmicpc.net/problem/2178
# 미로 탐색
from sys import stdin as s
# s=open("input.txt","rt")



n,m = map(int,s.readline().split())

Map=[]

for i in range(n):
    Map.append(list(map(int,s.readline().strip())))

Map

visited=[[0]*(m) for _ in range(n)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

Q=[]
Q.append([0,0])
visited[0][0]=1

while Q:
    now=Q.pop(0)
    now_x=now[0]
    now_y=now[1]
    visited[now_x][now_y]=1

    for i in range(4):
        next_x=now_x+dx[i]
        next_y=now_y+dy[i]

        if next_x>= 0 and next_x<=n-1 and next_y>=0 and next_y<=m-1:
            if Map[next_x][next_y]==1 and visited[next_x][next_y]==0:
                    Q.append([next_x,next_y])
                    Map[next_x][next_y]=Map[now_x][now_y]+1
                    
print(Map[n-1][m-1])






