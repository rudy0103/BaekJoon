# https://www.acmicpc.net/problem/2798
# 블랙잭

from sys import stdin as s
# s=open("input.txt","rt")

n,m=map(int,s.readline().split())

numbers=list(map(int,s.readline().split()))
visited=[0]*101
res=0

def dfs(a,L):
    if (L==3):
        global res
        total=0
        for i in range(n):
            if visited[i]==1:
                total+=numbers[i]
        if total<= m and total>res:
            res=total

    else:
        for i in range(a,n):
            if visited[i]==0:
                visited[i]=1
                dfs(i,L+1)
                visited[i]=0





dfs(0,0)

print(res)
