# https://www.acmicpc.net/problem/11279
# 최대 힙
from sys import stdin as s
import sys
import heapq
# s=open("input.txt","rt")

h=[]

n=int(s.readline().strip())

for i in range(n):

    N=int(s.readline().strip())

    if N==0:
        if h:
            sys.stdout.write(str(heapq.heappop(h)[1])+'\n')
        else:
            sys.stdout.write(str(0)+'\n')
    else:
        heapq.heappush(h,(-N,N))



heapq.heapify
        