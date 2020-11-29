# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:18:51 2020

@author: Nikola

Lecture 7 Exercise 3
"""
def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if not L:
        return float('NaN')
    else:
        X = len(L)
        L_len = []
        for val in L:
            L_len.append(len(val))
        u = sum(L_len) / X
        sumsqr = 0
        for val2 in L_len:
            sumsqr += (val2 - u)**2
        std_dev = (sumsqr / X)**0.5
        return std_dev
            
            
        
L = ['a', 'z', 'p']
print(stdDevOfLengths(L)) #returns 0

L = ['apples', 'oranges', 'kiwis', 'pineapples']
print(stdDevOfLengths(L)) #returns 1.87
