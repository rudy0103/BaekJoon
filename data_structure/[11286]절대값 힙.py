# https://www.acmicpc.net/problem/11286
# 절대값 힙
from sys import stdin as s
import sys
import heapq as hq
# s=open("input.txt","rt")

N=int(s.readline().strip())

h=[]

for i in range(N):
    n=int(s.readline().strip())
    if n==0:
        if h:
            sys.stdout.write(str(hq.heappop(h)[1])+'\n')
        else:
            sys.stdout.write(str(0)+'\n')
    else:
        hq.heappush(h,(abs(n),n))
        
        


