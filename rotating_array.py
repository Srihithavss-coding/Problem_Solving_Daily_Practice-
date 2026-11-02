def rotate_array(nums, k):
    n = len(nums)
    for i in range(k):
        p = nums.pop()
        nums.insert(0, p)
    return nums

print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))  # Output: [5, 6, 7, 1, 2, 3, 4]