# https://www.acmicpc.net/problem/1918
# 후위표기식

from sys import stdin as s
from collections import deque

# s=open("input.txt","rt")

inp=s.readline().strip()

st=deque()
inp=inp.lstrip('+')

for c in range(len(inp)):
    if inp[c]=="(":
        st.append(inp[c])
    elif inp[c] in "*/":
        while st and st[-1] in "*/":
            print(st.pop(),end="")
        st.append(inp[c])
    elif inp[c] in "+-":
        if not st and inp[c-1]!='(':
            st.append(inp[c])
        else:
            while st and st[-1]!='(':
                print(st.pop(),end="")
            if inp[c-1]!='(':
                st.append(inp[c])
    elif inp[c] ==")":
        while st and st[-1]!='(':
            print(st.pop(),end="")
        if st:
            st.pop()
    else:
        print(inp[c],end="")

while st:
    if st[-1] in "+-*/":
        print(st.pop(),end="")
    else:
        st.pop()

        


