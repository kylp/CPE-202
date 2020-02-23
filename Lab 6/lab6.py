"""Lab 6 for CPE 202 Jae Park"""
import random
import time


def insertion_sort(arr):
    comparisons = 0
    size = len(arr)
    for i in range(1, size):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j - 1], arr[j], = arr[j], arr[j-1]
            j -= 1
            comparisons += 1
        comparisons += 1
    return arr, comparisons


def algotime(arrsize):
    print("Timing insertion sort on ", arrsize, " items...")
    random.seed(1)
    alist = list(range(arrsize))
    random.shuffle(alist)
    start_time = time.time()
    sorted_list, num_comp = insertion_sort(alist)
    end_time = time.time()
    sort_time = end_time - start_time
    print("Done! Total time: ", sort_time)
    print("Number of comparisons made:", num_comp)
    print()
    return sort_time

algotime(500000)
