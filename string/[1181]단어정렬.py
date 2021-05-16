# https://www.acmicpc.net/problem/1181
# 단어 정렬
from sys import stdin as s

# s=open("input.txt","rt")

n=int(s.readline().strip())


words=dict()


for _ in range(n):
    word=s.readline().strip()
    if word not in words:
        words[word]=len(word)

word_list=sorted(words.items(), key = lambda x:x[1])

for i in range(1,51):
    word_list_by_len=[]
    for word in word_list:
        if word[1]==i:
            word_list_by_len.append(word[0])
    word_list_by_len.sort()
    for w in word_list_by_len:
        print(w)

