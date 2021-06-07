# https://www.acmicpc.net/problem/5430
# AC
from sys import stdin as s
import sys
from collections import deque
# s=open("input.txt","rt")


T=int(s.readline())

for _ in range(T):
    funcs=s.readline().strip()
    n=int(s.readline().strip())
    li=s.readline().lstrip("[").rstrip("]\n")
    reversed=False
    er=False
    if li!='':
        dq=deque(map(int,li.split(",")))
    else:
        dq=deque()
    for f in funcs:
        if f=='D':
            if not dq:
                sys.stdout.write("error"+'\n')
                er=True
                break
            else:
                if reversed:
                    dq.pop()
                else:
                    dq.popleft()
        else:
            if reversed:
                reversed=False
            else:
                reversed=True
    if not er:
        if reversed==True:
            dq.reverse()
         
        sys.stdout.write('[')
        while dq:
            sys.stdout.write(str(dq.popleft()))
            if dq:
                sys.stdout.write(',')
        sys.stdout.write(']'+'\n')
