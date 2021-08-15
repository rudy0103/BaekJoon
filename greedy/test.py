from sys import stdin as s

s=open("input.txt","rt",encoding='UTF8') #절대 경로도 되고, 상대 경로도 된다.
                         # r read t text 

ss=s.readline().strip()

print(ss[-3:-1])

cnt=0
tot=0
while ss:
    n=int(ss[-3:-1])
    tot+=n
    ss=s.readline().strip()
    cnt+=1

print(tot)
print(cnt)
