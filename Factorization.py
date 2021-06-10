# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 11:24:21 2021

@author: user
"""

def check_if_prime(num):
    if num > 1:
   # check for factors
       for i in range(2,num):
           if (num % i) == 0 :
                return False
       return True
 
    
def check(a,i):
     for j in a:
         for k in a:
             for l in a:
                 if ((j+k+l)==i):
                     return True
     return False
                 

a=[0 for o in range(0,303)]
o=0
for i in range(0,2001):
    x=check_if_prime(i)
    if (x==True):
        a[o]=i
        o=o+1;
gb=[]
o=-1
for i in a:
    if(i<1000) :
        continue
    o=o+1
    gb.append(check(a,i))
    
                
print(gb)
                    