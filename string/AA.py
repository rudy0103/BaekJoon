T= int(input())
cnt= 0
for _ in range(T):
    N= list(input())
    for i in range(len(N)):
        if i != len(N)-1:  
            if N[i]==N[i+1]:
                pass
            elif N[i] in N[i+1:]:
                break
        else:
            cnt +=1
print(cnt)