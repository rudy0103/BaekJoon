# https://www.acmicpc.net/problem/21758
# 꿀 따기

from sys import prefix, stdin as s
# s=open("input.txt","rt")
n=int(s.readline())
honey=[0]
honey+=list(map(int,s.readline().split()))
table=[0]*(n+1)

for i in range(1,len(honey)):
    table[i]=table[i-1]+honey[i]


res=0
# # case 1 꿀통이 가장 오른쪽에 있는 경우
b1=1
b2=2
while b2<n:
    sum=table[-1]-honey[b1]-honey[b2]
    sum+=table[-1]-table[b2]
    if sum>res:
        res=sum
    b2+=1

# # case 2 꿀통이 가장 왼쪽에 있는 경우

b1=n
b2=n-1
while b2>0:
    sum=table[-1]-honey[b1]-honey[b2]
    sum+=table[-1]-(table[-1]-table[b2-1])
    if sum>res:
        res=sum
    b2-=1

# # case 3 꿀통이 가운데 있는 경우

b1=1
b2=n
mid= int(b1+b2/2)

while True:
    sum=table[n-1]-honey[b1]-honey[b2]
    sum+=table[mid]
    if sum>res:
        res=sum
    break


print(res)

