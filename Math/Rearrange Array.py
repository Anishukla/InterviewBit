# -*- coding: utf-8 -*-
"""
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.
"""

class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        di = {}
        for i in range(len(A)):
            di.update({i:A[i]})
            
        L = []
        for i in A:
            L.append(di[i])
            
""" 
Alternatively
"""

class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        di = {}
        N = len(A)
        for i in range(N):
            A[i] = A[i]+(A[A[i]]%N)*N
        
        L = []
        for i in range(N):
            A[i] = A[i]//N