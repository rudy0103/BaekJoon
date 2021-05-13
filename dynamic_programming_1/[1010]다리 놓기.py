# https://www.acmicpc.net/problem/1010
# 다리 놓기

from sys import stdin as s
s=open("input.txt", "rt")


t= int(s.readline())
t
for _ in range(t):
    n,m = map(int, s.readline().split())
    k=1
    l=1
    for i in range(0,n):
        k*=(m-i)
    for i in range(n,0,-1):
        l*=i
    print(k/l)