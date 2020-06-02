# -*- coding: utf-8 -*-
"""
Given a string, find the rank of the string amongst its permutations sorted lexicographically.
Assume that no characters are repeated.
"""

class Solution:
    # @param A : string
    # @return an integer
    def fact(self, n) : 
        f = 1
        while n >= 1 : 
            f = f * n 
            n = n - 1
        return f 
          
    def findSmallerInRight(self, st, low, high) : 
          
        countRight = 0
        i = low + 1
        while i <= high : 
            if st[i] < st[low] : 
                countRight = countRight + 1
            i = i + 1
       
        return countRight
    
    def findRank(self, A):
        ln = len(A) 
        mul = self.fact(ln) 
        rank = 1
        i = 0 
       
        while i < ln : 
              
            mul = mul / (ln - i) 
            countRight = self.findSmallerInRight(A, i, ln-1) 
       
            rank = rank + countRight * mul 
            i = i + 1
              
        return rank%1000003