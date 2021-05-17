# https://www.acmicpc.net/problem/9342
# 염색체

from sys import stdin as s
# s=open("input.txt","rt")
t=int(s.readline().strip())


pattern=['A','B','C','D','E','F']

for _ in range(t):
    is_true=True
    inp_str=s.readline().strip()
    res=inp_str[0]

    for i in range(1,len(inp_str)):
        if inp_str[i] not in pattern:
            is_true=False
            res=""
            break
        if inp_str[i-1] != inp_str[i]:
            res+=inp_str[i]
    

    if res != "":
        if 'AFC' not in res:
            is_true=False
        elif len(res)>5:
            is_true=False

    if is_true:
        print("Infected!")
    else:
        print("Good")


