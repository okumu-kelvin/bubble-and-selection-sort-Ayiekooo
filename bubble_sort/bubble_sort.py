def bubble_sort(unsorted_list):
    n = len(unsorted_list)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):  # reduce comparisons each pass
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True
        if not swapped:  # stop if already sorted
            break

    return unsorted_list
