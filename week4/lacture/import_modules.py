# we can import modules using the import statement
"""
modules like
sys, random, datetime, statistics, math, os, json, re  etc

"""

import random

# choise from a list
input("Press Enter to flip a coin...") 
print(random.choice(['heads', 'tails']))


"""
now if we import only specific functions from a module
like

::::

from random import choice, randint

::::
then we can use those functions directly without prefixing them with the module name

but if you create a function or file with the same name as a module's function
then that will override the module's function

"""

# generate a random integer between 1 and 10
print(random.randint(1, 10))  # 1,10 both inclusive

# generate a random float between 0 and 1
print(random.random())  # 0.0 to 1.0

# shuffle a list
my_list = ["king", "queen", "jack", "ace"]
random.shuffle(my_list)
print(my_list)

# sample from a list
print(random.sample([1,2,3,4,5,6], 6))  # lottery numbers

# range(start, stop, step) gives a list of numbers from start to stop-1 with step

print(random.randrange(1, 10, 2))  # odd numbers between 1 and 10

import statistics

data = [1, 2, 2, 3, 4, 5, 5, 5, 6]  

print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))