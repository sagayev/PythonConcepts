# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:52:02 2018

@author: Sam-Sam
"""

import time

def timing_function(some_function):
    """
    Outputs the time a function takes to execute
    """
    def wrapper():
        
        t1 = time.time()
        some_function()
        t2=time.time()
        return "Time it took to run the function: " + str(t2-t1)
    return wrapper
    
@timing_function
def my_function():
    num_list=[]
    for num in range(100000):
        num_list.append(num)
    print("\nSum of all numbers: " + str(sum(num_list)))
    

from time import sleep

def sleep_decorator(function):
    """
    Limits how fast the function is called
    """
    def wrapper(*args, **kwargs):
        sleep(2)
        return function(*args, **kwargs)
    return wrapper
    
@sleep_decorator
def print_number(num):
    return num