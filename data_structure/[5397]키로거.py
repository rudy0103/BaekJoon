# https://www.acmicpc.net/problem/5397
# 키로거

from sys import stdin as s
from sys import stdout
from collections import deque
# s=open("input.txt","rt")

n=int(s.readline())


for i in range(n):
    kl=deque(s.readline().strip("\n"))
    p=0
    r=[]
    l=[]
    while kl:
        c=kl.popleft()
        if c=="<":
            if l:
                r.append(l.pop())
        elif c==">":
            if r:
                l.append(r.pop())
        elif c=="-":
            if l:
                l.pop()
        else:
            l.append(c)

    left=''.join(l)
    right=''.join(r[::-1])
    res=''.join([left,right])
    print(res)