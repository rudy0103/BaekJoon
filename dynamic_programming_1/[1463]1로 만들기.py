# https://www.acmicpc.net/problem/1463
# 1로 만들기


import sys

# sys.stdin=open("input.txt","rt")

N=int(input())

dp=[99999999]*(N+10)

dp[1]=0
dp[2]=1
dp[3]=1

i=3
while i*3<N+1:
    dp[i*3]=dp[i]+1
    i*=3

i=2
while i*2<N+1:
    dp[i*2]=dp[i]+1
    i*=2

for i in range(1,N+1):
    if dp[i]==99999999:
        if i % 2==0:
            dp[i]=min(dp[int(i/2)]+1,dp[i])
        if i % 3==0:
            dp[i]=min(dp[int(i/3)]+1,dp[i])
        dp[i]=min(dp[i-1]+1,dp[i])

print(dp[N])
