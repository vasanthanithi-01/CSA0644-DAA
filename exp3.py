def sum_of_squares(nums):
    total = 0
    n = len(nums)
    
    for i in range(n):
        unique_seen = set()
        for j in range(i, n):
            unique_seen.add(nums[j])
            
            count = len(unique_seen)
            
            total += (count * count)
            
    return total

# Test it with your example
print(sum_of_squares([1, 2, 1])) # Result: 15
