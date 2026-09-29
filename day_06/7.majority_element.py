"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

"""
nums = [2,2,1,1,1,2,2]

for i in nums:

    if nums.count(i) > len(nums)//2 :

        print(i)
        break
"""

# better method

nums = [2,2,1,1,1,2,2]

ans = None

count = 0

for i in nums:

    if count == 0:

        ans = i

    if ans == i :

        count += 1

    else: count -=1

print(ans)