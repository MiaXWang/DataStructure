import random

def partition(array, l, r):
    k = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= k:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[r] = array[r], array[i+1]
    return i+1

def randPartition(array, l, r):
    rand = random.randint(l, r)
    array[rand], array[r] = array[r], array[rand]
    return partition(array, l, r)

def randomSelect(array, l, r, k):
    if l < r:
        i = randPartition(array, l, r)
        t = r - i
        if t < k:
            randomSelect(array, l, i-1, k-t-1)
        else:
            randomSelect(array, i+1, r, k)
    return array[-k]

a = [4,2,3,5,1]
b =randomSelect(a, 0, 4, 2)
print(b)
print(a)
    
