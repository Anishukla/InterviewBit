# -*- coding: utf-8 -*-
"""
Implement the next permutation, which rearranges numbers into the numerically next greater
 permutation of numbers for a given array A of size N.
If such arrangement is not possible, it must be rearranged as the lowest possible order i.e., 
sorted in an ascending order.
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, arr):
        i = len(arr) - 1
        
        if i==0:
            return arr
            
        while i > 0:
            if arr[i] > arr[i - 1]: 
                break
            i = i-1
            
        if i == 0: 
            return sorted(arr)
            
        i = i-1
    
        for j in reversed(range(i + 1, len(arr))):
            if arr[j] > arr[i]: 
                break
    
        arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1:] = reversed(arr[i + 1:])
        return arr
        
