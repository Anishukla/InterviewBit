#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given an array of integers A of size N and an integer B.
array A is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).

You are given a target value B to search. If found in the array, return its index, 
otherwise return -1.
"""

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        for i in range(len(A)):
            if A[i]==B:
                return i
        
        return -1