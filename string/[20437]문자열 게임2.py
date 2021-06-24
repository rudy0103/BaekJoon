# https://www.acmicpc.net/problem/20437
# 문자열 게임2

import sys

sys.stdin=open("input.txt","rt")

T = int(input())


for _ in range(T):                      #테스트케이스
    w=input().strip()
    k=int(input())
    adj=[[] for _ in range(26)] #각 문자의 인덱스를 갖는 인접리스트 생성

    mini=len(w)
    maxi=0

    if k==1:                            #k가 1일경우 1 1 출력
        print(1,1)
    else:
        for i in range(len(w)):
            adj[ord(w[i])-97].append(i) # adj에 문자에 맞는 인덱스를 인접리스트 형태로 넣음

        possible=False

        li=[]
        res=[]
        for i in range(26):
            if len(adj[i]) >=k: # k개 이상인 문자가 있는지 확인
                possible=True # possible을 True로 바꿔 줌
                li.append(adj[i]) # k개 이상인 문자만 li에 다시 넣음
                

        if possible:  #possible 일때 인덱스를 저장한 인접리스트를 활용
            for ch in li:
                for i in range(len(ch)-k+1): 
                    res.append((ch[i+k-1]-ch[i]+1)) #res배열에 k개 만큼 포함한 연산을 하여 append

            print(min(res),max(res))
        else:
            print(-1)


