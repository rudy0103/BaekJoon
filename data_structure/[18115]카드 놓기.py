# https://www.acmicpc.net/problem/18115
# 카드 놓기

from sys import stdin as s
import sys
from collections import deque
# s=open("input.txt","rt")

n=int(s.readline())

arr=list(map(int,s.readline().split()))
arr.reverse()
deq=deque()


for a in range(0,n):
    if arr[a]==1:
        deq.appendleft(a+1)
    elif arr[a]==2:
        tmp=deq.popleft()
        deq.appendleft(a+1)
        deq.appendleft(tmp)
    elif arr[a]==3:
        deq.append(a+1)

while deq:
    sys.stdout.write(str(deq.popleft())+' ')


