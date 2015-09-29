
'''Wirite a Python function called satisfiesF that has the specification below. Then make the function call run_satisfiesF(L, satisfiesF). Your code should look like:'''

def satisfiesF(L):

   count= len(L)
   temp=list()

   for i in range(0,count):
     if(f(L[i])==False):
        temp.append(L[i])   

   if(temp):
     for j in temp:
      L.remove(j)



   return len(L)


def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print satisfiesF(L)
print L


run_satisfiesF(L, satisfiesF) 
