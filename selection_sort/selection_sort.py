def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr  # Correct: return AFTER all loops finish

# Test the function (outside the bubble_sort function)
sorted_list = bubble_sort([30, 87, 16, 25, 12, 42])
print(sorted_list)