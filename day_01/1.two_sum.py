lst = [1,5,6,7,8]

lst.sort()

target = 9

left = 0

right = len(lst)-1

while (left<right):

    current_sum = lst[left] + lst[right]

    if current_sum == target and lst[left]!= lst[right]:

        print(lst[left],lst[right])

        break

    elif current_sum > target :

        right -= 1

    elif current_sum < target:

        left += 1
