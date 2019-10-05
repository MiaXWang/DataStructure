import random

def quickSort(array, l, r):
    if l < r:
        q = randPartition(array, l, r)
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

def randPartition(array, l, r):
    k = random.randint(l, r)
    array[r], array[k] = array[k], array[r]
    return partition(array, l, r)

a = [2,3,5,1,3,7]
quickSort(a, 0, 5)
print(a)


    