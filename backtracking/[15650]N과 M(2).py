# https://www.acmicpc.net/problem/15650
# N과 M(2)

from sys import stdin as s
from collections import deque
# s=open("input.txt","rt")

n,m=map(int,s.readline().split())

arr=[i for i in range(1,n+1)]
check=[0 for _ in range(1,n+1)]
res=deque()

def DFS(a,L):
    if L==m:
        for i in range(m):
            print(res[i],end=" ")
        print()
    else:
        for i in range(a+1,n):
            if check[i]==0:
                check[i]=1
                res.append(arr[i])
                DFS(i,L+1)
                check[i]=0
                res.pop()



for i in range(n):
    check[i]=1
    res.append(arr[i])
    DFS(i,1)
    check[i]=0
    res.pop()

####################################################
# # https://www.acmicpc.net/problem/15650
# # N과 M(2)
# # 라이브러리 사용

# from sys import stdin as s
# from collections import deque
# from itertools import combinations

# # s=open("input.txt","rt")

# n,m=map(int,s.readline().split())

# arr=[i for i in range(1,n+1)]
# res=list(combinations(arr,m))

# for i in res:
#     for j in i:
#         print(j,end=" ")
#     print()