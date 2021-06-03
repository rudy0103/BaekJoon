from sys import stdin as s
import sys
# s=open("input.txt","rt")


n=int(s.readline())
tower=[0]
t=list(map(int,s.readline().split()))
tower+=t
table=[0]*500001

m=0


for i in range(1,n+1):
    if tower[i]>m:
        m=tower[i]
    table[i+1]=m
    if table[i]>=tower[i]:
        for j in range(i-1,0,-1):
            if tower[j] >= tower[i]:
                sys.stdout.write(str(j)+' ')
                break
    else:
       sys.stdout.write(str(0)+' ')