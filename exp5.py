def find_max(nums):
    if not nums:
        return None
    return max(nums)

# Test cases
print(find_max([1, 2, 3, 4, 5]))    
print(find_max([7, 7, 7, 7, 7]))    
print(find_max([-10, 2, 3, -4, 5])) 
