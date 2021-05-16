# https://www.acmicpc.net/problem/9046
# 복호화

from sys import stdin as s
import operator

# s=open("input.txt","rt")

t=int(s.readline().strip())




for _ in range(t):
    txt=s.readline().strip()

    max=0
    table = dict()
    for c in txt:
        if c!=' ':
            if c not in table:
                table[c]=0
                table[c]+=1
            else:
                table[c]+=1

    table = sorted(table.items(),key=operator.itemgetter(1), reverse=True)

    if len(table)!=1 and table[0][1]==table[1][1]:
        print("?")
    else:
        print(table[0][0])


        