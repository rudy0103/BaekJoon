# https://www.acmicpc.net/problem/17609
# 회문

import sys
from collections import deque

# sys.stdin=open("input.txt","rt")

T=int(sys.stdin.readline().strip())

def is_palindrome(ss):
    s=deque(ss)
    while s:
        if len(s)>=2:
            if s[0]==s[-1]:
                s.pop()
                s.popleft()
            else:
                return False
        else:
            return True
    
    if not s:
        return True
            


for _ in range(T):
    st=sys.stdin.readline().strip()
    # print(is_palindrome(s))
    if is_palindrome(st):
        sys.stdout.write('0'+'\n')
    else:
        s=deque(st)
        while s and s[0]==s[-1]:
            s.popleft()
            s.pop()
        ss="".join(s)
        if is_palindrome(ss[:-1]) or is_palindrome(ss[1:]):
            sys.stdout.write('1'+'\n')
        else:
            sys.stdout.write('2'+'\n')


            
