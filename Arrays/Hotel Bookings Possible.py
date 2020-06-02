# -*- coding: utf-8 -*-
"""
A hotel manager has to process N advance bookings of rooms for the next season. 
His hotel has K rooms. Bookings contain an arrival date and a departure date. 
He wants to find out whether there are enough rooms in the hotel to satisfy the demand. 
Write a program that solves this problem in time O(N log N) .

Input:
First list for arrival time of booking.
Second list for departure time of booking.
Third is K which denotes count of rooms.

"""

class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        events = [(t, 1) for t in arrive] + [(t, 0) for t in depart]
        events = sorted(events)

        req = 0

        for event in events:
            if event[1] == 1:
                req = req+1
            else:
                req = req-1

            if req > K:
                return 0

        return 1
