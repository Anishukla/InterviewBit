# -*- coding: utf-8 -*-
"""
You are given a string S, and you have to find all the amazing substrings of S.

Amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
"""
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        val = 0
        l = len(A)
        for i in range(l):
            if A[i]=='A' or A[i]=='E' or A[i]=='I' or A[i]=='O' or A[i]=='U' or A[i]=='a' or A[i]=='e' or A[i]=='i' or A[i]=='o' or A[i]=='u':
                val = val + (l-i)

        return val%10003