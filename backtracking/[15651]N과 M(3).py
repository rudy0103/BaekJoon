# https://www.acmicpc.net/problem/15651
# N과 M(3)


from sys import stdin as s
from collections import deque

# s=open("input.txt","rt")

n,m=map(int,s.readline().split())

arr=[i for i in range(1,n+1)]
res=deque()

def DFS(a,L):
    if L==m:
        for i in range(L):
            print(res[i],end=" ")
        print()
    else:
        for i in range(n):
            res.append(arr[i])
            DFS(i,L+1)
            res.pop()

for i in range(n):
    res.append(arr[i])
    DFS(i,1)
    res.pop()

##############################################################
# # https://www.acmicpc.net/problem/15651
# # N과 M(3)
# # 라이브러리 사용 product

# from sys import stdin as s
# from collections import deque
# from itertools import product

# # s=open("input.txt","rt")

# n,m=map(int,s.readline().split())

# arr=[i for i in range(1,n+1)]

# for i in product(arr,repeat=m):
#     for j in i:
#         print(j,end=" ")
#     print()