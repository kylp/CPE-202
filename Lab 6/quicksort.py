import random
import time


def quick_sort(items, lo, hi):
    """Author: Jae Park
    Quicksort algorthim that also counts number of comparisons.
    Args:
        items(list): list to be sorted
        lo(int): lower bound
        hi(int): upper bound
    Returns:
        int: number of comparisons
    """
    comparisons = 0
    if lo >= hi:
        return comparisons
    mid = (lo + hi) // 2
    pivot = items[mid]
    lt, gt, i = lo, hi, lo
    while i <= gt:
        if items[i] < pivot:
            temp = items[i]
            items[i] = items[lt]
            items[lt] = temp
            i += 1
            lt += 1
            comparisons += 1
        elif items[i] > pivot:
            temp = items[i]
            items[i] = items[gt]
            items[gt] = temp
            gt -= 1
            comparisons += 2
        else:
            i += 1
            comparisons += 2
    comparisons += quick_sort(items, lo, lt - 1)
    comparisons += quick_sort(items, gt + 1, hi)
    return comparisons


def algotime(arrsize):
    """ Author: Jae Park
    Takes in array size and returns the time it took to sort the array, along with the number of comparisons.
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
    num_comp = quick_sort(alist, 0, len(alist) - 1)
    end_time = time.time()
    sort_time = end_time - start_time
    print("Done! Total time: ", sort_time)
    print("Number of comparisons made:", num_comp)
    print()
    return sort_time


if __name__ == '__main__':
    algotime(1000)
    algotime(2000)
    algotime(4000)
    algotime(8000)
    algotime(16000)
    algotime(32000)
    algotime(100000)
    algotime(500000)
