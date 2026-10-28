"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Q. link: https://leetcode.com/problems/move-zeroes/description/
"""

def move_zeroes(nums):

    n = len(nums)
    left = 0 
    for right in range(n):
        if nums[right]!=0:
            nums[left] = nums[right]
            left+=1 

    while left < n:
        nums[left] =0 
        left+=1 
    
    return nums 


print(move_zeroes([0,1,0,3,12])) # Output: [1, 3, 12, 0, 0]