def insertion_sort(arr, simulation=False):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor
        print arr
    return arr

arr = [3, 5, 2, 1, 6, 8, 0]
print arr
print(insertion_sort(arr))
