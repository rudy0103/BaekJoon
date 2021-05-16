# https://www.acmicpc.net/problem/10798
# 세로읽기

from sys import stdin as s
# s=open("input.txt","rt")

sl=[]
max=0
for _ in range(5):
    inp_str=s.readline().strip()
    sl.append(inp_str)
    if len(inp_str)>max:
        max=len(inp_str)


outp_str=""

idx=0

while idx<max:
    for ss in sl:
        if idx<len(ss):
            outp_str+=ss[idx]
    idx+=1

print(outp_str)

