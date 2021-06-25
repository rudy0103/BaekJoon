# https://www.acmicpc.net/problem/17626
# Four Squares

import sys
import math

# sys.stdin=open("input.txt","rt")

N=int(input())

dy=[999999]*50001

i=1
while i*i<=N+1:
    dy[i*i]=1
    i+=1



for i in range(1,N+1):
    for j in range(1,int(math.sqrt(i))):
        dy[i]=min(dy[i],dy[j*j]+dy[i-j*j])


print(dy[N])