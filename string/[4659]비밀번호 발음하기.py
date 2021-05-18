# https://www.acmicpc.net/problem/4659
# 비밀번호 발음하기

from sys import stdin as s
s=open("input.txt","rt")

inp_str=s.readline().strip()

def rule_1(ss):
    for c in ss:
        if c in "aeiou":
            return True
    
    return False

def rule_2(ss):
    vowel=0
    not_vowel=0

    for c in ss:
        if c in "aeiou":
            vowel+=1
            not_vowel=0
            if vowel==3:
                return False
        else:
            not_vowel+=1
            vowel=0
            if not_vowel==3:
                return False
        
    return True


def rule_3(ss):
    for i in range(1,len(ss)):
        if ss[i]==ss[i-1]:
            if ss[i] not in "eo":
                return False
    return True




while inp_str!="end":

    if rule_1(inp_str) and rule_2(inp_str) and rule_3(inp_str):
        print("<"+inp_str+"> is acceptable.")

    else:
        print("<"+inp_str+"> is not acceptable.")

    inp_str=s.readline().strip()


