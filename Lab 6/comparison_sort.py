import random
import time


def insertion_sort(arr):
    """ Author: Jae Park
    Insertion sort for lab 6
    Args:
        arr(list): list to be sorted
    Returns:
        list: sorted list
        int: number of comparisons made during sort
    """
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
    sorted_list, num_comp = insertion_sort(alist)
    end_time = time.time()
    sort_time = end_time - start_time
    print("Done! Total time: ", sort_time)
    print("Number of comparisons made:", num_comp)
    print()
    return sort_time


# change value or call function multiple times for different array lengths
algotime(500000)


# Merge sort and selection sort
# Nathan Tang


def selection_sort(items):
    """Author: Nathan Tang
    sorts a list using selection_sort
    Args:
        items(list): a list of integers
    Returns:
        int: the number of comparisons
    """
    count = 0
    size = len(items)
    for i in reversed(range(1, size)):
        count += 1
        max_idx = 0
        for j in range(1, i):
            count += 1
            if items[j] > items[max_idx]:
                max_idx = j
        items[max_idx], items[i] = items[i], items[max_idx]
    return count


def merge_sort(items, count=0):
    """Author: Nathan Tang
    sort a list of items in ascending order using the merge sort algorithm
    Args:
        items(list): a list of integers or strings
    Returns:
        list: a copy of the original list with items sorted in ascending order
    """
    count += 1
    if len(items) <= 1:
        return items, count
    mid = len(items) // 2
    left, count_merge = merge_sort(items[:mid])
    count += count_merge
    right, count = merge_sort(items[mid:])
    count += count_merge
    count_merge, merged = merge(left, right)
    count += count_merge
    return merged, count


def merge(left, right):
    """Author: Nathan Tang
    merge two list into one as sorting items in ascending order
    Args:
        left(list): the left part of a list to be merged
        right(list): the right part of a list to be merged
    Returns:
        list: a merged and sorted list
    """
    count = 0
    merged = []
    left_idx = right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        count += 1
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    if left_idx < len(left):
        for i in range(left_idx, len(left)):
            merged.append(left[i])
    if right_idx < len(right):
        for i in range(right_idx, len(right)):
            merged.append(right[i])
    return count, merged


def bubble_sort(lst):
    """
    Author: Aidan Chandrasekaran
    :param lst: lst to be sorted
    :return: (int) number of compares
    """
    counter = 0
    for j in range(len(lst)):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                placeholder = lst[i + 1]
                lst[i + 1] = lst[i]
                lst[i] = placeholder
            counter += 1
    return counter


class MaxPQ:
    """
   Author: Aidan Chandrasekaran
   max heap class, max heap implemented with binary tree structure in array
   """

    def __init__(self, arr=None):
        if arr:
            self.capacity = len(arr)
            self.num_items = len(arr)
            self.arr = arr
            self.count = self.heapify(self.arr)
        else:
            self.capacity = 2
            self.arr = [None] * self.capacity
            self.num_items = 0

    def __repr__(self):
        return str(self.arr)

    def __eq__(self, other):
        return self.arr == other.arr

    def heapify(self, arr):
        """
       author: aidan chandrasekaran
       initialize the queue with a given array and convert the array into a max heap
       Args:
       arr (list): an array
       Returns:
       None : it returns nothing
       """
        counter = 0
        for i in range((len(arr) - 1) // 2, -1, -1):
            counter += self.shift_down(i)
        return counter

    def shift_down(self, idx):
        """
       Author: Aidan chandrasekaran
       shifts down an item in the queue using tail recursion.
       Use only < operator to compare two items: do not use <=, >, >=.
       YOU NEED TO DETERMINE WHERE THE END OF THE HEAP IS.
       YOU CAN USE self.num_items FOR DOING SO.
       Args:
       idx (int): the index of the item to be shifted down in the array.
       Returns:
       None : it returns nothing
       """
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left >= self.num_items or right >= self.num_items:
            return 1
        if self.arr[idx] < self.arr[left] and self.arr[left] >= self.arr[right]:
            tmp = self.arr[idx]
            self.arr[idx] = self.arr[left]
            self.arr[left] = tmp
            return 1 + self.shift_down(left)
        if self.arr[idx] < self.arr[right]:
            tmp = self.arr[idx]
            self.arr[idx] = self.arr[right]
            self.arr[right] = tmp
            return 1 + self.shift_down(right)
        return 1

    def dequeue(self):
        """
       Author: Aidan chandrasekaran
       dequeues the maximum item in the queue
       Returns:
           any : it returns the maximum item, which has just been deleted
       """
        return_val = self.arr[0]
        self.arr[0] = self.arr[self.num_items - 1]
        self.num_items -= 1
        counter = self.shift_down(0)
        return return_val, counter

    def heap_sort(self):
        """
       Author: Aidan Chandrasekaran
       :return: (int) count of compares
       """
        counter = 0
        while self.num_items > 1:
            new_sorted_bound = self.num_items - 1
            self.arr[new_sorted_bound], update = self.dequeue()
            counter += update
        return counter
