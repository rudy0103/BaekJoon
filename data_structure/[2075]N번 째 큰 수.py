# https://www.acmicpc.net/problem/2075
# N번 째 큰 수

import sys
import heapq as hq

# sys.stdin=open("input.txt","rt")

N=int(input())

q=[]

cnt=0

n=list(map(int,sys.stdin.readline().split()))
for i in n:
    hq.heappush(q,i)


for _ in range(N-1):
    n=list(map(int,sys.stdin.readline().split()))
    for i in n:
        if i > q[0]:
            hq.heapreplace(q,i)


print(hq.heappop(q))


    
