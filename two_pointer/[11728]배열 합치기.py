# https://www.acmicpc.net/problem/11728
# 배열 합치기
from sys import stdin as s
# s = open("input.txt","rt")

n,m=map(int, s.readline().split())

A=list(map(int,s.readline().split()))
B=list(map(int,s.readline().split()))

p1=0
p2=0

while True:
    if A[p1]<B[p2]:
        print(A[p1],end=' ')
        p1+=1
    else:
        print(B[p2],end=' ')
        p2+=1

    if p1==len(A):
        while p2<len(B):
            print(B[p2],end=' ')
            p2+=1
        break

    elif p2==len(B):
        while p1<len(A):
            print(A[p1],end=' ')
            p1+=1
        break

