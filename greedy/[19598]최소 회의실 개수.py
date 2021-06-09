# https://www.acmicpc.net/problem/19598
# 최소 회의실 개수
from sys import stdin as s
import heapq as hq
s=open("input.txt","rt")

N=int(s.readline().strip())


meetings=[]
rooms=[]

cnt=1

hq.heappush(rooms,(0))

for i in range(N):
    start,end=map(int,s.readline().split())
    hq.heappush(meetings,(start,end))

while meetings:
    start,end=hq.heappop(meetings)
    earliest=hq.heappop(rooms)

    if start>=earliest:
        hq.heappush(rooms,end)
    else:
        cnt+=1
        hq.heappush(rooms,earliest)
        hq.heappush(rooms,end)




print(cnt)