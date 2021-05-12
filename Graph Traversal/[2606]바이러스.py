#https://www.acmicpc.net/problem/2606
#바이러스

from sys import stdin
stdin=open("input.txt", "rt")



n= int(stdin.readline())
m= int(stdin.readline())



adj=[ [] for _ in range(n+1)]
ch = [ 0 for i in range(n+1)]


def DFS(a):
    if ch[a]==0:
        ch[a]=1;
        for i in adj[a]:
            next =i
            if(ch[next]==0):
                DFS(next)
    else:
        return;



for _ in range(m):
    src, dest = map(int, stdin.readline().split())
    adj[src].append(dest)
    adj[dest].append(src)

DFS(1)

cnt=0

for i in range(2, n+1):
    if ch[i]==1:
        cnt+=1

print(cnt)


