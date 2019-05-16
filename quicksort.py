def quicksort(arr, start, end):
    if start< end:
        pindex = partition(arr, start, end)
        quicksort(arr, start, pindex -1)
        quicksort(arr, pindex +1, end)


def partition(arr, start, end):
    pindex = (start - 1)
    pivot = arr[end]
    for j in range(start, end):
        if arr[j] <= pivot:
            pindex = pindex + 1
            arr[pindex], arr[j] = arr[j], arr[pindex]

    arr[pindex + 1], arr[end] = arr[end], arr[pindex + 1]
    return (pindex + 1)


def qsort(list):
    if len(list) < 2:
        return list

    pivot = list.pop()
    left = filter(lambda x: x <= pivot, list)
    right = filter(lambda x: x > pivot, list)

    return qsort(left) + [pivot] + qsort(right)

arr = [7,2,1,6,8,5,3,4]
print "Before sort : " + str(arr)
n = len(arr)
print n
# quicksort(arr, 0, n-1)
# print "After sort : " + str(arr)
qsort(arr)

print "After sort : " + str(qsort(arr))