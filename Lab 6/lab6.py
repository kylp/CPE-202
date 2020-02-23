"""Lab 6 for CPE 202 Jae Park"""
import random
import time


def insertion_sort(arr):
    size = len(arr)
    for i in range(1, size):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j - 1], arr[j], = arr[j], arr[j-1]
            j -= 1
    return arr


def algotime(arrsize):
    print("Timing insertion sort on " + str(arrsize) + " items...")
    random.seed(1)
    alist = list(range(arrsize))
    random.shuffle(alist)
    start_time = time.time()
    insertion_sort(alist)
    end_time = time.time()
    sort_time = end_time - start_time
    print("Done! Total time: " + str(sort_time))
    return sort_time


print(algotime(1000))
print(algotime(2000))
print(algotime(4000))
print(algotime(8000))
print(algotime(16000))
print(algotime(32000))
print(algotime(100000))
print(algotime(500000))

