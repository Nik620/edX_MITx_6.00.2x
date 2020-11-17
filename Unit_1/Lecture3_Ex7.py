"""
Created on Mon Nov  2 10:39:33 2020

@author: Nik

MITx 6.00.2 Lecture 3 Exercise 7
"""


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.src) + '->' + str(self.dest) + ' (' + str(self.getWeight()) + ')'
