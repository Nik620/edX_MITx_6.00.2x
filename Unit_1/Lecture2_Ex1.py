"""
Created on Thu Oct 29 11:59:19 2020

@author: Nikola
MITx 6.00.2 Lecture 2 Exercise 1
"""


def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    # Your code here
    
    # there are N items in the set
    N = len(items)
    
    # three possibilities: in bag1, in bag2, or neither
    # thus search through 3**n bags
    # Searching through all 3**n combos
    for i in range(3**N):
        # similar to first example, 
        bag1 = []
        bag2 = []
        for j in range(N):
            # i >> j is the same as i // 2**j
            if (i // 3**j) % 3 == 1:
                bag1.append(items[j])
            elif (i // 3**j) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)
