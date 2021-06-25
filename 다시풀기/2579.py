# https://www.acmicpc.net/problem/2579
# 계단 오르기

import sys

sys.stdin=open("input.txt","rt")


n=int(input())
stairs=[0]*(n+1)
dy=[0]*(n+1)
for i in range(1,n+1):
    stairs[i]=int(sys.stdin.readline())
    dy[i]=stairs[i]

for i in range(n-2,0,-1):
    dy[i]=max(stairs[i]+dy[i+1],stairs[i]+dy[i+2])

print(dy)

