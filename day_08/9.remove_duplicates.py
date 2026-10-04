"""Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored."""

nums = [1,1,2]

nums.sort()

unique_element = nums[0]
j=0

for i in range(0,len(nums)):

    if nums[i] != unique_element:

        unique_element = nums[i]
        j+=1
        nums[i],nums[j] = nums[j],nums[i]

print(nums)

print("k = ",j+1)

print(nums)
 