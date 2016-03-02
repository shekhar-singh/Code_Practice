#!/bin/python

import sys
import re

time = raw_input().strip()
ap=re.compile(r'(\d+)(\w+)').search(time.split(':')[2]).group(2)
sec=re.compile(r'(\d+)(\w+)').search(time.split(':')[2]).group(1)
hr=time.split(':')[0]
mn=time.split(':')[1]
if ap == "PM":
    if hr !='12':
        hr = int(hr)+12
else:
    if hr == '12':
        hr="00"

print str(hr) + ":" + mn + ":" + sec
