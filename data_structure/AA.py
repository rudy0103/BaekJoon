# https://www.acmicpc.net/problem/7662
# 이중 우선순위 큐

from sys import stdin as s
import sys
import heapq as hq
# s=open("input.txt","rt")

T=int(s.readline().strip())

for _ in range(T):
    n=int(s.readline().strip())
    visited=[False for _ in range(1000001)]
    minq=[]
    maxq=[]
    for i in range(n):
        op,val=s.readline().strip().split()

        if op =='I':
            hq.heappush(minq,(int(val),i))
            hq.heappush(maxq,(-int(val),i))
            visited[i]=True
        elif val=='-1':
            while minq and not visited[minq[0][1]]:
                hq.heappop(minq)
            if minq:
                visited[minq[0][1]]=False
                hq.heappop(minq)
        else:
            while maxq and not visited[maxq[0][1]]:
                hq.heappop(maxq)
            if maxq:
                visited[maxq[0][1]]=False
                hq.heappop(maxq)

    while minq and not visited[minq[0][1]]: hq.heappop(minq)
    while maxq and not visited[maxq[0][1]]: hq.heappop(maxq)
    print(f'{-maxq[0][0]} {minq[0][0]}' if maxq and minq else'EMPTY')

