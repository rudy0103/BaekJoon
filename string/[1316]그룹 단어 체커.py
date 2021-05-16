# https://www.acmicpc.net/problem/1316
# 그룹 단어 체커

from sys import stdin as s
# s=open("input.txt","rt")

n=int(s.readline().strip())

cnt=0


for _ in range(n):
    word=s.readline().strip()
    is_true=True
    for c in word:
        idx1=word.find(c)
        idx2=word.rfind(c)
        for k in range(idx1,idx2+1):
            if word[k] != c:
                is_true=False
    if is_true:
        cnt+=1

print(cnt)


