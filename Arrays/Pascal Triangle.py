"""
Given numRows(here, A), generate the first numRows of Pascal’s triangle.
Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.
"""

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        if A <= 0:
            return []
            
        l = [[1]]
        for r in range(1, A):
            req = [1]
            for i in range(1,r):
                req.append(l[r-1][i-1] + l[r-1][i])
            req.append(1)
            l.append(req)
        return l