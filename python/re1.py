#!/usr/bin/python
import re

line = "<li><span>Publisher</span>Bantam Books, 1995</li>, <li><span>Language</span>English</li>, <li><span>ISBN-13</span>9780553280340</li>, <li><span>Binding</span>Paperback</li>";

match = re.match( r'Publisher', line, re.M|re.I)
if match:
   print "match --> match.group() : ", match.group()
else:
   print "No match!!"

search = re.search( r'Publisher', line, re.M|re.I)
if search:
   print "search --> search.group() : ", search.group()
else:
   print "Nothing found!!"
