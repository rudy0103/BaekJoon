# https://www.acmicpc.net/problem/3986
# 좋은 단어

from sys import stdin as s
from collections import deque
# s=open("input.txt","rt")

n=int(s.readline())
cnt=0

for i in range(n):
    w=s.readline().strip("\n")
    st=[]
    for c in w:
        if c=='A':
            if st:
                if st[-1]=='A':
                    st.pop()
                else:
                    st.append(c)
            else:
                st.append(c)

        else:
            if st:
                if st[-1]=='B':
                    st.pop()
                else:
                    st.append(c)
            else:
                st.append(c)
    if not st:
        cnt+=1
print(cnt)