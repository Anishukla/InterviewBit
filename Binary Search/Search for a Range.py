# -*- coding: utf-8 -*-
"""
Given a sorted array of integers A(0 based index) of size N, find the starting and ending position
 of a given integar B in array A.

Your algorithm’s runtime complexity must be in the order of O(log n).

Return an array of size 2, such that first element = starting position of B in A and second 
element = ending position of B in A, if B is not found in A return [-1, -1]
"""

def first(arr,target,low,high):
    if low > high:
        return -1
    mid = (low+high)//2
    if arr[mid] == target and (mid == 0 or target > arr[mid-1]):
        return mid
    elif target > arr[mid]:
        return first(arr,target,mid+1,high)
    else:
        return first(arr,target,low,mid-1)

def last(arr,target,low,high):
    if low > high:
        return -1
    mid = (low+high)//2
    if arr[mid] == target and (mid == len(arr)-1 or target < arr[mid+1]):
        return mid
    elif target < arr[mid]:
        return last(arr,target,low,mid-1)
    else:
        return last(arr,target,mid+1,high)


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list0 of integers
    def searchRange(self, A, B):
        n = len(A)
        return [first(A,B,0,n-1),last(A,B,0,n-1)]