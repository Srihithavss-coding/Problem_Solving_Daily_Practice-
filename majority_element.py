"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""
#approach 1: Using HashMap 
# time complexity O(n)
# space complexity O(n)
def majority_element(nums):
    freq = dict()
    n = len(nums)
    for k in range(n):
        i = nums[k]
        freq[i] = freq.get(i,0)+1

        if freq[i]>n//2:
            return i
    return -1 

list1 = [3,2,3]
print("Using hashmap:", majority_element(list1))  # Output: 3


#approach 2: using sort  
# time complexity O(nlogn)
# space complexity O(1)

def majority_element_sort(nums):
    nums.sort()
    return nums[len(nums)//2]

list2 = [2,2,1,1,1,2,2]
print("Using sorting:", majority_element_sort(list2))  # Output: 2

#approach 3: using Boyer-Moore Voting Algorithm(without hashmap) 
# time complexity O(n)
# space complexity O(1)

def majority_element_boyer(nums):
    n = len(nums)
    candidate = nums[0]
    count = 1 
    for i in range(1,n):
        if count == 0:
            candidate = nums[i]
            count = 1 
        elif nums[i]== candidate:
            count += 1
        else:
            count -=1 

    return candidate 

print("Using Boyer-Moore Voting Algorithm:", majority_element_boyer(list2))  # Output: 2