"""Given an integer array nums,
 rotate the array to the right by k steps, 
 where k is non-negative."""


#using built-in functions - timelimit exceeded for big arrays
#time complexity: O(k)  
def rotate_array(nums, k):
    n = len(nums)
    for i in range(k):
        p = nums.pop()
        nums.insert(0, p)
    return nums

print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))  # Output: [5, 6, 7, 1, 2, 3, 4]


#brute-force approach - time complexity: O(n*k)
def rotate_array_brute_force(nums, k):
    n = len(nums)
    k = k%n 
    for i in range(k):
        last = nums[-1]
        for j in range(n-1,0,-1):
            nums[j] = nums[j-1] 
        nums[0] = last 
    return nums

print(rotate_array_brute_force([1, 2, 3, 4, 5, 6, 7], 3))  # Output: [5, 6, 7, 1, 2, 3, 4]



#extra array - time complexity: O(n)
def rotate_array_extra_array(nums, k):
    n = len(nums)
    k = k%n 
    result = [0]*n 
    for i in range(n):
        result[(i+k)%n] = nums[i]
    for i in range(n):
        nums[i] = result[i]
    return nums

print(rotate_array_extra_array([1, 2, 3, 4, 5, 6, 7], 3))  # Output: [5, 6, 7, 1, 2, 3, 4]