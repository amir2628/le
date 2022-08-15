from random import randint
import timeit

def quicksort(array):
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)]
    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    return quicksort(low) + same + quicksort(high)

array=[10, 5, 6,8,7,9]
print(timeit.timeit('print(quicksort(array))', number=1, globals=globals()))

import time
start = time.time()
print(quicksort(array))
print ("it took", time.time() - start, "seconds.")

#This is one of the sorting algorithms that I found to be faster than the other ones.
#I timed it and it became the fastest of all, so I chose this one.
