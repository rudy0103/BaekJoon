# https://www.acmicpc.net/problem/16953
# A->B
import sys
import heapq as hq
sys.stdin=open("input.txt","rt")

A,B=map(int,sys.stdin.readline().split())

cnt=0


while B>A:
    if B%2==0:
        B=int(B/2)
        cnt+=1
        if A==B:
            break
    elif B%10==1:
        B=int(B/10)
        cnt+=1
        if A==B:
            break
    else:
        break
if A==B:
    print(cnt+1)
else:
    print(-1)