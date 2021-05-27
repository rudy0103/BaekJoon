# https://www.acmicpc.net/problem/2470
# 두 용액

from sys import stdin as s
# s=open("input.txt","rt")

n=int(s.readline())

l=list(map(int,s.readline().split()))
l.sort()

min=2147000000


p1=0
p2=n-1

res=2147000000
x=-2147000000
y=+2147000000

while p1<p2:
    if res>abs(l[p1]+l[p2]):
        res=abs(l[p1]+l[p2])
        x=l[p1]
        y=l[p2]
    if l[p1]+l[p2]>0:
        p2-=1
    else:
        p1+=1

print(x,y)