# https://www.acmicpc.net/problem/11720
# 숫자의 합

from sys import stdin as s

# s=open("input.txt","rt")

n=s.readline().strip()
num=s.readline().strip()
sum=0
for i in num:
    sum+=int(i)

print(sum)


