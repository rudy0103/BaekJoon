# https://www.acmicpc.net/problem/4358
# 생태학
import sys

# sys.stdin=open("input.txt","rt")


d=dict()

n=0


while True:
    t=sys.stdin.readline().strip()
    if t=='':
        break
    if t not in d:
        d[t]=1
        n+=1
    else:
        d[t]+=1
        n+=1



res=sorted(d.keys())

for i in res:
    print("%s %.4f" % (i,d[i]*100/n))