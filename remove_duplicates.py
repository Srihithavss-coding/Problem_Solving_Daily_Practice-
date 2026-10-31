"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k. To get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important, as well as the size of nums.
Return k.
"""

#using hashset to remove duplicates 

def remove_duplicates(nums):
    seen = set()
    count = 0 
    for i in nums:
        if i not in seen:
            seen.add(i)
            count += 1
    return count 

print("Number of unique elements:", remove_duplicates([0,0,1,1,1,2,2,3,3,4]))  # Output: 5

#using two-pointes approach 

def remove_duplications_two_pointer(nums):
    insert_pos = 1 
    for i in range(1, len(nums)):
        if nums[i]!= nums[insert_pos - 1 ]:
            nums[insert_pos] = nums[i]
            insert_pos += 1 

    return insert_pos

print("Number of unique elements using two-pointer approach:", remove_duplications_two_pointer([0,0,1,1,1,2,2,3,3,4]))  # Output: 5