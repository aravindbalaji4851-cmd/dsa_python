nums = [-2,1,-3,4,-1,2,1,-5,4]

maximum_sum = nums[0]

for i in range(0,len(nums)):

    for j in range(i,len(nums)):

        current_sum = sum(nums[i:j+1])

        if current_sum > maximum_sum:

            maximum_sum = current_sum
      
print(maximum_sum)
