# https://www.acmicpc.net/problem/19598
# 최소 회의실 개수
from sys import stdin as s
import heapq as hq
# s=open("input.txt","rt")

N=int(s.readline().strip())


meeting=[]
using=[]

cnt=1

hq.heappush(using,(0))

for i in range(N):
    start,end=map(int,s.readline().split())
    hq.heappush(meeting,(start,end))

while meeting:
    meet=hq.heappop(meeting)
    earliest=hq.heappop(using)

    if meet[0]>=earliest:
        hq.heappush(using,meet[1])
    else:
        cnt+=1
        hq.heappush(using,earliest)
        hq.heappush(using,meet[1])




print(cnt)