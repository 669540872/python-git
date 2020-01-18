# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 18:27:23 2019

@author: Lenovo
"""

print("Hello Python")
print(2+3)
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2))
    
print(fib(10))