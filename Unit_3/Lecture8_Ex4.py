# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 17:46:38 2020

@author: Nik

Lecture 8 Exercise 4
"""
import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    bucket = ['r', 'r', 'r', 'g', 'g', 'g']
    all_same = 0
    all_mix = 0
    # loop through trials to calculate same or mix
    while numTrials > 0:
        # initialize
        trial = bucket.copy()
        drawn = []
        upper_lim = 5      
        # drawing the ball
        for i in range(0,3): # 3 draws
            draw = trial[random.randint(0,upper_lim)]
            trial.remove(draw)
            drawn.append(draw)
            upper_lim -= 1
        # checking if mix or same
        if drawn[0] == 'r' and drawn[1] == 'r' and drawn [2] == 'r':
            all_same += 1
        elif drawn[0] == 'g' and drawn[1] == 'g' and drawn [2] == 'g':
            all_same += 1
        else:
            all_mix += 1
        # reduce
        numTrials -= 1
    #return function
    return all_same / (all_same + all_mix)



print(noReplacementSimulation(1))
print(noReplacementSimulation(10))
print(noReplacementSimulation(100))
print(noReplacementSimulation(1000))
print(noReplacementSimulation(10000))
print(noReplacementSimulation(100000))
