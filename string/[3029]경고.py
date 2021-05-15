# https://www.acmicpc.net/problem/3029
# 경고 

from sys import stdin as s
import datetime

# s=open("input.txt","rt")

now=s.readline()
warning =s.readline()


now_h,now_m,now_s=map(int,now.split(":"))
warning_h,warning_m,warning_s=map(int,warning.split(":"))

wait_h=warning_h-now_h
wait_m=warning_m-now_m
wait_s=warning_s-now_s

if wait_s<0:
    wait_s+=60
    wait_m-=1
if wait_m<0:
    wait_m+=60
    wait_h-=1
if wait_h<0:
    wait_h+=24

if now==warning:
    print("24:00:00")
else:
    print(datetime.time(wait_h,wait_m,wait_s))