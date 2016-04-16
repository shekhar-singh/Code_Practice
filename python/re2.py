#!/usr/bin/python
import re

line = "<li><span>Publisher</span>Bantam Books, 1995</li>, <li><span>Language</span>English</li>, <li><span>ISBN-13</span>9780553280340</li>, <li><span>Binding</span>Paperback</li>";

searchObj = re.search( r'(Publisher)(.*?) .*', line, re.M|re.I)

if searchObj:
   print "searchObj.group() : ", searchObj.group()
   print "searchObj.group(1) : ", searchObj.group(1)
   print "searchObj.group(2) : ", searchObj.group(2)
else:
   print "Nothing found!!"
