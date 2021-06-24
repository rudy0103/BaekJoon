# https://www.acmicpc.net/problem/21939
# 문제 추천 시스템 Version 1

import sys
import heapq as hq


# sys.stdin=open("input.txt","rt")

visited=[0]*100001

n=int(input())

min_q=[]
max_q=[]

for _ in range(n):
    P,L=map(int,sys.stdin.readline().split())
    visited[P]=L
    hq.heappush(min_q,(L,P))
    hq.heappush(max_q,(-L,-P))


m=int(input())

for _ in range(m):
    l=sys.stdin.readline().split()

    if l[0]=='add':
        visited[int(l[1])]=int(l[2])
        hq.heappush(min_q,(int(l[2]),int(l[1])))
        hq.heappush(max_q,(-int(l[2]),-int(l[1])))


    elif l[0]=='solved':
        visited[int(l[1])]=0

    elif l[0]=='recommend':
        if l[1]=='1':
            if visited[-max_q[0][1]]==-max_q[0][0]:
                sys.stdout.write(str(-max_q[0][1])+'\n')
            else:
                while max_q and visited[-max_q[0][1]] != -max_q[0][0]:
                    hq.heappop(max_q)
                sys.stdout.write(str(-max_q[0][1])+'\n')

        elif l[1]=='-1':
            if visited[min_q[0][1]]==min_q[0][1]:
                sys.stdout.write(str(min_q[0][1])+'\n')
            else:
                while min_q and visited[min_q[0][1]] != min_q[0][0]:
                    hq.heappop(min_q)
                sys.stdout.write(str(min_q[0][1])+'\n')
                