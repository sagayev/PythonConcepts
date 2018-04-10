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

def parent(num):
    print("Printing from the parent() function.")
    
    def first_child():
        return "Printing from the first_child() function." 
    
    def second_child():
        return "Printing from the second_child() function."
    
    try:
        assert num==10
        return first_child
    except AssertionError:
        return second_child
    
foo=parent(10)
bar=parent(11)

def my_decorator_old(some_function):
    
    def wrapper():
        print("Something is happening before some_function() is called")
        
        some_function()
        
        print("Something is happening after some_function is called")
        
    return wrapper
    
#def just_some_function():
#    print("Wheee!")
    
#just_some_function = my_decorator_old(just_some_function)
#just_some_function()
        
def my_decorator(some_function):
    def wrapper():
        
        num=10
        if num == 10:
            print("Yes!")
        else:
            print("No!")
            
        some_function()
        
        print("Something is happening after some_function() is called")
    return wrapper
    
#just_some_function = my_decorator(just_some_function)
from my_dec import my_decorator

@my_decorator
def just_some_function():
    print("Whee!")
