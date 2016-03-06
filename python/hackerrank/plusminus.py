#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
pc=0.0
nc=0.0
zc=0.0
for i in range(n):
    if arr[i]<0:
        nc=nc+1
    elif arr[i]>0:
        pc=pc+1
    elif arr[i]==0:
        zc=zc+1

print round(pc/n,3)
print round(nc/n,3)
print round(zc/n,3)
