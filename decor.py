# -*- coding: utf-8 -*-
"""
https://realpython.com/primer-on-python-decorators/

Created on Tue Apr 10 11:08:59 2018

@author: Sam-Sam
"""

def foo(bar):
    return bar + 1

print(foo(2)==3)
print(foo)
print(foo(2))
print(type(foo))

def call_foo_with_arg(foo, arg):
    return foo(arg)
    
print(call_foo_with_arg(foo, 3))

##Nested Functions

def parent():
    print("Printing from the parent() function.")
    
    def first_child():
        return "Printing from the first_child() function." 
    
    def second_child():
        return "Printing from the second_child() function."
        
    print(first_child())
    print(second_child())
    
