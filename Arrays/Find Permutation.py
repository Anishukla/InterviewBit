# -*- coding: utf-8 -*-
"""
Given a positive integer n and a string s consisting only of letters D or I, you have to find 
any permutation of first n positive integer that satisfy the given input string.
D means the next number is smaller, while I means the next number is greater.

Notes:
Length of given string s will always equal to n - 1
Your solution should run in linear time and space.
"""

class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        L = [0]*B
        val = 1
        req = B
        for i in range(len(A)):
            if A[i]=='I':
                L[i]=val
                val = val+1
                
            elif A[i]=='D':
                L[i]=req
                req = req-1
        
        L[B-1] = req
        
        return L
