"""Minimum Priority Queue
For:
    CPE202
    Sections 3 & 5
    Winter 2020
Author:
    Jae Park
"""


def index_parent(index):
    if index <= 0:
        return -1
    return (index - 1) // 2


def index_left(index):
    if index < 0:
        return -1
    return 2 * index + 1


def index_right(index):
    if index < 0:
        return -1
    return 2 * index + 2


def index_minchild(arr, index, num_items):
    if index_left(index) >= num_items:
        return -1
    if index_right(index) >= num_items:
        return index_left(index)
    if arr[index_left(index)] < arr[index_right(index)]:
        return index_left(index)
    return index_right(index)


def shift_down(arr, index, num_items):
    imin = index_minchild(arr, index, num_items)
    if imin < 0 or arr[imin] >= arr[index]:
        return None
    temp = arr[index]
    arr[index] = arr[imin]
    arr[imin] = temp
    return shift_down(arr, imin, num_items)


def shift_up(arr, index):
    iparent = index_parent(index)
    if iparent < 0 or arr[iparent] <= arr[index]:
        return
    temp = arr[index]
    arr[index] = arr[iparent]
    arr[iparent] = temp
    return shift_up(arr, iparent)


class MinPQ:
    """Minimum Priority Queue
    Attributes:
        capacity (int): the capacity of the queue. The default capacity is 2, but will be increased automatically.
        num_items (int): the number of items in the queue.
        arr (list): an array which contains the items in the queue.
    """

    def __init__(self, arr=None):
        if arr is None:
            self.capacity = 2
            self.num_items = 0
            self.arr = [None] * self.capacity
        else:
            self.capacity = len(arr)
            self.num_items = len(arr)
            self.arr = self.heapify(arr)

    def __eq__(self, other):
        return isinstance(other, MinPQ) \
               and self.capacity == other.capacity \
               and self.num_items == other.num_items \
               and self.arr == other.arr

    def __repr__(self):
        return 'MinPQ(%d, %d, %s)' % (self.capacity, self.num_items, repr(self.arr))

    def heapify(self, arr):
        """initialize the queue with a given array and conver the array into a min heap
        Args:
            arr (list): an array
        Returns:
            None : it returns nothing
        """
        i = index_parent(len(arr) - 1)
        while i >= 0:
            shift_down(arr, i, len(arr))
            i -= 1
        return arr

    def insert(self, item):
        """inserts an item to the queue
        If the capacity == the num_items before inserting an item, enlarge the array.

        Args:
            item (any): an item to be inserted to the queue. It is of any data type.
        Returns:
            None : it returns nothing
        """
        if self.num_items == self.capacity:
            self.enlarge()
        self.arr[self.num_items] = item
        shift_up(self.arr, self.num_items)
        self.num_items += 1
        return

    def del_min(self):
        """deletes the minimum item in the queue
        If the capacity > 2 and num_items > 0 and <= capacity // 4, shrink the array

        Returns:
            any : it returns the minimum item, which has just been deleted
        Raises:
            IndexError : Raises IndexError when the queue is empty
        """
        min_item = self.arr[0]
        self.arr[0] = self.arr[self.num_items-1]
        shift_down(self.arr, 0, self.num_items - 1)
        self.num_items -= 1
        if self.capacity > 2 and 0 < self.num_items <= self.capacity // 4:
            self.shrink()
        return min_item

    def min(self):
        """returns the minimum item in the queue without deleting the item
        Returns:
            any : it returns the minimum item 
        Raises:
            IndexError : Raises IndexError when the queue is empty
        """
        if self.arr is None:
            raise IndexError()
        return self.arr[0]

    def is_empty(self):
        """checks if the queue is empty 
        Returns:
            bool : True if empty, False otherwise. 
        """
        if self.num_items == 0:
            return True
        return False

    def size(self):
        """returns the number of items in the queue 
        Returns:
            int : it returns the number of items in the queue 
        """
        return self.num_items

    def enlarge(self):
        """enlarges the array.
        """
        self.capacity = 2 * self.capacity
        temp = [None] * self.capacity
        for i in range(self.num_items):
            temp[i] = self.arr[i]
        self.arr = temp

    def shrink(self):
        """shrinks the array.
        """
        if self.num_items > 2 * self.capacity:
            raise ValueError
        self.capacity = self.capacity // 2
        temp = [None] * self.capacity
        for i in range(self.num_items):
            temp[i] = self.arr[i]
        self.arr = temp
