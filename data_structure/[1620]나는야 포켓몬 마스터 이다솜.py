# https://www.acmicpc.net/problem/1620
# 나는야 포켓몬 마스터 이다솜

from sys import stdin as s
import sys
from collections import deque
# s=open("input.txt","rt")

n,m=map(int,s.readline().split())


dic={}
for i in range(n):
    mon=s.readline().strip()
    dic[mon]=i+1
dic2={v:k for k,v in dic.items()}

for i in range(m):
    quiz=s.readline().strip()
    if quiz.isdigit():
        sys.stdout.write(str(dic2.get(int(quiz))+'\n'))
    else:
        sys.stdout.write(str(dic.get(quiz))+'\n')