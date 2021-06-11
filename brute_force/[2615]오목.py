# https://www.acmicpc.net/problem/2615
# 오목


from os import pipe, terminal_size
from sys import stdin as s
# s=open("input.txt","rt")

m=[]
black=False
white=False
#오른쪽 오른쪽 대각선, 아래로,오른쪽 위 대각선
dx=[1,1,0,1]
dy=[0,1,1,-1]
point=[0,0]
for i in range(19):
    m.append(list(map(int,s.readline().split())))


def is_right(y,x,d,cnt):
    xx=x+dx[d]
    yy=y+dy[d]
    global white,black
    if xx>=0 and yy>=0 and xx<=18 and yy<=18:
        if m[yy][xx]==m[y][x]:
            return is_right(yy,xx,d,cnt+1)
        else:
            if cnt==5:
                if m[y][x]==1:
                    black=True
                    return True
                else:
                    white=True
                    return True
            else:
                return False
    elif cnt==5:
        if m[y][x]==1:
                black=True
                return True
        else:
            white=True
            return True
    
def f():
    global white,black
    for i in range(19):
        for j in range(19):
            cnt=1
            if m[i][j]!=0:
                for d in range(4):
                    xx=j+dx[d]
                    yy=i+dy[d]
                    if xx>=0 and yy>=0 and xx<=18 and yy<=18:
                        if m[yy][xx]==m[i][j]:
                            if is_right(yy,xx,d,cnt+1):
                                if (i-dy[d]>=0 and i-dy[d]<=18 and j-dx[d]>=0 and j-dx[d]<=18):
                                    if m[i-dy[d]][j-dx[d]]==m[i][j]:
                                        if m[i][j]==1:
                                            black=False
                                        else:
                                            white=False
                                    else:
                                        point[0]=i
                                        point[1]=j
                                        return
                                        break
                                else:
                                    point[0]=i
                                    point[1]=j
                                    return
                                    break


f()

if black:
    print(1)
    print(point[0]+1,point[1]+1)
elif white:
    print(2)
    print(point[0]+1,point[1]+1)
else:
    print(0)
