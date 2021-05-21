# https://www.acmicpc.net/problem/14502
# 연구소
from itertools import combinations
from collections import deque
import copy
from sys import stdin as s
# s=open("input.txt","rt")


n,m = map(int,s.readline().split())

Map=[]
for i in range(n):
    Map.append(list(map(int,s.readline().split())))


# 벽 3개 세우고 -> 안전 영역 확인 반복

# 빈공간에 벽 3개 세우기 -> 조합으로 해야함.

empty_space=deque() # 벽을 세울 3곳의 빈공간을 찾기위해
for i in range(n):
    for j in range(m):
        if Map[i][j]==0:
            empty_space.append((i,j))

comb_list=list(combinations(empty_space,3)) # combination으로 리스트를 만듬

virus=[]
for i in range(n):
    for j in range(m):
        if Map[i][j]==2:
            virus.append([i,j])


copy_Map=copy.deepcopy(Map)


dx=[1,0,-1,0]
dy=[0,1,0,-1]
Max_area=0
for wall in comb_list:
    for w in wall:
        Map[w[0]][w[1]]=1 #벽 3개 세우기
    Q=deque(virus)

    while Q:
        now=Q.pop()
        x=now[0]
        y=now[1]

        for i in range(4):
            xx= x+dx[i]
            yy= y+dy[i]

            if xx>=0 and xx<n and yy>=0 and yy<m:
                if Map[xx][yy]==0:
                    Q.append([xx,yy])
                    Map[xx][yy]=2
    cnt=0
    
    for a in range(n):
        for b in range(m):
            if Map[a][b]==0:
                cnt+=1

    if cnt>Max_area: # 최댓값 구하기
        Max_area=cnt

    
    for wa in wall:
        Map[wa[0]][wa[1]]=0 #세운 벽 다시 없애기

    Map=copy.deepcopy(copy_Map) # 바이러스 퍼진거 다시 초기화
        


print(Max_area)
