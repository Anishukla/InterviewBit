# -*- coding: utf-8 -*-
"""
You are given two positive numbers A and B. You need to find the maximum valued integer X such that:

1. X divides A i.e. A % X = 0
2. X and B are co-prime i.e. gcd(X, B) = 1
"""

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B): 
        a = max(A, B)
        b = min(A, B)
        if b == 0: 
            return a
            
        elif a == b: 
            return a 
            
        elif a > b: 
            val = a%b
            a = b
            b = val
            return self.gcd(a, b)
    
    def cpFact(self, A, B):
        while self.gcd(A, B) != 1: 
            A = A / self.gcd(A, B)
        return int(A)
