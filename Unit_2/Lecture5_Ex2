"""
Created on Tue Nov 17 09:48:12 2020

@author: Nik P
MITx 6.00.2 Exercise 5.2
"""

# generate an even number between 0 <= x < 100, 
# not including 100
import random

def genEven():
    num = random.randint(0, 99)
    if num % 2 != 0:
        num = genEven()
    return num
