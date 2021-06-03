# https://www.acmicpc.net/problem/2493
# 탑
from sys import stdin as s
import sys
from collections import deque
# s=open("input.txt","rt")


n=int(s.readline())
tower=deque(map(int,s.readline().split()))

tower.appendleft(0)

st=deque([0])


for i in range(1,n+1):
    if tower[st[-1]]<tower[i]:
        while tower[st[-1]]<tower[i]:
            st.pop()
            if not st:
                break
        if st:
            sys.stdout.write(str(st[-1])+' ')
        else:
            sys.stdout.write(str(0)+' ')
        st.append(i)
    else:
        sys.stdout.write(str(st[-1])+' ')
        st.append(i)