# -*- coding: utf-8 -*-
"""
Given a string S, find the longest palindromic substring in S.
"""

def longestPalindrome(self, s: str) -> str:
	def check(l, r):
		while 0 <= l and r < n and s[l] == s[r]: 
			l -= 1
			r += 1
		return l, r

	n, L, R = len(s), 0, 0
	for i in range(2*n-1):
		if i%2: l, r = check((i-1)//2, (i+1)//2)
		else: l, r = check(i//2, i//2)
		if r-l > R-L: L, R = l, r                
	return s[L+1:R]