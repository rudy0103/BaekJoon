# https://www.acmicpc.net/problem/19598
# 최소 회의실 개수
from sys import stdin as s
import heapq as hq
# s=open("input.txt","rt")

N=int(s.readline().strip())

rooms=[0]*100001

meetings=[]
cnt=0

for i in range(N):              #힙에 일단 다 넣음
    start,end=map(int,s.readline().split())
    hq.heappush(meetings,(start,end))

while meetings:                 # 가장 빨리 시작하는 회의부터 꺼냄
    start,end=hq.heappop(meetings)
    for i in range(N):          # rooms를 순회하면서 비교하여 갱신
        if start>=rooms[i]:
            rooms[i]=end
            break

for i in range(N):               # 0이 아닌 회의실을 카운팅
    if rooms[i]!=0:
        cnt+=1
    else:
        break

print(cnt)