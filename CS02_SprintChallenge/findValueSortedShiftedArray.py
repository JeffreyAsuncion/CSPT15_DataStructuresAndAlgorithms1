"""
You are given a sorted array in ascending order that is rotated at some unknown pivot (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]) and a target value.

Write a function that returns the target value's index. If the target value is not present in the array, return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

[execution time limit] 4 seconds (py3)

[input] array.integer nums

[input] integer target

[output] integer

[Python 3] Syntax Tips
"""

def findValueSortedShiftedArray(nums, target):
    result = -1
    for index, value in enumerate(nums):
        #print(value, target)
        if value == target:
            result = index
            return result
    return result

    
#Example 1:
#Input: 
nums = [4,5,6,7,0,1,2] 
target = 0
print(findValueSortedShiftedArray(nums, target))
#Output: 4

#Example 2:
#Input: 
nums = [4,5,6,7,0,1,2] 
target = 3
print(findValueSortedShiftedArray(nums, target))
#Output: -1