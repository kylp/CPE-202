"""Insertion Sort written by Jae Park for CPE 202"""
import random
import time


def insertion_sort(arr):
    comparisons = 0
    size = len(arr)
    for i in range(1, size):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j], = arr[j], arr[j - 1]
            j -= 1
            comparisons += 1
        comparisons += 1
    return arr, comparisons


def algotime(arrsize):
    """ Takes in array size and returns the time it took to sort the array, along with the number of comparisons.
    Args:
        arrsize(int): the size of randomly generated array to test
    Returns:
         sort_time(int): the time it took to sort the array
         num_comp(int): number of comparisons made during the sort
    """
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


# change value or call function multiple times for different array lengths
algotime(500000)
