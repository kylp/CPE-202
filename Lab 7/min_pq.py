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
        raise IndexError()
    return (index - 1) // 2


def index_left(index):
    if index < 0:
        raise IndexError()
    return 2 * index + 1


def index_right(index):
    if index < 0:
        raise IndexError()
    return 2 * index + 2


def index_minchild(arr, index, capacity):
    if index_right(index) >= capacity:
        return index_left(index)
    


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
            self.arr = arr

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



    def insert(self, item):
        """inserts an item to the queue
        If the capacity == the num_items before inserting an item, enlarge the array.

        Args:
            item (any): an item to be inserted to the queue. It is of any data type.
        Returns:
            None : it returns nothing
        """
        pass

    def del_min(self):
        """deletes the minimum item in the queue
        If the capacity > 2 and num_items > 0 and <= capacity // 4, shrink the array

        Returns:
            any : it returns the minimum item, which has just been deleted
        Raises:
            IndexError : Raises IndexError when the queue is empty
        """
        pass

    def min(self):
        """returns the minimum item in the queue without deleting the item
        Returns:
            any : it returns the minimum item 
        Raises:
            IndexError : Raises IndexError when the queue is empty
        """
        pass

    def is_empty(self):
        """checks if the queue is empty 
        Returns:
            bool : True if empty, False otherwise. 
        """
        pass 
    
    def size(self):
        """returns the number of items in the queue 
        Returns:
            int : it returns the number of items in the queue 
        """
        pass 

    def enlarge(self):
        """enlarges the array.
        """
        pass

    def shrink(self):
        """shrinks the array.
        """
        pass
