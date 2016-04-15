n = int(raw_input())
a = []
q = raw_input()
a = map(int,q.split())
x=sorted(a)
l=len(a)
if x[0]!=0 and x[n-1]!=0:
    r1 = x[0]*x[1]
    r2 = x[n-1]*x[n-2]
    
if r1 > r2:
	print r1
else:
	print r2

