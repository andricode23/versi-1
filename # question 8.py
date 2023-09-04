 # question 8
def sumList(nums):
    nums.sort()
    triplets = set()
    unique_nums = set(nums)
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                triplets.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return list(triplets)

# Test the function
nums = [-1, 0, 1, 2, -1, -4]
result = sumList(nums)
print(result)

