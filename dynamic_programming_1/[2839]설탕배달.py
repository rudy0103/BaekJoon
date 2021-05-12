#https://www.acmicpc.net/problem/2839
#설탕 배달

from sys import stdin as s

# stdin=open("input.txt","rt")
n = int(s.readline())


a=[ 99999 for _ in range(5001)]
coin=[3,5]
a[3]=1
a[5]=1

for i in coin:
    for j in range(i,n+1):
        a[j]=min(a[j],a[j-i]+1)


if a[n]==99999:
    print(-1)
else:
    print(a[n])
