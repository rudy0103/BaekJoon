# https://www.acmicpc.net/problem/1863
# 스카이라인 쉬운거

from sys import stdin as s
import sys
from collections import deque
# s=open("input.txt","rt")

n=int(s.readline())

st=[]
cnt=0
st.append(0)

for _ in range(n):
    x,y=map(int,s.readline().split())
    if st[-1]<y:
        st.append(y)
        cnt+=1
    elif st[-1]>y:
        while st and st[-1]>y:
            tmp=st.pop()
        if st[-1]==y:
            pass
        else:
            if st[-1]<y:
                st.append(y)
                cnt+=1

print(cnt)




