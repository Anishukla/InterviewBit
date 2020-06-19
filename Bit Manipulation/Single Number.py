# -*- coding: utf-8 -*-
"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note: Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        elements = {} 
    	for num in A:
    		if num not in elements:
    			elements[num] = True
    		else:
    			elements[num] = False

    	for key in elements.keys():
    		if elements[key]:
    			return key