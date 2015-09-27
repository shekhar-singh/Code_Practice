'''Write a Python function that creates and returns a list of prime numbers between 2 and N, inclusive, sorted in increasing order.This function takes in an integer and returns a list of integers.'''

def primesList(N):
    '''
    N: an integer
    '''
    # Your code here
    l=[]
    for num in range(2,N+1):
        if all(num%i!=0 for i in range(2,num)):
            l.append(num)
    return l
    print l
