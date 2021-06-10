# https://www.acmicpc.net/problem/2615
# 오목


from sys import stdin as s
s=open("input.txt","rt")

m=[]
for i in range(19):
    m.append(list(map(int,s.readline().split())))
print(m)
