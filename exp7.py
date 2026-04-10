def remove_duplicates(nums):
    unique_elements = list(set(nums))
    return unique_elements

print(remove_duplicates([3, 7, 3, 5, 2, 5, 9, 2])) 
print(remove_duplicates([-1, 2, -1, 3, 2, -2]))   
print(remove_duplicates([1000000, 999999, 1000000])) 
