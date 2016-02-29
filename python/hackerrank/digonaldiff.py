#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)

s=0
for i in range(n):
    s+=a[i][i]

s1=0
a.reverse()
for i in range(n):
    s1=s1+a[i][i]

print abs(s1-s)
