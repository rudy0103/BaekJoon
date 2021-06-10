# https://www.acmicpc.net/problem/19598
# 최소 회의실 개수
from sys import stdin as s
import heapq as hq
# s=open("input.txt","rt")

N=int(s.readline().strip())


meetings=[]             # N개의 회의
rooms=[]                # 최대 N개의 회의실

cnt=1                   # 회의실 1개 부터 시작

hq.heappush(rooms,(0))  # 기존 회의실에 진행중인게 없음으로 0을 넣어둠

for i in range(N):      # N개의 회의를 최소힙에 넣음
    start,end=map(int,s.readline().split())
    hq.heappush(meetings,(start,end))

# N개의 회의를 하나씩 빼면서 진행중인 회의중에 
# 가장 빨리 끝나는 회의를 찾아 교대 할지 새로 추가할지 판단.
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