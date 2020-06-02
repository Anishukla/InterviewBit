# -*- coding: utf-8 -*-
"""
A robot is located at the top-left corner of an A x B grid (marked ‘Start’ in the diagram below).
The robot can only move either down or right at any point in time.The robot is trying 
 to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).

How many possible unique paths are there?

Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.
"""

def nCr(n, r): 
    return (fact(n) / (fact(r)*fact(n - r))) 
  
def fact(n): 
    res = 1
    for i in range(2, n+1): 
        res = res * i 
    return res 
    
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        return nCr(A+B-2, A-1)
