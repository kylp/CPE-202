# Jae Park Lab 2 CPE 202 W 2020

class ArrayList:
    """Array List
    Attributes:
        capacity (int): the capacity of the list
        num_items (int): the number of items in the list
        arr (list): a python list construct which stores items
    """

    def __init__(self):
        self.capacity = 2
        self.num_items = 0
        self.arr = [None] * self.capacity

    def __eq__(self, other):
        return isinstance(other, ArrayList) and other.arr == self.arr and other.num_items == self.num_items

    def __repr__(self):
        return 'ArrayList(%s, %d, %d)' % (repr(self.arr), self.num_items, self.capacity)


def enlarge(lst):
    """double the original capacity of an array list
    Args:
        lst (ArrayList): an array list object
    Returns:
        ArrayList: an array list with double the original capacity
    """
    templst = [None] * 2 * lst.capacity
    for i in range(lst.num_items):
        templst[i] = lst.arr[i]

    lst.capacity = 2 * lst.capacity
    lst.arr = templst
    return lst


def shrink(lst):
    """shrink an array list by halving the original capacity.
    Args:
        lst (ArrayList): an array list object
    Returns:
        ArrayList: an array list with half the original capacity
    """

    templst = [None] * (lst.capacity//2)
    for i in range(lst.num_items):
        templst[i] = lst.arr[i]

    lst.capacity = (lst.capacity//2)
    lst.arr = templst
    return lst


def insert(lst, val, idx):
    """takes an object of ArrayList lst, a integer val, and an integer idx, 
    and insert the integer val to the arr of the ArrayList object at the index
    indicated by the integer idx, and returns the ArrayList object. 
    The function shall enlarge the ArrayList by calling the enlarge
    function when the ArrayList is full (num_items == capacity).
    Args:
        lst (ArrayList): an array list object
        val (int): a integer value
        idx (int): the index at which the val will be inserted
    Returns:
        ArrayList: an array list with the val inserted at the idx
    """
    if lst.num_items == lst.capacity:
        lst = enlarge(lst)
    for i in reversed(range(idx, lst.num_items)):
        lst.arr[i+1] = lst.arr[i]
    lst.arr[idx] = val
    lst.num_items += 1
    return lst


def get(lst, idx):
    """get an item stored at the index indicated by the integer idx
    Args:
        lst (ArrayList): an array list object
        idx (int): the index at which the val will be inserted
    Returns:
        int: an integer value stored at the idx in the lst
    Raises:
        IndexError if the index is out of bound ( >= num_items).
    """
    if idx >= lst.num_items or idx < 0:
        raise IndexError()
    return lst.arr[idx]


def contains(lst, val):
    """searches for the value in the list, and returns True if the value is found or False if not.
    Args:
        lst (ArrayList): an array list object
        val (int): a integer value
    Returns:
        bool: True if the value exists in the list, False otherwise.
    """
    for i in range(lst.num_items):
        if lst.arr[i] == val:
            return True
    return False


def search(lst, val):
    """Searches for val in an array list.
    Args:
        lst (ArrayList): an array list object
        val (int): a value to search for
    Returns:
        int: the index where the integer is stored in the lst 
             It returns None if the integer is not found.
    """
    for i in range(lst.num_items):
        if lst.arr[i] == val:
            return i
    return None

def remove(lst, val):
    """removes the first occurence of the val from the lst by shifting items on the right by one to the left.
    If the item to be removed is the last item in the ArrayList (index == num_items - 1),
    simply decrement the value of num_items by 1 (num_items -= 1). 
    The function shall shrink the ArrayList by calling the shrink function
    when the ArrayList is a quarter full (4 * num_items <= capacity), and the capacity is greater than 2 (capacity > 2).
    Args:
        lst (ArrayList): an array list object
        val (int): the value to be removed
    Returns:
        ArrayList: an array list with the val removed
    """

    temp = search(lst, val)
    if temp is None:
        return lst
    temp_lst, _ = pop(lst, temp)
    return temp_lst


def pop(lst, idx):
    """removes the val from the lst by shifting items on the right by one to the left.
    If the item to be removed is the last item in the ArrayList (index == num_items - 1),
    simply decrement the value of num_items by 1 (num_items -= 1). 
    The function shall shrink the ArrayList by calling the shrink function
    when the ArrayList is a quarter full (4 * num_items <= capacity), and the capacity is greater than 2 (capacity > 2).
    Args:
        lst (ArrayList): an array list object
        idx (int): the index at which the val will be inserted
    Returns:
        ArrayList: an array list with the val removed
        int: the removed value at the index
    Raises:
        IndexError: if idx is out of range.
    """
    if idx < 0 or idx >= lst.num_items:
        raise IndexError()

    temp = lst.arr[idx]

    for i in range(idx + 1, lst.num_items):
        lst.arr[i-1] = lst.arr[i]

    lst.num_items -= 1

    if 4 * lst.num_items <= lst.capacity and lst.capacity > 2:
        lst = shrink(lst)

    return lst, temp






def size(lst):
    """returns the number of items stored in the ArrayList object (returns num_items).
    Args:
        lst (ArrayList): an array list object
    Returns:
        int: the number of items stored in the array list
    """
    return lst.num_items
