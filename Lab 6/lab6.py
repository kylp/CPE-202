"""Lab 6 for CPE 202 Jae Park"""
import random
import time

random.seed(1)

alist = random.sample(range(10000), 10)


def insertion_sort(arr):
    size = len(arr)
    for i in range(1, size):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j - 1], arr[j], = arr[j], arr[j-1]
            j -= 1
        return arr


start_time = time.time()
    #insert algorithm here
end_time = time.time()
sort_time = end_time - start_time
