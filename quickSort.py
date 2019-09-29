def quickSort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quickSort(array, l, q-1)
        quickSort(array, q+1, r)

def partition(array, l, r):
    k = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= k:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[r] = array[r], array[i+1]
    return i + 1
