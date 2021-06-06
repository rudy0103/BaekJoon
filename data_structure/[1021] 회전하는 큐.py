# https://www.acmicpc.net/problem/1021
# 회전하는 큐

from sys import stdin as s
from collections import deque
# s=open("input.txt","rt")
n,m=map(int,s.readline().split())

l=list(map(int,s.readline().split()))

q=deque(i for i in range(1,n+1))

cnt=0
for e in l:
    if q[0]==e:
        q.popleft()
    else:
        idx=q.index(e)
        while q[0]!=e:
            if idx<=int(len(q)/2):
                tmp=q.popleft()
                q.append(tmp)
                cnt+=1
            else:
                tmp=q.pop()
                q.appendleft(tmp)
                cnt+=1
        q.popleft()
print(cnt)

