# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 10:03:52 2020

@author: Nik P
MITx 6.00.2 Exercise 5.3
"""
import random

def deterministicNumber():
    '''
    Deterministically generates and returns 
    an even number between 9 and 21
    '''
    return 12

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return random.randrange(10,22,2)
