#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.

Input 1:
    A = 3

Output 1:
    [   [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]   ]
"""

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        lst = [[0]*A for i in range(A)]
        t = 0
        l = 0
        b = A
        r = A
        val = 1
        while(l < r and t < b):
            for i in range(l,r):
                lst[t][i] = val
                val +=1
            t += 1
            for i in range(t,b):
                lst[i][r-1] = val
                val += 1
            r -= 1
            if(t < b):
                for i in range(r-1,l-1,-1):
                    lst[b-1][i] = val
                    val += 1
                b -= 1
            if(l < r):
                for i in range(b-1,t-1,-1):
                    lst[i][l] = val
                    val += 1
                l += 1
        return lst