""" 
Q: Given a non-negative number represented as an array of digits,
add 1 to the number ( increment the number represented by the digits ).
The digits are stored such that the most significant digit is at the head of the list. """

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        N = len(A)
        i = 1
        while A[N-i]==9:
            A[N-i] = 0
            i = i+1
            
        if i == len(A)+1:
            A.insert(0, 1)
        
        else: 
            A[N-i] = A[N-i]+1
        
        j = 0
        while A[j]==0:
            A.pop(0)
            
        return A[j:]
