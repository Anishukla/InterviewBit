# -*- coding: utf-8 -*-
"""
You are in an infinite 2D grid where you can move in any of the 8 directions :

    (x,y) to 
    (x+1, y), 
    (x - 1, y), 
    (x, y+1), 
    (x, y-1), 
    (x-1, y-1), 
    (x+1,y+1), 
    (x-1,y+1), 
    (x+1,y-1)
    
You are given a sequence of points and the order in which you need to cover the points. 
Give the minimum number of steps in which you can achieve it. You start from the first point.
"""
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        L = []
        c = 0
        for i in range(len(A)-1):
            a = abs(A[i+1]-A[i])
            b = abs(B[i+1]-B[i])
            c = min(a, b)
            d = max(a, b)-c
            L.append(c+d)
            
        return sum(L)
