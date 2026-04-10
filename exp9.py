def binary_search(arr, key):
    # Important: Array must be sorted for Binary Search to work
    arr.sort() 
    
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == key:
            return f"Element {key} is found at position {mid}"
        elif arr[mid] < key:
            low = mid + 1  
        else:
            high = mid - 1             
            
    return f"Element {key} is not found"

arr = [3, 4, 6, -9, 10, 8, 9, 30]
print(binary_search(arr, 10)) 
print(binary_search(arr, 100))
