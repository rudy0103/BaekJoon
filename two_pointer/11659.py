# https://www.acmicpc.net/problem/11659
# 구간 합 구하기 4

from sys import stdin as s
s=open("input.txt","rt")

n,m=map(int,s.readline().split())
numbers=[0]
numbers+=list(map(int,s.readline().split()))
numbers
table=[0]*(n+1)
for i in range(1,len(numbers)):
    table[i]=table[i-1]+numbers[i]

for i in range(m):
    p1,p2=map(int,s.readline().split())
    res=table[p2]-table[p1-1]
    
    print(res)