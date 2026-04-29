def sort_list(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

# Test cases
print(sort_list([]))
print(sort_list([1]))
print(sort_list([7, 7, 7, 7]))
print(sort_list([-5, -1, -3, -2, -4]))