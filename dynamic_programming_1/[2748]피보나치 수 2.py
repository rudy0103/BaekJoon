# https://www.acmicpc.net/problem/2748
# 피보나치 수 2

from sys import stdin

stdin=open("input.txt","rt")

n=int(stdin.readline())

a=[]
a.append(0)
a.append(1)


for i in range(2,n+1):
    a.append(a[i-1]+a[i-2])

print(a[n])
