"""
Given a matrix, A of size M x N of 0s and 1s. If an element is 0, set its entire 
row and column to 0.

Note: This will be evaluated on the extra memory used. Try to minimize the space and 
time complexity.
"""

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, matrix):
        if matrix==None or len(matrix)==0:
            return
        cols=[False]*len(matrix[0])
        rows=[False]*len(matrix)
        
        for col in range(len(matrix[0])):
            for row in range(len(matrix)):
                if matrix[row][col]==0:
                    cols[col]=True
                    rows[row]=True
        for col in range(len(matrix[0])):
            for row in range(len(matrix)):
                if cols[col] or rows[row]:
                    matrix[row][col]=0
                    
        return matrix