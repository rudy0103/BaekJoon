# https://www.acmicpc.net/problem/11365
# !밀비 급일
from sys import stdin as s


s=open("input.txt","rt")

cyphertxt=s.readline().strip()

while(cyphertxt!="END"):
    plaintxt=cyphertxt[::-1]
    print(plaintxt)
    cyphertxt=s.readline().strip()
