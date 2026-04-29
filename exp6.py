def find_max_with_sorting(nums):
    if not nums:
        return "List is empty"
    nums.sort() 
    return nums[-1]

print(find_max_with_sorting([]))            
print(find_max_with_sorting([5]))               
print(find_max_with_sorting([3, 3, 3, 3, 3]))    
