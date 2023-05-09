#!/usr/bin/env python3

'''Successor with delete. Given a set of n integers S={0,1,...,n−1} 
and a sequence of requests of the following form:
- Remove x from S
- Find the successor of x: the smallest y in S such that y≥x.
design a data type so that all operations (except construction) 
take logarithmic time or better in the worst case.'''

import numpy as np

class Successor:
    def __init__(self, N):
        """Initialize Successor class.
        Args:
            N (int): the number of elements
        """
        self.S = np.array([i for i in range(0, N)], dtype=float)
        self.roots = np.array([i for i in range(1, N)], dtype=float)
        self.roots = np.append(self.roots, [N-1])
    
    def data_output(self):
        print("Set:\t", self.S)
        print("Roots:\t", self.roots)

    def remove(self:list, x: int):
        """Remove x from S.
        Return the successor of x."""
        if x == self.S[-1]:
            successor = self.S[-1]
            self.S = self.S[:-1]
            self.roots = self.roots[:-1]
            self.roots[-1] = self.S[-1]
            return int(successor)
        else:
            successor = self.roots[self.S == x]
            if len(successor) == 0:
                return None            
            self.roots = self.roots[self.S != x]
            self.S = self.S[self.S != x]
            self.roots[self.roots == x] = successor[0]
            return int(successor[0])
        

if __name__ == '__main__':
    data_set = Successor(N=8)
    data_set.data_output()
    element = 4
    successor = data_set.remove(element)
    if successor is None:
        print(f"The element {element} already removed!")
    else:
        print(f"The successor of {element} is {successor}")
    data_set.data_output()
    element = 4
    successor = data_set.remove(element)
    if successor is None:
        print(f"The element {element} already removed!")
    else:
        print(f"The successor of {element} is {successor}") 
        data_set.data_output()
    element = 7
    successor = data_set.remove(element)
    if successor is None:
        print(f"The element {element} already removed!")
    else:
        print(f"The successor of {element} is {successor}") 
    data_set.data_output()
