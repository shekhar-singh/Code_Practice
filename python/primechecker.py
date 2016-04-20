import math
import sys

def checkifprime(testnum):
	"""checks if testnum is prime, returns 1 if yes, 0 if no"""
	for a in xrange(2,int(testnum**.5)+1):
		if testnum % a == 0:
			return 0
	return 1

def findprimes_range(start, end):
	"""finds all primes in a range given by start and end"""
	if start >= end:
		return 0
	if start < 3:
		print 2
		start = 3
		if start >= end:
			return 0
	for a in range(start, end):
		if checkifprime(a):
			print a
	return 1

def findprimes_num(start, num):
	"""finds next num primes greater than or equal to start"""
	a = 0 #our counter
	if num < 1:
		return 0
	if start < 3:
		print 2
		start = 3
		a = 1 #since we already have 1 prime
	while a < num:
		if checkifprime(start):
			print start
			a = a + 1
		start = start + 1
	return 1

def findmersenne_range(start, end):
	"""finds all mersenne primes m=2^p-1 where p is prime between start and end"""
	if start >= end:
		return 0

	pstart = math.log(start+1, 2) #cycle through exponents for more speed
	pstart = int( math.ceil(p) )

	pend = math.log(end+1, 2)
	pend = int( math.ceil(p) )

	for a in range(pstart, pend):
		if checkifprime(a):
			m = x**p - 1
			if checkifprime(m):
				print m
	return 1

def findmersenne_num(start, num):
	"""finds num mersenne primes m=2^p-1 where p is prime greater than or equal to start"""
	a = 0 #counter
	if num < 1:
		return 0
	if start < 3:
		start = 3
	
	p = math.log(start+1, 2) #cycle through exponents for more speed
	p = int( math.ceil(p) )

	while a < num:
		if checkifprime(p):
			m = 2**p - 1
			if checkifprime(m):
				print m
				a = a + 1
		p = p + 1

def print_help():
	print "Prime checker"
usage: primes.py <PMpm> <start> <end | number>
options:
	P - search for primes in a range <start> to <end>
	M - search for mersenne primes in a range <start> to <end>
	p - find <number> primes greater than or equal to <start>
	m - find <number> mersenne primes greater to or equal to <start>"""

if len(sys.argv) == 4:
	if sys.argv[1] == 'P':
		findprimes_range(int(sys.argv[2]), int(sys.argv[3]))
	elif sys.argv[1] == 'M':
		findmersenne_range(int(sys.argv[2]), int(sys.argv[3]))
	elif sys.argv[1] == 'm':
		findmersenne_num(int(sys.argv[2]), int(sys.argv[3]))
	elif sys.argv[1] == 'p':
		findprimes_num(int(sys.argv[2]), int(sys.argv[3]))
	else:
		print_help()
else:
	print_help()
