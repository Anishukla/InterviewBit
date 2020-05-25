# -*- coding: utf-8 -*-
"""
Give a N*N square matrix, return an array of its anti-diagonals. 
Look at the example for more details.

Example:		
Input: 	
1 2 3
4 5 6
7 8 9
Return the following :
[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]
"""

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        l = len(A[0])
        if(l == 0):
            return 0
        final = []
        sol = []
        for d in range(2*l-1):
            for i in range(d+1):
                j = d-i
                if(j >= l or i >= l):
                    pass
                else:
                    final.append(A[i][j])
            sol.append(final)
            final = []
        return sol        