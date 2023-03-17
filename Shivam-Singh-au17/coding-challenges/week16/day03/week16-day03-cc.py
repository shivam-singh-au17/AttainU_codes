"""
Given an integer array nums sorted in non-decreasing order, remove the 
duplicates in-place such that
each unique element appears only once. The relative order of the elements 
should be kept the same. 

"""

class Solution:
    def removeDuplicates(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]   
        return i + 1
        