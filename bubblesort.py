def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    swapped = True
    k = 0
    while swapped:
        swapped = False
        k = k + 1
        for i in range(0, len(arr) - 1):
            # for better performance replace 1 with K,
            # so that further iterations are small for comparison.
            # This leaves out the sorted elements at the end.
            if arr[i] > arr[i + 1]:
                swap(i, i + 1)
                swapped = True
    return arr


def bubble_sort2(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    for k in range(0, len(arr) - 1):
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                swap(i, i + 1)
    return arr


arr = [3, 5, 2, 1, 6, 8, 0]
print arr
print(bubble_sort2(arr))
