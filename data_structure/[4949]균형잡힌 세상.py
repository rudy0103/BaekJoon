# https://www.acmicpc.net/problem/4949
# 균형잡힌 세상

from os import terminal_size
from sys import stdin as s
# s=open("input.txt","rt")

T=s.readline().strip('\n')

while T!=".":
    st=[]
    collect=True
    for c in T:
        if c=="(" or c=="[":
            st.append(c)
        elif c==")":
            if not st or st[-1]!="(":
                collect=False
                break
            else:
                st.pop()
        elif c=="]":
            if not st or st[-1]!="[":
                collect=False
                break
            else:
                st.pop()
    if st:
        collect=False

    if collect:
        print("yes")
    else:
        print("no")

    T=s.readline().strip('\n')
    