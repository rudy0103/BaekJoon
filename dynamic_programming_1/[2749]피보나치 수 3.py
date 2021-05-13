# https://www.acmicpc.net/problem/2749
#피보나치 수 3
from sys import stdin as s

# stdin=open("input.txt","rt")

n=int(s.readline())

mod =1000000;
period = int(mod/10*15);

a=[0,1]



for i in range(2,period+1):
    a.append((a[i-1]+a[i-2])%mod)

idx = n%period
print(a[idx])
