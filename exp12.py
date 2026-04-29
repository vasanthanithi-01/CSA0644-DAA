def rob_line(nums):
    prev = curr = 0
    for num in nums:
        prev, curr = curr, max(curr, prev + num)
    return curr

def rob(nums):
    if len(nums) == 1:
        return nums[0]

    return max(rob_line(nums[:-1]), rob_line(nums[1:]))

nums = [2, 3, 2]
print(rob(nums))