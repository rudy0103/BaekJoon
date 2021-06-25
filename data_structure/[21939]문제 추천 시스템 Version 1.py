# https://www.acmicpc.net/problem/21939
# 문제 추천 시스템 Version 1

import sys
import heapq as hq


sys.stdin=open("input.txt","rt")

visited=[[0,0]]*100001

n=int(input())

min_q=[[] for _ in range(101)]
max_q=[[] for _ in range(101)]
min_q2=[[] for _ in range(101)]
max_q2=[[] for _ in range(101)]


for _ in range(n):
    P,L,G=map(int,sys.stdin.readline().split())
    visited[P]=[L,G]
    hq.heappush(min_q[G],(L,P,G))
    hq.heappush(max_q[G],(-L,-P,-G))
    hq.heappush(min_q2[L],(L,P,G))
    hq.heappush(max_q2[L],(-L,-P,-G))
    hq.heappush(min_q[0],(L,P,G))
    hq.heappush(max_q[0],(-L,-P,-G))

def ret_high(L):
    l=L
    while not max_q2[l]:
        l+=1
    return l

def ret_low(L):
    l=L
    while not max_q2[l]:
        l-=1
    return l


m=int(input())

for _ in range(m):
    l=sys.stdin.readline().split()

    if l[0]=='add':
        visited[int(l[1])]=[int(l[2]),int(l[3])]
        hq.heappush(min_q[int(l[3])],(int(l[2]),int(l[1]),int(l[3])))
        hq.heappush(max_q[int(l[3])],(-int(l[2]),-int(l[1]),-int(l[3])))
        hq.heappush(min_q2[int(l[2])],(int(l[2]),int(l[1]),int(l[3])))
        hq.heappush(max_q2[int(l[2])],(-int(l[2]),-int(l[1]),-int(l[3])))


    elif l[0]=='solved':
        visited[int(l[1])]=[0,0]


    elif l[0]=="recommend":
        if l[2]=='1':
            if visited[-max_q[int(l[1])][0][1]]==[-max_q[int(l[1])][0][0],-max_q[int(l[1])][0][2]]:
                sys.stdout.write(str(-max_q[int(l[1])][0][1])+'\n')
            else:
                while max_q[int(l[1])] and visited[-max_q[int(l[1])][0][1]] != [-max_q[int(l[1])][0][0],-max_q[int(l[2])][0][2]]:
                    hq.heappop(max_q[int(l[1])])
                sys.stdout.write(str(-max_q[int(l[1])][0][1])+'\n')

        elif l[2]=='-1':
            if visited[min_q[int(l[1])][0][1]]==[min_q[int(l[1])][0][1],min_q[int(l[1])][0][2]]:
                sys.stdout.write(str(min_q[int(l[1])][0][1])+'\n')
            else:
                while min_q[int(l[1])] and visited[min_q[int(l[1])][0][1]] != [min_q[int(l[1])][0][0],min_q[int(l[1])][0][2]]:
                    hq.heappop(min_q[int(l[1])])
                sys.stdout.write(str(min_q[int(l[1])][0][1])+'\n')

    elif l[0]=='recommend2': #분류와 상관없이 
        if l[1]=='1':
            if visited[-max_q[0][0][1]]==[-max_q[0][0][0],-max_q[0][0][2]]:
                sys.stdout.write(str(-max_q[0][0][1])+'\n')
            else:
                while max_q[0] and visited[-max_q[0][0][1]] != [-max_q[0][0][0],-max_q[0][0][2]]:
                    hq.heappop(max_q[0])
                sys.stdout.write(str(-max_q[0][0][1])+'\n')

        elif l[1]=='-1':
            if visited[min_q[0][0][1]]==[min_q[0][0][1],min_q[0][0][2]]:
                sys.stdout.write(str(min_q[0][0][1])+'\n')
            else:
                while min_q[0] and visited[min_q[0][0][1]] != [min_q[0][0][0],min_q[0][0][2]]:
                    hq.heappop(min_q[0])
                sys.stdout.write(str(min_q[0][0][1])+'\n')

    elif l[0]=='recommend3': #레벨 포함 recommen3 x L
        if l[1]=='-1':
            if visited[-max_q[0][0][1]]==[-max_q[0][0][0],-max_q[0][0][2]] and visited[-max_q[0][0][1]][0]<=int(l[2]):
                sys.stdout.write(str(-max_q[0][0][1])+'\n')
            else:
                while max_q[0] and visited[-max_q[0][0][1]] != [-max_q[0][0][0],-max_q[0][0][2]]:
                    hq.heappop(max_q[0])
                if visited[-max_q[0][0][1]][0]<=int(l[2]):
                    sys.stdout.write(str(-max_q[0][0][1])+'\n')
                else:
                    L=ret_low(int(l[2]))
                    if max_q2[L] and visited[-max_q2[L][0][1]]==[-max_q2[L][0][0],-max_q2[L][0][2]]:
                        sys.stdout.write(str(-max_q2[L][0][1])+'\n')
                    else:
                        tmp=[]
                        while max_q2[L] and visited[-max_q2[L][0][1]]!=[-max_q2[L][0][0],-max_q2[L][0][2]]:
                            tmp.append(hq.heappop(max_q2))
                        if L>=1 and not max_q2[L]:
                            sys.stdout.write('-1\n')
                        else:
                            sys.stdout.write(str(-max_q2[L][0][1])+'\n')
                        for i in tmp:
                            hq.heappush(max_q2[L],i)

        if l[1]=='1':
            if visited[min_q[0][0][1]]==[min_q[0][0][0],min_q[0][0][2]] and visited[min_q[0][0][1]][0]>=int(l[2]):
                sys.stdout.write(str(min_q[0][0][1])+'\n')
            else:
                while min_q[0] and visited[min_q[0][0][1]] != [min_q[0][0][0],min_q[0][0][2]]:
                    hq.heappop(min_q[0])
                if visited[min_q[0][0][1]][0]>=int(l[2]):
                    sys.stdout.write(str(min_q[0][0][1])+'\n')
                else:
                    L=ret_high(int(l[2]))
                    if min_q2[L] and visited[min_q2[L][0][1]]==[min_q2[L][0][0],min_q2[L][0][2]]:
                        sys.stdout.write(str(min_q2[L][0][1])+'\n')
                    else:
                        tmp=[]
                        while min_q2[L] and visited[min_q2[L][0][1]]!=[min_q2[L][0][0],min_q2[L][0][2]]:
                            tmp.append(hq.heappop(min_q2[L]))
                        if L<=100 and not min_q2[L]:
                            sys.stdout.write('-1\n')
                        else:
                            sys.stdout.write(str(min_q2[L][0][1])+'\n')
                        for i in tmp:
                            hq.heappush(min_q2[L],i)

    # elif l[0]=='recommend3': #레벨 포함
    #     if l[1]=='-1':
    #         if visited[-max_q[0][0][1]]==[-max_q[0][0][0],-max_q[0][0][2]] and visited[-max_q[0][0][1]][0]<=int(l[2]):
    #             sys.stdout.write(str(-max_q[0][0][1])+'\n')
    #         else:
    #             while max_q[0] and visited[-max_q[0][0][1]] != [-max_q[0][0][0],-max_q[0][0][2]]:
    #                 hq.heappop(max_q[0])
    #             if visited[-max_q[0][0][1]][0]<=int(l[2]):
    #                 sys.stdout.write(str(-max_q[0][0][1])+'\n')
    #             else:
    #                 tmp=[]
    #                 while max_q[0] and visited[-max_q[0][0][1]] != [-max_q[0][0][0],-max_q[0][0][2]] or (max_q[0] and visited[-max_q[0][0][1]][0]>int(l[2])):
    #                     tmp.append(hq.heappop(max_q[0]))
    #                 if not max_q[0]:
    #                     sys.stdout.write('-1\n')
    #                 else:
    #                     sys.stdout.write(str(-max_q[0][0][1])+'\n')
    #                 for i in tmp:
    #                     hq.heappush(max_q[0],i)

    #     elif l[1]=='1':
    #         if visited[min_q[0][0][1]]==[min_q[0][0][0],min_q[0][0][2]] and visited[min_q[0][0][1]][0]>=int(l[2]):
    #             sys.stdout.write(str(min_q[0][0][1])+'\n')
    #         else:
    #             while min_q[0] and visited[min_q[0][0][1]] != [min_q[0][0][0],min_q[0][0][2]]:
    #                 hq.heappop(min_q[0])
    #             if visited[min_q[0][0][1]][0]>=int(l[2]):
    #                 sys.stdout.write(str(-min_q[0][0][1])+'\n')
    #             else:
    #                 tmp=[]
    #                 while min_q[0] and visited[min_q[0][0][1]] != [min_q[0][0][0],min_q[0][0][2]] or (min_q[0] and visited[min_q[0][0][1]][0]<int(l[2])):
    #                     tmp.append(hq.heappop(min_q[0]))
    #                 if not min_q[0]:
    #                     sys.stdout.write('-1\n')
    #                 else:
    #                     sys.stdout.write(str(min_q[0][0][1])+'\n')
    #                 for i in tmp:
    #                     hq.heappush(min_q[0],i)

                