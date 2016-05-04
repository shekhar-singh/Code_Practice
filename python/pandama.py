p=int(raw_input())
q=raw_input()
a=[]
a=map(int,q.split())
sorted(a)
l=len(a)
pp=a[0]*a[1]
qq=a[l-1]*a[l-2]
if pp > qq:
	print pp
else:
	print qq
